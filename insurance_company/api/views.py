from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Policy
from .serializer import PolicySerializer  # Renamed for proper naming convention

@api_view(['GET', 'POST'])
def policy_list_create(request):
    if request.method == 'GET':
        policies = Policy.objects.all()
        serializer = PolicySerializer(policies, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PolicySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def policy_detail(request, pk):
    try:
        policy = Policy.objects.get(pk=pk)
    except Policy.DoesNotExist:
        return Response({"error": "Policy not found"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = PolicySerializer(policy)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = PolicySerializer(policy, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        policy.delete()
        return Response({"message": "Policy deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
