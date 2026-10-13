import unittest
from task_manager import get_status_color


class TestRichTable(unittest.TestCase):

    def test_completed_green(self):
        result = get_status_color("completed")
        self.assertEqual(result, "green")

    def test_pending_red(self):
        result = get_status_color("pending")
        self.assertEqual(result, "red")

if __name__ == "__main__":
    unittest.main()