from .models import drinks
from .serializers import django_api_2
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

@api_view(['GET', 'POST'])
def show_values(request):
        drink = drinks.objects.all()
                
        if request.method == 'GET':
                serializers = django_api_2(drink,many=True)
                return Response(serializers.data, status=200)
        if request.method == 'POST':
                serializers = django_api_2(data=request.data)
                if serializers.is_valid():      
                        serializers.save()
                        return Response(serializers.data, status=status.HTTP_201_CREATED)
                else:
                        return Response(serializers.data,status=status.HTTP_304_NOT_MODIFIED)
        
                
                
@api_view(['GET', 'PUT','DELETE'])
def delete_values(request,id):
        drink = drinks.objects.filter(id=id)
                
        if request.method == 'GET':
                serializers = django_api_2(drink,many=True)
                return Response(serializers.data, status=200)
        
        if request.method == 'POST':
                serializers = django_api_2(data=request.data)
                if serializers.is_valid():      
                        serializers.save()
                        return Response(serializers.data, status=status.HTTP_201_CREATED)
                else:
                        return Response(serializers.data,status=status.HTTP_304_NOT_MODIFIED)
                
        if request.method == 'PUT':
                data=request.data
                serializers = django_api_2(data=request.data)
                if serializers.is_valid(): 
                        drink = drinks.objects.get(id=id)
                        drink.id = id    
                        drink.username = data['username']     
                        drink.Age = data['Age']     
                        drink.save()
                        return Response(serializers.data, status=status.HTTP_201_CREATED)
                else:
                        return Response(serializers.data,status=status.HTTP_304_NOT_MODIFIED)     
                           
        if request.method == 'DELETE' :
                drink.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)