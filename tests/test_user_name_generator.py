from name2user.user_name_generator import UserNameGenerator
from name2user.user_name_creation_methods import UserNameCreationMethods
from unittest import TestCase

# Test class
class TestName2User(TestCase):

    def test_build_usernames(self):

        # Check if the amount of results
        result = UserNameGenerator.build_usernames("Liam Smith", None, UserNameCreationMethods.ALL.value)
        self.assertEqual(len(result), 6)

        # Mail address
        result = UserNameGenerator.build_usernames("Liam Smith", "somecompany.com", UserNameCreationMethods.FIRST.value)
        self.assertEqual(result[0], "liam@somecompany.com")

        ## Simple, two part name
        ##########################################
        user = "Liam Smith"

        # Method: LAST
        result = UserNameGenerator.build_usernames(user, None, UserNameCreationMethods.LAST.value)
        self.assertEqual(result[0], "smith")

        # Method: FLAST
        result = UserNameGenerator.build_usernames(user, None, UserNameCreationMethods.FLAST.value)
        self.assertEqual(result[0], "lsmith")

        # Method: FDLAST
        result = UserNameGenerator.build_usernames(user, None, UserNameCreationMethods.FDLAST.value)
        self.assertEqual(result[0], "l.smith")

        # Method: FULL
        result = UserNameGenerator.build_usernames(user, None, UserNameCreationMethods.FULL.value)
        self.assertEqual(result[0], "liamsmith")

        # Method: FULLD
        result = UserNameGenerator.build_usernames(user, None, UserNameCreationMethods.FULLD.value)
        self.assertEqual(result[0], "liam.smith")

        # Method: FIRST
        result = UserNameGenerator.build_usernames(user, None, UserNameCreationMethods.FIRST.value)
        self.assertEqual(result[0], "liam")


        ## Multi part name
        ##########################################
        user = "Liam Tony Brown"

        # Method: LAST
        result = UserNameGenerator.build_usernames(user, None, UserNameCreationMethods.LAST.value)
        self.assertEqual(result[0], "brown")

        # Method: FLAST
        result = UserNameGenerator.build_usernames(user, None, UserNameCreationMethods.FLAST.value)
        self.assertEqual(result[0], "lbrown")

        # Method: FDLAST
        result = UserNameGenerator.build_usernames(user, None, UserNameCreationMethods.FDLAST.value)
        self.assertEqual(result[0], "l.brown")

        # Method: FULL
        result = UserNameGenerator.build_usernames(user, None, UserNameCreationMethods.FULL.value)
        self.assertEqual(result[0], "liamtonybrown")

        # Method: FULLD
        result = UserNameGenerator.build_usernames(user, None, UserNameCreationMethods.FULLD.value)
        self.assertEqual(result[0], "liam.tony.brown")

        # Method: FIRST
        result = UserNameGenerator.build_usernames(user, None, UserNameCreationMethods.FIRST.value)
        self.assertEqual(result[0], "liam")


# Run the tests
if __name__ == '__main__':
    TestCase.main()