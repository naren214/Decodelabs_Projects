import contextlib
import io
import unittest
from unittest.mock import patch

import ExpenseTracker_Project_2 as tracker


class ExpenseTrackerTests(unittest.TestCase):
    def run_tracker(self, entries):
        output = io.StringIO()
        with patch('builtins.input', side_effect=entries), contextlib.redirect_stdout(output):
            tracker.main()
        return output.getvalue()

    def test_non_finite_and_negative_values_are_ignored_but_zero_is_allowed(self):
        output = self.run_tracker(['nan', 'inf', '-1', '0', '12.50', 'q'])
        self.assertIn('Number of expenses: 2', output)
        self.assertIn('Total spent: 12.50', output)

    def test_amount_that_overflows_running_total_is_rejected(self):
        output = self.run_tracker(['1e308', '1e308', 'q'])
        self.assertIn('Number of expenses: 1', output)
        self.assertIn('Total spent: 100000', output)
        self.assertNotIn('Total spent: inf', output)


if __name__ == '__main__':
    unittest.main()
