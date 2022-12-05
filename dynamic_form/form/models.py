from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

from django.db import models

class IntroductoryQuestionnaire(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    # I remember seeing ads for the following brands this year
    brands_seen = models.TextField()
    
    # I remember using products of the following brands this year
    brands_used = models.TextField()
    
    # I have used these brands at least once in the past
    past_brands_used = models.TextField()
    
    # Have you installed any Ad Blocking software in your browser(s)?
    ad_blocking = models.BooleanField()
    
    # Do you use a Youtube subscription?
    youtube_subscription = models.BooleanField()
    
    # Approximately how much percentage of time do you spend on Youtube mobile vs Youtube web?
    youtube_mobile_vs_web = models.CharField(max_length=100)
    
    # How do you apprise yourself of the latest products and brands? (Multi correct)
    product_awareness = models.TextField()
    
    # How many percentage marks did you score in your 12th standard?
    twelfth_marks = models.FloatField()
    
    # What was your BITSAT rank?
    bitsat_rank = models.IntegerField()
    
    # What is your current GPA?
    gpa = models.FloatField()
    
    # For the following sectors, name top-5 brands and their products that you have used in the past or are currently using:
    # (Name the product even if you don’t know the brand which produced it)
    food_brands = models.TextField()
    automobiles_brands = models.TextField()
    clothing_brands = models.TextField()
    cosmetics_brands = models.TextField()
    electronics_brands = models.TextField()
    telecom_brands = models.TextField()
    healthcare_brands = models.TextField()