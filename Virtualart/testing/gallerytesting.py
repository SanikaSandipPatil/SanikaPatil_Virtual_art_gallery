import unittest
from unittest.mock import MagicMock
from dao.crime_analysis_service_impl import CrimeAnalysisServiceImpl
from entity.Gallery import Gallery

class TestGalleryManagement(unittest.TestCase):
    def setUp(self):
        self.crime_analysis_service = CrimeAnalysisServiceImpl()

    def test_create_gallery_success(self):
        # Mocking the DB connection and cursor
        self.crime_analysis_service.connection = MagicMock()
        cursor_mock = self.crime_analysis_service.connection.cursor.return_value
        cursor_mock.execute.return_value = None

        gallery = Gallery(name="Test Gallery", description="Test Description", location="Test Location",
                          curator="Test Curator", opening_hours="Test Opening Hours")

        result = self.crime_analysis_service.add_gallery(gallery)

        self.assertTrue(result)
        cursor_mock.execute.assert_called_once()

    def test_create_gallery_failure(self):
        # Mocking the DB connection and cursor
        self.crime_analysis_service.connection = MagicMock()
        cursor_mock = self.crime_analysis_service.connection.cursor.return_value
        cursor_mock.execute.side_effect = Exception("Mocked DB Error")

        gallery = Gallery(name="Test Gallery", description="Test Description", location="Test Location",
                          curator="Test Curator", opening_hours="Test Opening Hours")

        result = self.crime_analysis_service.add_gallery(gallery)

        self.assertFalse(result)
        cursor_mock.execute.assert_called_once()

    def test_update_gallery_success(self):
        # Mocking the DB connection and cursor
        self.crime_analysis_service.connection = MagicMock()
        cursor_mock = self.crime_analysis_service.connection.cursor.return_value
        cursor_mock.execute.return_value = None

        gallery_id = 1  # Assuming gallery with ID 1 exists
        updated_gallery = Gallery(gallery_id=gallery_id, name="Updated Gallery", description="Updated Description",
                                  location="Updated Location", curator="Updated Curator",
                                  opening_hours="Updated Opening Hours")

        result = self.crime_analysis_service.update_gallery(updated_gallery)

        self.assertTrue(result)
        cursor_mock.execute.assert_called_once()

    def test_update_gallery_failure(self):
        # Mocking the DB connection and cursor
        self.crime_analysis_service.connection = MagicMock()
        cursor_mock = self.crime_analysis_service.connection.cursor.return_value
        cursor_mock.execute.side_effect = Exception("Mocked DB Error")

        gallery_id = 1  # Assuming gallery with ID 1 exists
        updated_gallery = Gallery(gallery_id=gallery_id, name="Updated Gallery", description="Updated Description",
                                  location="Updated Location", curator="Updated Curator",
                                  opening_hours="Updated Opening Hours")

        result = self.crime_analysis_service.update_gallery(updated_gallery)

        self.assertFalse(result)
        cursor_mock.execute.assert_called_once()

    def test_remove_gallery_success(self):
        # Mocking the DB connection and cursor
        self.crime_analysis_service.connection = MagicMock()
        cursor_mock = self.crime_analysis_service.connection.cursor.return_value
        cursor_mock.execute.return_value = None

        gallery_id = 1  # Assuming gallery with ID 1 exists

        result = self.crime_analysis_service.delete_gallery(gallery_id)

        self.assertTrue(result)
        cursor_mock.execute.assert_called_once()

    def test_remove_gallery_failure(self):
        # Mocking the DB connection and cursor
        self.crime_analysis_service.connection = MagicMock()
        cursor_mock = self.crime_analysis_service.connection.cursor.return_value
        cursor_mock.execute.side_effect = Exception("Mocked DB Error")

        gallery_id = 1  # Assuming gallery with ID 1 exists

        result = self.crime_analysis_service.delete_gallery(gallery_id)

        self.assertFalse(result)
        cursor_mock.execute.assert_called_once()

    def test_search_galleries_success(self):
        # Mocking cursor and execute method
        self.crime_analysis_service.connection.cursor().execute = MagicMock()
        # Mocking fetchall method to return sample data
        self.crime_analysis_service.connection.cursor().fetchall = MagicMock(return_value=[
            {'gallery_id': 1, 'name': 'Gallery 1', 'description': 'Description 1', 'location': 'Location 1',
             'curator': 'Curator 1', 'opening_hours': '9am - 5pm'},
            {'gallery_id': 2, 'name': 'Gallery 2', 'description': 'Description 2', 'location': 'Location 2',
             'curator': 'Curator 2', 'opening_hours': '10am - 6pm'}
        ])
        search_term = "Gallery"
        galleries = self.crime_analysis_service.search_galleries(search_term)
        # Assert that the search results contain expected gallery data
        self.assertEqual(len(galleries), 2)
        self.assertEqual(galleries[0]['name'], 'Gallery 1')
        self.assertEqual(galleries[1]['name'], 'Gallery 2')


if __name__ == '__main__':
    unittest.main()
