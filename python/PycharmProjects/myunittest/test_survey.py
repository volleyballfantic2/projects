import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the Class AnonymousSurvey"""

    def setUp(self):
        """
        Create a survey and set up responses to be used in test methods
        Unit test setup of responses
        """
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.test_responses = ['English', 'Spanish', 'Mandarin']


    def test_store_single_response(self):
        # question = "What language did you first learn to speak?"
        # my_survey = AnonymousSurvey(question)
        self.my_survey.store_response(self.test_responses[0])
        self.assertIn(self.test_responses[0], self.my_survey.responses)

        #print(self.my_survey.responses)

    def test_store_three_responses(self):
        # question = "What language did you first learn to speak?"
        # my_survey = AnonymousSurvey(question)
        # responses = ['English', 'Spanish', 'Mandarin']
        for response in self.test_responses:
            self.my_survey.store_response(response)

        for response in self.test_responses:
            self.assertIn(response, self.my_survey.responses)

        #print(self.my_survey.responses)

# run the unit tests
if __name__ == '__main__':
    unittest.main()