from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.decorators import api_view
from operations.models import Tutorial
from operations.serializers import TutorialSerializer
from rest_framework.response import Response
# Create your views here.

@api_view(['GET', 'POST', 'DELETE'])
def tutorial_list(request):
    if request.method == 'GET':
        tutorials = Tutorial.objects.all()
        
        title = request.query_params.get('title', None)
        if title is not None:
            tutorials = tutorials.objects.values('title')
        
        tutorials_serializer = TutorialSerializer(tutorials, many=True)
        return Response(tutorials_serializer.data, status=status.HTTP_302_FOUND)

    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorials_serializer = TutorialSerializer(data=tutorial_data)
        if tutorials_serializer.is_valid():
            tutorials_serializer.save()
            return Response(tutorials_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(tutorials_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        total_count = Tutorial.objects.all().delete()
        return Response({'message': '{} Tutorials were deleted successfully!'.format(total_count[0])}, status=status.HTTP_200_OK)
    

@api_view(['GET', 'PUT', 'DELETE'])
def tutorial_detail(request, pk):
    try: 
        tutorial = Tutorial.objects.get(pk=pk) 
    except Tutorial.DoesNotExist: 
        return Response({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 

    if request.method == 'GET':
        tutorial_serializer = TutorialSerializer(tutorial)
        return Response(tutorial_serializer.data)

    elif request.method == 'PUT':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = TutorialSerializer(tutorial, data=tutorial_data) 
        if tutorial_serializer.is_valid(): 
            tutorial_serializer.save() 
            return Response(tutorial_serializer.data, status=status.HTTP_202_ACCEPTED) 
        else:
            return Response(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
    elif request.method == 'DELETE':
        tutorial.delete()
        return Response({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_200_OK)

@api_view(['GET'])
def tutorial_list_published(request):
    tutorials = Tutorial.objects.filter(published=True)
    if request.method == 'GET': 
        tutorials_serializer = TutorialSerializer(tutorials, many=True)
        return Response(tutorials_serializer.data)