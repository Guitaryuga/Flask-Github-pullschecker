import pytest
from webapp import create_app
from webapp.datacollect import CollectingData

@pytest.fixture
def test_client(scope='module'):
    flask_app = create_app()
    with flask_app.test_client() as testing_client:
        with flask_app.app_context():
            yield testing_client
