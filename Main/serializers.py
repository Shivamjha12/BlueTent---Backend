from rest_framework import serializers
from .models import *

class DestinationPlannerAdd(serializers.ModelSerializer):
    destination = serializers.CharField(source="destination.name")
    class Meta:
        model = destinationPlanner
        fields = ['title','destination','postid','budget','no_of_people','no_of_days','purpose_of_visit','date_of_visit','description','likes']

class destionationSerializer(serializers.Serializer):
    class Meta:
        model = destination
        fields = ['__all__']