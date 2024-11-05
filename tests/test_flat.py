import unittest
from models.flat import Flat
from repositories.flat_repository import FlatRepository

class TestFlatRepository(unittest.TestCase):
    def setUp(self):
        self.repo = FlatRepository('test_flats.json')
        # Ensure the repository is empty before each test
        self.repo.flats = []
        self.repo.save()

    def tearDown(self):
        # Clean up the test file after each test
        import os
        if os.path.exists('test_flats.json'):
            os.remove('test_flats.json')

    def test_add_flat(self):
        flat = Flat(flat_number=101, floor=1, room_type='1-room')
        self.repo.add_flat(flat)
        self.assertIn(flat, self.repo.flats)

    def test_delete_flat(self):
        flat = Flat(flat_number=101, floor=1, room_type='1-room')
        self.repo.add_flat(flat)
        result = self.repo.delete_flat(101)
        self.assertTrue(result)
        self.assertNotIn(flat, self.repo.flats)

    def test_get_flat_by_number(self):
        flat = Flat(flat_number=101, floor=1, room_type='1-room')
        self.repo.add_flat(flat)
        fetched = self.repo.get_flat_by_number(101)
        self.assertEqual(fetched, flat)

if __name__ == '__main__':
    unittest.main()
