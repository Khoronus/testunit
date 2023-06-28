import unittest

class ModulesTestUnit(unittest.TestCase):

    def test_run(self):
        try:
            return 0
        except Exception:
            self.fail("test_initialization raised an error")

if __name__ == "__main__":
    unittest.main()