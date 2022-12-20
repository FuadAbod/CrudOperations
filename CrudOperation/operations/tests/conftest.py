from rest_framework.test import APIClient
from django.urls import reverse
import pytest
from ..models import Tutorial
import sqlite3

@pytest.fixture
def create_api_connection():
    client = APIClient()
    return client

@pytest.fixture
def create_sample_data(db):
    first_tutorial = Tutorial(title='LOTR', description= 'sjncs', published = True)
    second_tutorial= Tutorial(title='LOTR', description= 'Film', published = False)
    first_tutorial.save()
    second_tutorial.save()

