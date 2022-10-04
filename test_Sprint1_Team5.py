from contextlib import nullcontext
import unittest
import Sprint1_Team5



Dictionary={}
Dictionary[0] = {'ID': 0, 'Name': '', 'Gender': '',
                                                            'Birthday': '', 'Age': 151, 'Alive': 'True', 'Death': 'NA',
                                                            'Child' : 'NA', 'Spouse': 'NA'}
Dictionary[1] = {'ID': 1, 'Name': '', 'Gender': '',
                                                            'Birthday': '', 'Age': -1, 'Alive': 'True', 'Death': 'NA',
                                                            'Child' : 'NA', 'Spouse': 'NA'}
Dictionary[2] = {'ID': 2, 'Name': '', 'Gender': '',
                                                            'Birthday': '', 'Age': 1.34, 'Alive': 'True', 'Death': 'NA',
                                                            'Child' : 'NA', 'Spouse': 'NA'}
Dictionary[3] = {'ID': 3, 'Name': '', 'Gender': '',
                                                            'Birthday': '', 'Age': -3, 'Alive': 'True', 'Death': 'NA',
                                                            'Child' : 'NA', 'Spouse': 'NA'}  
Dictionary[4] = {'ID': 4, 'Name': '', 'Gender': '',
                                                            'Birthday': '', 'Age': '', 'Alive': 'True', 'Death': 'NA',
                                                            'Child' : 'NA', 'Spouse': 'NA'}
Dictionary[5] = {'ID': 5, 'Name': '', 'Gender': '',
                                                            'Birthday': '1951-10-24', 'Age': '', 'Alive': 'True', 'Death': '1951-09-24',
                                                            'Child' : 'NA', 'Spouse': 'NA'}
Dictionary[6] = {'ID': 6, 'Name': '', 'Gender': '',
                                                            'Birthday': '1922-09-21', 'Age': '', 'Alive': 'True', 'Death': 'NA',
                                                            'Child' : 'NA', 'Spouse': 'NA'}                                                                                                                       
Dictionary[7] = {'ID': 7, 'Name': '', 'Gender': '',
                                                            'Birthday': '1950-11-24', 'Age': '', 'Alive': 'True', 'Death': '1940-11-24',
                                                            'Child' : 'NA', 'Spouse': 'NA'}
Dictionary[8] = {'ID': 8, 'Name': '', 'Gender': '',
                                                            'Birthday': '1948-09-4', 'Age': '', 'Alive': 'True', 'Death': 'NA',
                                                            'Child' : 'NA', 'Spouse': 'NA'}
Dictionary[9] = {'ID': 9, 'Name': '', 'Gender': '',
                                                            'Birthday': '', 'Age': '1985-05-13', 'Alive': 'True', 'Death': 'NA',
                                                            'Child' : 'NA', 'Spouse': 'NA'}        
                                                                                                                             
class userStories1to8Test(unittest.TestCase):
    
    def test_ageLessThan150(self):
        result=Sprint1_Team5.ageLessThan150(0, Dictionary)
        self.assertFalse(result)

    def test_ageNotLessThan0(self):
        result=Sprint1_Team5.ageLessThan150(1,Dictionary)
        self.assertFalse(result)

    def test_ageNotDecimals(self):
        result=Sprint1_Team5.ageLessThan150(2,Dictionary)
        self.assertFalse(result)

    def test_ageNotNegtive(self):
        result=Sprint1_Team5.ageLessThan150(3,Dictionary)
        self.assertFalse(result)

    def test_ageNotEmpty(self):
        result=Sprint1_Team5.ageLessThan150(4,Dictionary)
        self.assertFalse(result)

    def test_birthBeforeDeath(self):
        result=Sprint1_Team5.birthBeforeDeath(5, Dictionary)
        self.assertTrue(result)

    def test_birthBeforeDeath(self):
        result=Sprint1_Team5.birthBeforeDeath(6,Dictionary)
        self.assertFalse(result)

    def test_birthBeforeDeath(self):
        result=Sprint1_Team5.birthBeforeDeath(7,Dictionary)
        self.assertTrue(result)

    def test_birthBeforeDeath(self):
        result=Sprint1_Team5.birthBeforeDeath(8,Dictionary)
        self.assertFalse(result)

    def test_birthBeforeDeath(self):
        result=Sprint1_Team5.birthBeforeDeath(9,Dictionary)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()