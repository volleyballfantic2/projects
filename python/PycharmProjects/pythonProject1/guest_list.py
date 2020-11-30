guests = []
guests.append('Neil Peart')
guests.append('Albert Einstein')
guests.append('George Washington')

for guest in guests:
    print(f"Hello {guest}, please join me for dinner.")

# a variable and pop.  or var and remove
# but replace is simplest
print(f"{guests[1]}, can not attend.")
guests[1] = 'Abraham Lincoln'

for guest in guests:
    print(f"Hello {guest}, please join me for dinner.")

guests.insert(0, 'Issac Newton')
guests.insert(3, 'Alexander the Great')
guests.append('Jesus Christ')

print(guests)
print(F"Number of guests is {len(guests)}")

