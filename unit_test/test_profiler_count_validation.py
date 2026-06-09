import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from mcoplib.profiler import _normalize_profile_count, profiler


class ProfilerCountValidationTest(unittest.TestCase):
    def test_normalize_profile_count_accepts_numeric_strings(self):
        self.assertEqual(_normalize_profile_count("repeat", "3", 1), 3)

    def test_normalize_profile_count_rejects_invalid_values(self):
        with self.assertRaisesRegex(ValueError, "warmup must be an integer"):
            _normalize_profile_count("warmup", "bad", 0)

    def test_normalize_profile_count_rejects_values_below_minimum(self):
        with self.assertRaisesRegex(ValueError, "repeat must be >= 1"):
            _normalize_profile_count("repeat", 0, 1)

    def test_profiler_validates_counts_when_decorator_is_created(self):
        with self.assertRaisesRegex(ValueError, "repeat must be >= 1"):
            profiler(repeat=0)


if __name__ == "__main__":
    unittest.main()
