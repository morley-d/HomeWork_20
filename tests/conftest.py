import pytest
from unittest.mock import MagicMock

from dao.director import DirectorDAO
from dao.genre import GenreDAO
from dao.model.director import Director
from dao.model.genre import Genre
from dao.model.movie import Movie
from dao.movie import MovieDAO


@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(None)

    dir1 = Director(id=1, name="Joe")
    dir2 = Director(id=2, name="Losy")
    dir3 = Director(id=3, name="Tony")
    dir4 = Director(id=4, name="Pony")

    director_dao.get_one = MagicMock(return_value=dir1)
    director_dao.get_all = MagicMock(return_value=[dir1, dir2, dir3])
    director_dao.create = MagicMock(return_value=dir4)
    director_dao.delete = MagicMock(return_value="")
    director_dao.update = MagicMock(return_value="")

    return director_dao


@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(None)

    genre1 = Genre(id=1, name="Drama")
    genre2 = Genre(id=2, name="Comedy")
    genre3 = Genre(id=3, name="Horror")

    genre_dao.get_one = MagicMock(return_value=genre1)
    genre_dao.get_all = MagicMock(return_value=[genre1, genre2])
    genre_dao.create = MagicMock(return_value=genre3)
    genre_dao.delete = MagicMock(return_value="")
    genre_dao.update = MagicMock(return_value="")

    return genre_dao


@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(None)

    mov1 = Movie(id=1, title="2012", description="Cool", year=2011, trailer="pouiiwerer", genre_id=2, director_id=1)
    mov2 = Movie(id=2, title="Troya", description="Kall", year=2005, rating=9)
    mov3 = Movie(id=3, title="Limitless", description="Gol", year=2008, trailer="ergreg")

    movie_dao.get_one = MagicMock(return_value=mov1)
    movie_dao.get_all = MagicMock(return_value=[mov1, mov2])
    movie_dao.create = MagicMock(return_value=mov3)
    movie_dao.delete = MagicMock(return_value="")
    movie_dao.update = MagicMock(return_value="")

    return movie_dao
