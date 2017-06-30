import unittest
from primes import is_prime


class PrimeTestCase(unittest.TestCase):
    """Tests for 'primes.py'."""

    def test_is_five_prime(self):
        """Is five successfully determined to be prime?"""
        self.assertTrue(is_prime(5))

    def test_is_four_non_prime(self):
        """Is four correctly determined not to be prime?"""
        self.assertFalse(is_prime(4), msg='Four is not prime!')

    def test_is_zero_not_prime(self):
        """is zero correctly determined not to be prime?"""
        self.assertFalse(is_prime(0))

    def test_negative_number(self):
        """Is a negative number correctly determined not to be prime?"""
        self.assertFalse(is_prime(-1))



if __name__ == '__main__':
    unittest.main()

# https://jeffknupp.com/blog/2013/12/09/improve-your-python-understanding-unit-testing/
# Q: Why is testing important?
# A: Testing make sure your code works properly under a given set of conditions.
# Testing allows one to ensure that changes to the code did not break existing functionality.
# This is important in refactoring code. If you want to refactor code you need to write good tests!

# in the test we ASSERT that something is correct.
# Do NOT use assertTrue for each unit test because it is a cognitive burden on the reader fo the test.,

# Each test should test a single specific property of the code and by named appropriately.

# our code before never actually ran because our code threw an exception first!
# We can fix it by change it to range(2, number). But we should NOT remove our test!

# It's important to know BEFORE WRITING THE TEST what the output SHOULD BE!

