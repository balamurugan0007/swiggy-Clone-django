from django.db import models

# Create your models here.


class foodCatogory(models.Model):
    name = models.CharField(max_length=200,null=False,blank=False)
    cat_image = models.ImageField(upload_to='static/images/cat',blank=False,null=False)
    food_img = models.CharField(max_length=1000)
    created_at =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class hotel(models.Model):
    name = models.CharField(max_length=200,null=False,blank=False)
    created_at =models.DateTimeField(auto_now_add=True)
    Address = models.TextField()
    rating =models.FloatField()
    city = models.CharField(max_length=200,null=False,blank=False)
    hotel_image = models.ImageField(upload_to='static/images/hotels' , default="")
    # second_image= models.ImageField(upload_to='static', default="" )

    def __str__(self) -> str:
        return self.name
    
  

class food(models.Model):
    name = models.CharField(max_length=200,null=False,blank=False)
    created_at =models.DateTimeField(auto_now_add=True)
    catogory = models.ForeignKey(foodCatogory ,on_delete=models.CASCADE)
    hotel_name =models.ForeignKey(hotel,on_delete=models.CASCADE)
    food_img = models.ImageField(upload_to='static/images/food',blank=False,null=False)
    food_link = models.CharField(max_length=1000)
    most_of =models.BooleanField(default=False,help_text='0-default ,1-show')
    rating =models.FloatField()
    combo=models.BooleanField(default=False,help_text='0-default ,1-show')
    







