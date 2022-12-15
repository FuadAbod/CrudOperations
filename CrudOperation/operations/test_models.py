# from django.test import TestCase

# Create your tests here.
from .models import Tutorial
import pytest

@pytest.mark.django_db
def test_tutorial():
    tutorial = Tutorial.objects.create(title='LOTR', description= 'GOOD', published=True)
    assert tutorial.title == 'LOTR'
    assert tutorial.description == 'GOOD'
    assert tutorial.published == True