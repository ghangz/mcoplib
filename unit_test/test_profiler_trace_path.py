import os
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from mcoplib.profiler import _trace_file_path


class ProfilerTracePathTest(unittest.TestCase):
    def test_trace_file_path_is_unique(self):
        with tempfile.TemporaryDirectory() as tmp_path:
            first = _trace_file_path(tmp_path, "fused_mla", 0)
            second = _trace_file_path(tmp_path, "fused_mla", 0)

        self.assertNotEqual(first, second)
        self.assertTrue(first.endswith(".json"))
        self.assertEqual(os.path.dirname(first), tmp_path)

    def test_trace_file_path_sanitizes_function_name(self):
        with tempfile.TemporaryDirectory() as tmp_path:
            path = _trace_file_path(tmp_path, "op/name with spaces", 1)

        filename = os.path.basename(path)
        self.assertTrue(filename.startswith("op_name_with_spaces_trace_rank_1_"))
        self.assertNotIn("/", filename)
        self.assertNotIn(" ", filename)


if __name__ == "__main__":
    unittest.main()
