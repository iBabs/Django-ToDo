from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class Mytodos(models.Model):
    owner= models.ForeignKey(User, on_delete=models.CASCADE, null= True,)
    task = models.CharField(max_length= 30, null =True)
    details = models.TextField()
    created= models.DateField(auto_now_add=True)
    complete= models.BooleanField(default= False)

    def __str__(self):
        return self.task

    class Meta:
        ordering= [
            "complete"
        ]

    # def get_absolute_url(self):
    #     # return reverse("list")
    
