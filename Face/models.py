# -*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from django.db import models
import django.utils.timezone as timezone

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    job_type=models.CharField(max_length=100)
    gongjijing_type=models.CharField(max_length=100)
    job_type=models.CharField(max_length=100)
    job_address = models.CharField(max_length=100,default=u'无')
    job_age = models.CharField(max_length=100,default='0')
    salary = models.CharField(max_length=100)
    shebaotime= models.CharField(max_length=100,default='0')
    shebao_type=models.CharField(max_length=100)
    gongjijintime = models.CharField(max_length=100,default='0')
    home_address= models.CharField(max_length=100)
    zhimafen = models.CharField(max_length=100)
    house = models.CharField(max_length=100)
    create_time = models.DateTimeField(default = timezone.now)
    result=models.CharField(max_length=100)
    money=models.CharField(max_length=100)


