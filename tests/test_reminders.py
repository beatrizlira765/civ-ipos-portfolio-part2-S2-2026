import unittest
from src.task_manager import check_due_date


class TestReminders(unittest.TestCase):
    """
    Unit tests for reminders functionality, including overdue, due today and due tomorrow tasks.
    """

    def test_overdue(self):
        """
        Test adding a task with an overdue date.
        Verify that the function handles overdue input gracefully and returns the string "overdue".
        """
        result = check_due_date("20-12-2001", "14-10-2026")
        self.assertEqual(result, "overdue")


    def test_due_today(self):
        """
        Test adding a task with a task due today date.
        Verify that the function handles today date input gracefully and returns the string "today".
        """
        result = check_due_date("14-10-2026", "14-10-2026")
        self.assertEqual(result, "today")


    def test_due_tomorrow(self):
        """
        Test adding a task with a task due tomorrow.
        Verify that the function handles tomorrow date input gracefully and returns the string "tomorrow".
        """
        result = check_due_date("15-10-2026", "14-10-2026")
        self.assertEqual(result, "tomorrow")