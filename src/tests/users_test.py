import unittest
import services.users as users


class TestUsers(unittest.TestCase):
    def setUp(self):
        users.delete_all()
        
        
    def test_register(self):
        users.register('tunnus', 'salasana123')
        all = users.find_all()
        
        self.assertEqual(len(all), 1)
        self.assertEqual(all[0].username, 'tunnus')
        
        
    def test_register_multiple(self):
        users.register('tunnus1', 'salasana123')
        users.register('tunnus2', 'salasana123')
        users.register('tunnus3', 'salasana123')
        
        all = users.find_all()
        
        self.assertEqual(len(all), 3)
        self.assertEqual(all[0].username, 'tunnus1')
        
    
    def test_delete_all(self):
        users.register('tunnus1', 'salasana123')
        users.register('tunnus2', 'salasana123')
        users.delete_all()
        
        all = users.find_all()
        
        self.assertEqual(len(all), 0)
        

        
    
    