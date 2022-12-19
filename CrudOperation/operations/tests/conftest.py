from rest_framework.test import APIClient
from django.urls import reverse
import pytest
from ..models import Tutorial

@pytest.fixture
def create_api_connection():
    client = APIClient()
    return client


@pytest.fixture
def create_dummy_data(create_api_connection):
    data = {
        "title": "Python&ReACT",
        "description": "OOP",
        "published": True
    }
    respone = create_api_connection.post(reverse('tutorial_list'),data=data, format='json')
    return respone.json()

@pytest.fixture
def mock_sqlite_database():
    Tutorial.create
    mock_model= Tutorial(
        title="XXX",
        description = "YYY",
        published = True
    )
    return mock_model
