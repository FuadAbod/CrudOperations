from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework.parsers import JSONParser 
import pytest
import json 
from ..models import Tutorial
from .conftest import create_api_connection,create_sample_data

@pytest.mark.django_db
def test_request_method(create_api_connection):
    get_request = create_api_connection.get('/api/tutorials')
    post_request = create_api_connection.post('/api/tutorials')
    delete_request = create_api_connection.delete('/api/tutorials')
    assert get_request.status_code == 302
    assert post_request.status_code == 201 or 400
    assert delete_request.status_code == 200

@pytest.mark.django_db
def test_get_request_to_tutorial_list_return_empty_data(create_api_connection):
    get_request = create_api_connection.get('/api/tutorials')
    assert get_request.json() == []
    

@pytest.mark.django_db
def test_get_request_for_data(create_api_connection, create_sample_data):
    get_request = create_api_connection.get('/api/tutorials')
    assert get_request.status_code == 302
    assert get_request.json() == [{'id': 1, 'title': 'LOTR', 'description': 'sjncs', 'published': True}, {'id': 2, 'title': 'LOTR', 'description': 'Film', 'published': False}]

 
def test_post_request(create_api_connection,create_sample_data):
    data = {
        "title": "Python&ReACT",
        "description": "OOOP",
        "published": True
        }
    post_request = create_api_connection.post(reverse('tutorial_list'), data=data, format="json")
    assert post_request.json() == {'id': 3, 'title': 'Python&ReACT', 'description': 'OOOP', 'published': True}
    assert post_request.status_code == 201

def test_delete_request(create_api_connection,create_sample_data):  
    delete_request = create_api_connection.delete('/api/tutorials', format="json")
    assert delete_request.status_code == 200
    assert delete_request.json() == {'message': '2 Tutorials were deleted successfully!'}


def test_get_request_tutorial_detail(create_api_connection,create_sample_data):
    get_request = create_api_connection.get('/api/tutorials/1')
    get_request_with_incorrect_id = create_api_connection.get('/api/tutorials/3')
    assert get_request.status_code == 200
    assert get_request.json() == {'id': 1, 'title': 'LOTR', 'description': 'sjncs', 'published': True}
    assert get_request_with_incorrect_id.status_code == 404
    assert get_request_with_incorrect_id.json() == {'message': 'The tutorial does not exist'}

def test_put_request_tutorial_detail(create_api_connection,create_sample_data):
    new_body= {'title': 'LOTR', 'description': 'sjncs', 'published': False}
    put_request = create_api_connection.put('/api/tutorials/1',data = new_body, format="json")
    assert put_request.status_code == 202
    assert put_request.json() =={'id': 1, 'title': 'LOTR', 'description': 'sjncs', 'published': False}

def test_delete_request_tutorial_detail(create_api_connection,create_sample_data):
    delete_request = create_api_connection.delete('/api/tutorials/1',format="json")
    assert delete_request.status_code == 200
    assert delete_request.json() == {'message': 'Tutorial was deleted successfully!'}

def test_delete_request_tutorial_list_published(create_api_connection,create_sample_data):
    get_request = create_api_connection.get('/api/tutorials/published', format="json")
    assert get_request.json() == [{'id': 1, 'title': 'LOTR', 'description': 'sjncs', 'published': True}]