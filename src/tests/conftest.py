import pytest
from app import create_app

@pytest.fixture(scope="module")
def app():
    """Instance of Main Flask app"""
    return create_app()