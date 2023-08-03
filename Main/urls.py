from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings

# user_podcast = UserPodcast.as_view({'post': 'addPodcast',})
user_plan_add = UserDestinationPlannerViewset.as_view({'post': 'addDestionPlanner',})
user_plan_update = UserDestinationPlannerViewset.as_view({'post': 'updateDestinationPlanner',})
get_destination = UserDestinationPlannerViewset.as_view({'get': 'getDestinations',})
get_destinationPlannerPost = UserDestinationPlannerViewset.as_view({'get': 'getDestionationPlanner',})
get_user_plans = UserDestinationPlannerViewset.as_view({'get': 'getUserPlans',})
get_new_plans = UserDestinationPlannerViewset.as_view({'get': 'getNewPlans',})

urlpatterns = [
    path("addplan",user_plan_add,name="add_plan"),
    path('updatePlan/<str:pk>',user_plan_update,name="update_plan"),
    path("destinations",get_destination ,name="destinations"),
    path("destinationPlan/<str:postid>",get_destinationPlannerPost,name="get_destinationPlannerPost"),
    path('plans/<str:userid>',get_user_plans,name="user_plans"),
    path('plans/explore/',planList.as_view(),name="plan_list"),
    path('plans', get_new_plans, name="new_plans")
]