from django.db import models

class Userinfo(models.Model):
    username = models.CharField(max_length=100,default='')
    email = models.EmailField(primary_key=True, unique=True, default='')
    password = models.CharField(max_length=100, default='')
    confirmpassword = models.CharField(max_length=100, default='')

    class Meta:
        db_table = 'sdp'