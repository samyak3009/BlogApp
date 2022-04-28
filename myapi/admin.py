import imp
from django.contrib import admin
from myapi import models
# Register your models here.


admin.site.register(models.UserProfile)