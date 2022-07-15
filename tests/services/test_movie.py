"""Тестирование MovieService"""

import pytest

from service.movie import MovieService


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)
        assert movie is not None
        assert isinstance(movie.id, int)
        assert movie.title == "2012"
        assert movie.description == "Cool"
        assert movie.year == 2011
        assert movie.trailer == "pouiiwerer"
        assert movie.rating == None
        assert movie.genre_id == 2
        assert movie.director_id == 1

    def test_get_all(self):
        movies = self.movie_service.get_all()
        assert len(movies) == 2

    def test_create(self):
        new_movie = self.movie_service.create(None)
        assert new_movie.id is not None
        assert new_movie.title == "Limitless"
        assert new_movie.description == "Gol"
        assert new_movie.year == 2008
        assert new_movie.trailer == "ergreg"
        assert new_movie.rating == None
        assert new_movie.genre_id == None
        assert new_movie.director_id == None

    def test_update(self):
        res = self.movie_service.update(1)
        assert res == ""

    def test_delete(self):
        res = self.movie_service.delete(1)
        assert res is None
