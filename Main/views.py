from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import *
from .models import *
from Accounts.models import *
import jwt,datetime
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import viewsets
from django.http import JsonResponse

class UserDestinationPlannerViewset(viewsets.ViewSet):
    def addDestionPlanner(self,request):
        dest= request.data.get('destination')
        user = request.data.get('user')
        title = request.data.get('title')
        description = request.data.get('description')
        budget = request.data.get('budget')
        no_of_people = request.data.get('no_of_people')
        no_of_days = request.data.get('no_of_days')
        purpose_of_visit = request.data.get('purpose_of_visit')
        date_of_visit = request.data.get('date_of_visit')

        #user 
        print(dest,user,title,description,budget,no_of_people,no_of_days,purpose_of_visit,date_of_visit, "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        user = User.objects.filter(email=user).first()
        currentDestination = destination.objects.filter(name=dest).first()
        # creating the podcast object for user
        destinationPlanner.objects.create(user=user, destination=currentDestination,title=title, description=description,budget=budget,no_of_people=no_of_people,no_of_days=no_of_days,purpose_of_visit=purpose_of_visit,date_of_visit=date_of_visit)
        print(user, title, " ",description, purpose_of_visit, budget, date_of_visit)

        return Response(status=201)
        
    def updateDestinationPlanner(self,request,pk):
        print(" =========  ",request.data)
        data = request.data
        plan = destinationPlanner.objects.get(postid=pk)
        if plan:
            plan.title = data['title']
            plan.description = data['description']
            plan.save()
            return Response(status=201,data={'message': 'Podcast updated successfully'})
        else:
            return Response({'message': 'Podcast not found'})
    
    def getDestinations(self,request):
        destinations = destination.objects.values_list('name', flat=True)
        return JsonResponse({'destinations': list(destinations)})
    
    def getDestionationPlanner(self,request,postid):
        post = destinationPlanner.objects.filter(postid=postid).first()
        serializer = DestinationPlannerAdd(post)
        return Response(serializer.data)
    
    def getUserPlans(self,request,userid):
        user = User.objects.filter(email=userid).first()
        plans = destinationPlanner.objects.filter(user=user)
        serializer = DestinationPlannerAdd(plans,many=True)
        return Response(serializer.data)
    
class planList(generics.ListCreateAPIView):
    search_fields = ['title','description','destination.name']
    filter_backends = (filters.SearchFilter,)
    queryset = destinationPlanner.objects.all()
    serializer_class = DestinationPlannerAdd