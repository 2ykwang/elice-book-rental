import unittest


class TestTemplate(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_right(self) -> None:
        value = True
        EXPECTED = True
        self.assertEqual(EXPECTED, value)


if __name__ == "__main__":
    unittest.main()
