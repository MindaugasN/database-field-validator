import unittest

from model.fields.integer import IntegerField


def run_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    runner = unittest.TextTestResult(verbosity=2)
    result = runner.run(suite)


class TestIntegerField(unittest.TestCase):
    @staticmethod
    def create_test_class(min_, max_):
        obj = type('TestClass', (), {'age': IntegerField(min_, max_)})
        return obj()

    def test_set_age_ok(self):
        """Tests that valid valued can be assigned/retrieved"""
        min_ = 5
        max_ = 10
        obj = self.create_test_class(min_, max_)
        
        valid_values = range(min_, max_ + 1)

        obj.age = 5
        for i, value in enumerate(valid_values):
            with self.subTest(test_number=i):
                obj.age = value
                self.assertEqual(value, obj.age)

    def test_set_age_invalid(self):
        """Tests that invalid values raise ValueError exceptions"""
        min_ = 10
        max_ = 10
        obj = self.create_test_class(min_, max_)
        
        bad_values = list(range(min_ - 5, min_))
        bad_values += list(range(max_ + 1, max_))
        bad_values += [10.5, 1 + 0j, 'abc', (1, 2)]

        for i, value in enumerate(bad_values):
            with self.subTest(test_number=i):
                with self.assertRaises(ValueError):
                    obj.age = value

    def test_class_get(self):
        """Tests that class attribute retrieval returns the descriptor instance"""
        obj = self.create_test_class(0, 0)
        obj_class = type(obj)
        self.assertIsInstance(obj_class.age, IntegerField)

if __name__ == '__main__':
    run_tests(TestIntegerField)