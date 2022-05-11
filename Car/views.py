from django.http import HttpResponse
from .models import Car
from .serializers import CarSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from django.db.models import Q


class CarAPIView(APIView):
    #auth_classes = [SessionAuthentication,BasicAuthentication]
    auth_classes = (TokenAuthentication,)
    permission_calss = (IsAuthenticated,)
    def get(self,request):
        cars = Car.objects.all()
        serializer = CarSerializer(cars,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = CarSerializer(data = request.data)        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class CarDetails(APIView):
    auth_classes = (TokenAuthentication,)
    permission_calss = (IsAuthenticated,)
    
    def get_object(self,id):
 
        try:
            return Car.objects.get(id=id)
        except car.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    def get(self,request,id):
        car = self.get_object(id)
        serializer = CarSerializer(car)
        return Response(serializer.data)


    def put(self,request,id):
        car = self.get_object(id)
        serializer = CarSerializer(car,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request , id ):
        car = self.get_object(id)
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CarFilterList(generics.ListAPIView):
    serializer_class = CarSerializer

    def get_queryset(self):
        queryset = Car.objects.all()
        carMake = self.request.query_params.get('carMake')
        carModel = self.request.query_params.get('carModel')
        carMileage = self.request.query_params.get('carMileage')
        carColor = self.request.query_params.get('carColor')
        print(carColor)
       
        queryset = queryset.filter(
            Q(carMake__icontains=carMake) 
            |  
            Q(carModel__icontains=carModel)

            |
            Q(carMileage=carMileage)

            |

            Q(carColor__icontains=carColor)

            



            
            )

        return queryset



