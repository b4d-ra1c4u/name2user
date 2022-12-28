from user_name_generator import UserNameGenerator
from user_name_creation_methods import UserNameCreationMethods
import unittest

# Test class
class TestName2User(unittest.TestCase):

    def test_build_usernames(self):

        result = UserNameGenerator.build_usernames("Liam Smith", None, UserNameCreationMethods.ALL.value)
        self.assertEqual(len(result), 6)

# Run the tests
if __name__ == '__main__':
    unittest.main()