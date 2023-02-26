from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_save,post_save

# Create your models here.

class Project(models.Model):
    project_name=models.CharField(max_length=50)
    
    user=models.ForeignKey(User, default='',on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.project_name

class Client(models.Model):
    client_name=models.CharField(max_length=50)
    created_by=models.ForeignKey(User,on_delete=models.CASCADE)
    project_name=models.ManyToManyField(Project)

    def __str__(self) -> str:
        return self.client_name
    
    
class ClientP(models.Model):
    client_name=models.ForeignKey(Client, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    project_name=models.ForeignKey(Project, on_delete=models.CASCADE)
   
# @receiver(pre_save, sender=Client)
# def correct_price(sender, **kwargs):
#     name= kwargs['instance']
#     project_name=Project.objects.get(id=name)
#     client=Client.objects.get(id=project_name)
#     client.save()    