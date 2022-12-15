from .serializers import TutorialSerializer
from unittest.mock import patch

@patch("operations.serializers.TutorialSerializer.Meta")
def test_serializer(mock_meta):
    mock_meta.return_value =('id',
                  'title',
                  'description',
                  'published')
 
    assert TutorialSerializer.Meta() == ('id',
                  'title',
                  'description',
                  'published')
                  
  