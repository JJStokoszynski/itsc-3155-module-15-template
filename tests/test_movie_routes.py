from flask.testing import FlaskClient

from src.models import Movie
from tests.utils import create_movie, refresh_db


def test_get_all_movies_empty(test_app: FlaskClient):
    refresh_db()

    res = test_app.get('/movies')
    page_data: str = res.data.decode()

    assert res.status_code == 200
    assert '<td>' not in page_data
