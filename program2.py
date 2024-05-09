import unittest
from program2 import decode_message

def decode_message(s: str, p: str) -> bool:
    if len(s) != len(p):
        return False

    i, j = 0, 0
    while i < len(s) and j < len(p):
        if p[j] == '?' or p[j] == s[i]:
            i += 1
            j += 1
        elif p[j] == '*':
            if j == len(p) - 1:
                return True
            while i < len(s) and s[i] != p[j+1]:
                i += 1
            j += 1
        else:
            return False

    return i == len(s) and j == len(p)


class TestDecoder(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(decode_message("aa", "a"), False)

    def test_case2(self):
        self.assertEqual(decode_message("a", "*"), True)

    def test_case3(self):
        self.assertEqual(decode_message("cb", "?a"), False)

    def test_case4(self):
        self.assertEqual(decode_message("abc", "?b?"), True)

if __name__ == '__main__':
    unittest.main()

