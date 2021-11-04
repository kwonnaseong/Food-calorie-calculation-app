from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=20)
    image = models.ImageField(upload_to='media', null=True)
    # create_at = models.DateTimeField(auto_now=True)
    # 아직 migrate 안함

class Photo(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

class Output(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=20, null=True)
    # 1회 제공량
    One_timesupply = models.FloatField(null=True)
    # 탄단지
    Carbohydrate= models.FloatField(null=True)
    Protein = models.FloatField(null=True)
    Fat = models.FloatField(null=True)
    #당, 칼로리
    sugars = models.FloatField(null=True)
    energy = models.FloatField(null=True)


class total_information(models.Model):
    create_at = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    total_One_timesupply = models.FloatField(null=True)
    total_Carbohydrate = models.FloatField(null=True)
    total_Protein = models.FloatField(null=True)
    total_Fat = models.FloatField(null=True)
    total_sugars = models.FloatField(null=True)
    total_energy = models.FloatField(null=True)

class NutritionFacts(models.Model):
    NO = models.IntegerField()
    SAMPLE_ID = models.IntegerField()
    code = models.CharField(max_length=30)
    DB = models.CharField(max_length=30)
    Foodname1 = models.CharField(max_length=30)
    One_timesupply = models.FloatField()
    energy = models.FloatField()
    Protein = models.FloatField()
    Fat = models.FloatField()
    Carbohydrate= models.FloatField()
    Totalsugars = models.FloatField()
    Foodname2 = models.CharField(max_length=20)

