from django.db import models
import uuid
from django.core.validators import MinValueValidator, MaxValueValidator
from Accounts.models import *
# Create your models here.

# I used bulk_create model class method for feeding basic data in the destination model
class destination(models.Model):
    name = models.CharField(max_length=100,unique=True, db_index=True)
    description = models.TextField()
    longitude = models.FloatField(max_length=100)
    latitude = models.FloatField(max_length=100)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    rating = models.IntegerField(default=0,
        validators=[
            MinValueValidator(1, message='Value must be greater than or equal to 1.'),
            MaxValueValidator(5, message='Value must be less than or equal to 5.')
        ]
    )
    avg_rating = models.FloatField(default=0,
        validators=[
            MinValueValidator(1,),MaxValueValidator(5,)
        ]
    )
    
    def __str__(self):
        return self.name

purpose_of_visit= (
    ("Bussiness","BUSSINESS"),
    ("Explore","EXPLORE"),
    ("Holidays","HOLIDAYS"),
    ("Religious Tour","RELIGIOUS TOUR"),
    ("Personal Work","PERSONAL WORK")
    
)

class destinationPlanner(models.Model):
    destination = models.ForeignKey(destination,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE,default="")
    title = models.CharField(max_length=100,default="")
    postid = models.UUIDField(default=uuid.uuid4, editable=True)
    budget = models.FloatField(default=0)
    no_of_people = models.IntegerField(default=0)
    no_of_days = models.IntegerField(default=0)
    purpose_of_visit  = models.CharField(max_length=100,default="",blank=True,choices=purpose_of_visit)
    description = models.TextField()
    date_of_visit = models.DateField()
    likes = models.IntegerField(default=0)
    visitCompleted = models.BooleanField(default=False)
    MoneySpent = models.IntegerField(default=0)
    tips = models.CharField(max_length=500,default=" ",null=True, blank=True)
    
    def __str__(self):
        return self.title
    
class Favorite_plan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plan = models.ForeignKey(destinationPlanner, on_delete=models.CASCADE)
    is_favorite = models.BooleanField(default=False)
    class Meta:
        unique_together = ('user', 'plan',)  
    
    
    
    
    