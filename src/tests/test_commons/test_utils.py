import unittest
from src.crapi.commons.utils import build_path


class TestUtils(unittest.TestCase):
    def test_build_path(self) -> None:
        assert build_path("players", "#123456789"), "/players/%23123456789"


if __name__ == "__main__":
    unittest.main()
