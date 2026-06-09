import unittest

from tools.maca_env_snapshot import snapshot


class MacaEnvSnapshotTest(unittest.TestCase):
    def test_snapshot_has_expected_sections(self):
        report = snapshot()

        self.assertIn("python", report)
        self.assertIn("environment", report)
        self.assertIn("tools", report)


if __name__ == "__main__":
    unittest.main()
