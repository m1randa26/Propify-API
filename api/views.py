from django.shortcuts import render
from rest_framework import viewsets 
from rest_framework.renderers import JSONRenderer
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
    renderer_classes = [JSONRenderer]
    
class PropertyViewSet(viewsets.ModelViewSet):
    
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    renderer_classes = [JSONRenderer]
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    
class RentalHistoryViewSet(viewsets.ModelViewSet):
    
    queryset = RentalHistory.objects.all()    
    serializer_class = RentalHistorySerializer
    renderer_classes = [JSONRenderer]