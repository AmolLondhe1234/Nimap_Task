from rest_framework import serializers
from .models import *
from user.serializer import *

class ClientSerializer(serializers.ModelSerializer):
    # created_by=UserSerializer()
    class Meta:
        model = Client
        fields = ('client_name','created_by')
        
        
        
        
        
class ClientPSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientP
        fields = "__all__"
        
        
        
        
        
        
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"                