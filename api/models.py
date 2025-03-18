from django.db import models

# Create your models here.
class Users(models.Model):
    
    # AutoField -> Auto increment value
    user_id = models.AutoField(primary_key=True)