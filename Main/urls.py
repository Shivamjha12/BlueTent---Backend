from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings

# user_podcast = UserPodcast.as_view({'post': 'addPodcast',})
user_plan_add = UserDestinationPlannerViewset.as_view({'post': 'addDestionPlanner',})
user_plan_update = UserDestinationPlannerViewset.as_view({'post': 'updateDestinationPlanner',})

urlpatterns = [
    path("addplan",user_plan_add,name="add_plan"),
    
]