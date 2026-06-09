import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tools.run_benchmark_with_logs import build_command


class RunBenchmarkWithLogsTest(unittest.TestCase):
    def test_build_command_forwards_extra_args(self):
        root = Path("/repo")
        command = build_command(root, "rms_norm", ["--generate", "--csv", "out.csv"])

        self.assertEqual(Path(command[1]), root / "benchmark" / "mcoplib_mxbenchmark_ops.py")
        self.assertEqual(command[2:], ["--op", "rms_norm", "--generate", "--csv", "out.csv"])


if __name__ == "__main__":
    unittest.main()
