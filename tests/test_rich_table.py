import unittest
from task_manager import get_status_color


class TestRichTable(unittest.TestCase):
    """
        Unit tests for checking RichTable functionality.
    """

    def test_completed_green(self):
        """
        Test verifying that the task has the completed status green.
        """
        result = get_status_color("completed")
        self.assertEqual(result, "green")

    def test_pending_red(self):
        """
        Test verifying that the task has the pending status red.
        """
        result = get_status_color("pending")
        self.assertEqual(result, "red")

if __name__ == "__main__":
    unittest.main()