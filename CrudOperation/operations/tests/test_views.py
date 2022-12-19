from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework.parsers import JSONParser 
import pytest
import json 
from .conftest import create_api_connection,create_dummy_data, mock_sqlite_database

@pytest.mark.django_db
def test_request_type_on_tutorial_list(create_api_connection):
    get_request = create_api_connection.get('/api/tutorials')
    post_request = create_api_connection.post('/api/tutorials')
    delete_request = create_api_connection.delete('/api/tutorials')
    assert get_request.status_code == 302
    assert post_request.status_code == 201 or 400
    assert delete_request.status_code == 204

@pytest.mark.django_db
def test_get_request_to_tutorial_list_return_empty_data(create_api_connection, create_dummy_data):
    get_request = create_api_connection.get('/api/tutorials')
    assert get_request.json() == []
    
# @pytest.mark.django_db
# def test_post_request_to_tutorial_list_saves_data(create_dummy_data):
#     print(post_request.context)
    
#     assert get_request.json() == []

