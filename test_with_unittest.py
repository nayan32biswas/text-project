import unittest

from solutions import SolutionOne, Person, SolutionTwo, SolutionThree


class TestProblemOne(unittest.TestCase):
    def setUp(self) -> None:
        self.data = {
            "key1": 1,
            "key2": {
                "key3": 1,
                "key4": {
                    "key5": 4
                },
                "key6": {},
                "key7": [1, 2, 3],
                "key8": {
                    "key9": "string",
                    "key 10": 0
                },
            }
        }
        return super().setUp()

    def match_all_keys(self, x, y):
        if len(x) != len(y):
            return False
        for value in y:
            value = " ".join(value.split()[:-1])
            if value not in x:
                return False
        return True

    def test_output(self):
        results = ["key1 1","key2 1","key3 2","key4 2","key5 3", "key6 2","key7 2","key8 2","key9 3","key 10 3",]
        obj = SolutionOne(self.data)
        executed_results = obj.get_results()
        self.assertEqual(results, executed_results)

    def test_all_key(self):
        results = ["key1","key2","key3","key4","key5", "key6","key7","key8","key9","key 10"]
        obj = SolutionOne(self.data)
        executed_results = obj.get_results()
        self.assertTrue(self.match_all_keys(results, executed_results))



class TestProblemTwo(unittest.TestCase):
    def setUp(self) -> None:
        self.data = {
            "key1": 1,
            "key2": {
                "key3": 1,
                "key4": {
                    "key5": 4,
                    "user": Person("two-first", "two-last", Person("one-first", "one-last", None))
                },
                "key6": Person("one-first", "one-last", None),
                "key7": [1, 2, 3],
                "key8": {
                    "key9": "string",
                    "key 10": Person("three-first", "three-last", Person("two-first", "two-last", Person("one-first", "one-last", None)))
                },
            }
        }
        return super().setUp()

    def match_all_keys(self, x, y):
        if len(x) != len(y):
            return False
        for value in y:
            value = " ".join(value.split()[:-1])
            if value not in x:
                return False
        return True

    def test_output(self):
        results = [
            "key1 1","key2 1","key3 2","key4 2","key5 3", "user 3",
            "first_name 4", "last_name 4", "father 4", "first_name 5",
            "last_name 5", "father 5", "key6 2", "first_name 3",
            "last_name 3", "father 3", "key7 2","key8 2","key9 3",
            "key 10 3", "first_name 4", "last_name 4", "father 4",
            "first_name 5", "last_name 5", "father 5",
            "first_name 6", "last_name 6", "father 6"
        ]
        obj = SolutionTwo(self.data)
        executed_results = obj.get_results()
        self.assertEqual(results, executed_results)

    def test_all_key(self):
        results = [
            "key1","key2","key3","key4","key5", "user",
            "first_name", "last_name", "father", "first_name",
            "last_name", "father", "key6", "first_name",
            "last_name", "father", "key7","key8","key9",
            "key 10", "first_name", "last_name", "father",
            "first_name", "last_name", "father",
            "first_name", "last_name", "father"
        ]
        obj = SolutionTwo(self.data)
        executed_results = obj.get_results()
        self.assertTrue(self.match_all_keys(results, executed_results))
