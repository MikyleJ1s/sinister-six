import calculate_age

'''
def test_get_age():
    year, month, day = map(int, '1999/02/21'.split(""))
    age = calculate_age.get_age(year, month, day)
    assert age == 24
'''
    
def test_get_age():
    yyyy,mm,dd=1999,2,21
    age=calculate_age.get_age(yyyy,mm,dd)
    assert age==23
    
'''
# using unit testing ... 
import calculate_age # The code to test
import unittest # The test framework
class Test_GetAge(unittest.TestCase):
    def test_calculate_age(self):
        self.assertEqual(calculate_age.get_age(2020,6,11), 2)
if __name__ == '__main__':
    unittest.main()
'''