import unittest
from translator import english_to_french, french_to_english
from ibm_cloud_sdk_core import api_exception

class TestTranslation(unittest.TestCase):
    def test_french_to_english(self):
        self.assertRaises(api_exception.ApiException, french_to_english, "")
        self.assertEqual(french_to_english("Merci"), "Thank you")
        self.assertEqual(french_to_english("Bonjour"), "Hello")
    
    def test_english_to_french(self):
        self.assertRaises(api_exception.ApiException, english_to_french, "")
        self.assertEqual(english_to_french("Thank you"), "Je vous remercie")     
        self.assertEqual(english_to_french("Hello"), "Bonjour")

unittest.main()