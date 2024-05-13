import unittest
from unittest.mock import MagicMock
from dao.crime_analysis_service_impl import CrimeAnalysisServiceImpl
from entity.artwork import Artwork

class TestArtworkManagement(unittest.TestCase):
    def setUp(self):
        self.crime_analysis_service = CrimeAnalysisServiceImpl()

    def test_add_artwork_success(self):
        # Mocking the DB connection and cursor
        self.crime_analysis_service.connection = MagicMock()
        cursor_mock = self.crime_analysis_service.connection.cursor.return_value
        cursor_mock.execute.return_value = None

        artwork = Artwork(title="Test Artwork", description="Test Description", creation_date="2024-05-13",
                          medium="Oil on Canvas", image_url="http://example.com/test_artwork.jpg")

        result = self.crime_analysis_service.add_artwork(artwork)

        self.assertTrue(result)
        cursor_mock.execute.assert_called_once()

    def test_add_artwork_failure(self):
        # Mocking the DB connection and cursor
        self.crime_analysis_service.connection = MagicMock()
        cursor_mock = self.crime_analysis_service.connection.cursor.return_value
        cursor_mock.execute.side_effect = Exception("Mocked DB Error")

        artwork = Artwork(title="Test Artwork", description="Test Description", creation_date="2024-05-13",
                          medium="Oil on Canvas", image_url="http://example.com/test_artwork.jpg")

        result = self.crime_analysis_service.add_artwork(artwork)

        self.assertFalse(result)
        cursor_mock.execute.assert_called_once()

    def test_update_artwork_success(self):
        # Mocking the DB connection and cursor
        self.crime_analysis_service.connection = MagicMock()
        cursor_mock = self.crime_analysis_service.connection.cursor.return_value
        cursor_mock.execute.return_value = None

        artwork_id = 1  # Assuming artwork with ID 1 exists
        updated_artwork = Artwork(artwork_id=artwork_id, title="Updated Title", description="Updated Description",
                                  creation_date="2024-05-13", medium="Oil on Canvas",
                                  image_url="http://example.com/updated_artwork.jpg")

        result = self.crime_analysis_service.update_artwork(updated_artwork)

        self.assertTrue(result)
        cursor_mock.execute.assert_called_once()

    def test_update_artwork_failure(self):
        # Mocking the DB connection and cursor
        self.crime_analysis_service.connection = MagicMock()
        cursor_mock = self.crime_analysis_service.connection.cursor.return_value
        cursor_mock.execute.side_effect = Exception("Mocked DB Error")

        artwork_id = 1  # Assuming artwork with ID 1 exists
        updated_artwork = Artwork(artwork_id=artwork_id, title="Updated Title", description="Updated Description",
                                  creation_date="2024-05-13", medium="Oil on Canvas",
                                  image_url="http://example.com/updated_artwork.jpg")

        result = self.crime_analysis_service.update_artwork(updated_artwork)

        self.assertFalse(result)
        cursor_mock.execute.assert_called_once()

    def test_remove_artwork_success(self):
        # Mocking the DB connection and cursor
        self.crime_analysis_service.connection = MagicMock()
        cursor_mock = self.crime_analysis_service.connection.cursor.return_value
        cursor_mock.execute.return_value = None

        artwork_id = 1  # Assuming artwork with ID 1 exists

        result = self.crime_analysis_service.delete_artwork(artwork_id)

        self.assertTrue(result)
        cursor_mock.execute.assert_called_once()

    def test_remove_artwork_failure(self):
        # Mocking the DB connection and cursor
        self.crime_analysis_service.connection = MagicMock()
        cursor_mock = self.crime_analysis_service.connection.cursor.return_value
        cursor_mock.execute.side_effect = Exception("Mocked DB Error")

        artwork_id = 1  # Assuming artwork with ID 1 exists

        result = self.crime_analysis_service.delete_artwork(artwork_id)

        self.assertFalse(result)
        cursor_mock.execute.assert_called_once()

    def test_search_artworks_success(self):
        # Mocking cursor and execute method
        mock_cursor = MagicMock()
        self.crime_analysis_service.connection.cursor = MagicMock(return_value=mock_cursor)

        # Mocking fetchall method to return sample data
        mock_cursor.fetchall.return_value = [
            {'artwork_id': 1, 'Title': 'Artwork 1', 'Description': 'Description 1', 'Creation_date': '2024-05-15',
             'Medium': 'Medium 1', 'Image_url': 'image1.jpg'},
            {'artwork_id': 2, 'Title': 'Artwork 2', 'Description': 'Description 2', 'Creation_date': '2024-05-16',
             'Medium': 'Medium 2', 'Image_url': 'image2.jpg'}
        ]

        search_term = "Artwork"
        artworks = self.crime_analysis_service.search_artworks(search_term)

        # Assert that the search results contain expected artwork data
        self.assertEqual(len(artworks), 2)
        self.assertEqual(artworks[0].get_title(), 'Artwork 1')
        self.assertEqual(artworks[1].get_title(), 'Artwork 2')

        # Print the retrieved artworks for verification
        print("Retrieved Artworks:")
        for artwork in artworks:
            print(artwork)

if __name__ == '__main__':
    unittest.main()
