from rest_framework import serializers
from .models import *

class DestinationPlannerAdd(serializers.ModelSerializer):
    class Meta:
        model = destinationPlanner
        fields = ['title','destination','budget','no_of_people','no_of_days','purpose_of_visit','description','likes','speaker','file']

class destionationSerializer(serializers.Serializer):
    class Meta:
        model = destination
        fields = ['__all__']