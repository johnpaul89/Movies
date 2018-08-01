import unittest
from models import Movie
# Movie = movie.Movi

class MovieTest(unittest.TestCase):
    """Test class to test the behaviour of the class"""

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_movie = Movie(1234,'Python Must Be Crazy', 'A thrilling new Python Series', 'https://developers.themoviedb.org/3/getting-started/images/khsjha27hbs',8.5,129993)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_movie,Movie))
