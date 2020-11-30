import sys
import pygame
from pygame import mixer
from time import sleep

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


class AlienInvasion:
    """Overall Class to manage game and behaviors"""

    def __init__(self):
        """Initialize the game, and create resources"""
        pygame.init()
        self.settings = Settings()

        # Set screen size
        # self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # full screen
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Alien Invasion")

        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

        self.play_button = Button(self, "Play")

        mixer.init()
        self.beam_sound = mixer.Sound("sounds/beam.wav")
        self.gun_sound = mixer.Sound('sounds/gun.wav')
        self.pop_sound = mixer.Sound('sounds/pop.wav')
        self.crash_sound = mixer.Sound('sounds/crash.mp3')


    def run_game(self):
        """Start the main loop of game"""
        while True:
            # Watch keyboard and mouse for input events
            self._check_events()

            if self.stats.game_active:
                # position and update the Ship
                self.ship.update()
                # update bullet positions
                self._update_bullets()
                # alien ships
                self._update_aliens()
                #print(len(self.aliens))

            # Redraw the screen last
            self._update_screen()

    def _check_events(self):
        """Respond to keyboard and mouse for input events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        # end game if 'q' or esc is pressed *** critical in full screen mode
        elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_p:
            self._start_new_game()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        """ Update images and flip the screen  """
        self.screen.fill(self.settings.bg_color)
        self.ship.blit()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen)

        self.sb.show_score()

        if not self.stats.game_active:
            self.play_button.draw_button()

        # Make the most recently drawn screen visible
        pygame.display.flip()

    def _update_bullets(self):
        # positions bullets
        self.bullets.update()

        # get ride of bullets off screen
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
                # print(len(self.bullets))

        self._check_bullet_alien_collisions()

    def _repopulate_aliens(self):
        # no aliens left so repopulate. clear bullets and re create fleet
        if not self.aliens or len(self.aliens) == 0:
            self.settings.increase_speed()
            self.stats.level += 1
            self.sb.prep_level()
            self._reset_fleet()

    def _check_bullet_alien_collisions(self):
        # Check if bullet hit alien and remove them
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if collisions:
            self.pop_sound.play()
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

            # if no aliens left so repopulate. clear bullets and re create fleet
            if not self.aliens or len(self.aliens) == 0:
                self._repopulate_aliens()

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            self.gun_sound.play()

    def _create_fleet(self):
        if not self.aliens or len(self.aliens) == 0:
            alien = Alien(self)
            alien_width, alien_height = alien.rect.size
            available_space_x = self.settings.screen_width - (2 * alien_width)
            number_aliens_x = available_space_x // (2 * alien_width)  # // floor division

            ship_height = self.ship.rect.height
            available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
            number_rows = available_space_y // (2 * alien_height)

            # create the first row of aliens
            for row_number in range(number_rows):
                for alien_number in range(number_aliens_x):
                    self._create_alien(alien_number, row_number)

            print(f"create fleet {len(self.aliens)}")

    def _create_alien(self, alien_number, row_number):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _update_aliens(self):
        """
        Check if fleet hit a screen edge then
        Update the position of the alien fleet
        """
        self._check_fleet_edges()
        self.aliens.update()

        # look for alien and ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # aliens landed
        self._check_aliens_bottom()

    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        self.beam_sound.play()
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1


    def _reset_fleet(self):
        #print('reset')
        self.aliens.empty()
        self.bullets.empty()

        self._create_fleet()
        self.ship.center_ship()

    def _ship_hit(self):
        self.crash_sound.play()
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.sb.prep_ships()
            self._reset_fleet()
            # pause
            sleep(2.0)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _start_new_game(self):
        if not self.stats.game_active:
            self.stats.game_active = True

            # Reset game
            self.stats.reset_stats()
            self.sb.prep_score()
            self.sb.prep_high_score()
            self.sb.prep_level()
            self.sb.prep_ships()
            self.settings.initialize_dynamic_settings()
            self._reset_fleet()

            # Hide mouse cursor
            pygame.mouse.set_visible(False)

    def _check_aliens_bottom(self):
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break

    def _check_play_button(self, mouse_pos):
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self._start_new_game()


if __name__ == '__main__':
    # make an instance of the game and run it
    ai = AlienInvasion()
    ai.run_game()


