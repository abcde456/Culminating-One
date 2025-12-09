import unittest
from caesar_utils import clean_text, encode, decode, chunk5, get_key

class TestCaesarUtils(unittest.TestCase):
    # Tests for clean_text
    def test_clean_text_basic(self):
        self.assertEqual(clean_text("Hello, World!"), "HELLOWORLD")

    def test_clean_text_with_numbers(self):
        self.assertEqual(clean_text("Python3.9"), "PYTHON")

    def test_clean_text_empty(self):
        self.assertEqual(clean_text(""), "")

    # Tests for encode
    def test_encode_basic(self):
        self.assertEqual(encode("ABC", 3), "DEF")

    def test_encode_wraparound(self):
        self.assertEqual(encode("XYZ", 3), "ABC")

    def test_encode_with_spaces(self):
        self.assertEqual(encode("HELLO WORLD", 5), "MJQQT BTWQI")

    # Tests for decode
    def test_decode_basic(self):
        self.assertEqual(decode("DEF", 3), "ABC")

    def test_decode_wraparound(self):
        self.assertEqual(decode("ABC", 3), "XYZ")

    def test_decode_with_spaces(self):
        self.assertEqual(decode("MJQQT BTWQI", 5), "HELLO WORLD")

    # Tests for chunk5
    def test_chunk5_basic(self):
        self.assertEqual(chunk5("HELLOWORLD"), ["HELLO", "WORLD"])

    def test_chunk5_short_text(self):
        self.assertEqual(chunk5("HI"), ["HI"])

    def test_chunk5_with_long_text(self):
        self.assertEqual(chunk5("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
                         ["ABCDE", "FGHIJ", "KLMNO", "PQRST", "UVWXY", "Z"])

if __name__ == '__main__':
    unittest.main()