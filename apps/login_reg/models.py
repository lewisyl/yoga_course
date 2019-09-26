from __future__ import unicode_literals
from django.db import models
from dateutil import parser
import datetime
import re

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['firstname']) < 2:  
            errors["firstname"] = "User firstname should be at least 2 characters"
        if len(postData['lastname']) < 2:
            errors["lastname"] = "User lastname should be at least 2 characters"
        if len(postData['password']) < 8:
            errors["password"] = "register password should be at least 8 characters"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address!"
        if postData['password'] != postData['confirm'] :
            errors['confirm'] = 'password needs to be match!'
        if postData['birthday'] == '':
            errors["birthday"] = "Birthday should not be empty"
        else: 
            if parser.parse(postData["birthday"]).date() >= datetime.date.today():
                errors["birthday"] = "Birthday should be in the past" 
            if (datetime.date.today() - parser.parse(postData["birthday"]).date()).days < (18 * 366):
                errors["birthday"] = "Children under the age of 18 must be accompanied by parents."
        return errors 
    def login_validator(self,postData):
        errors={}
        if not User.objects.filter(email=postData['login_email']) and postData['login_pw'] != User.objects.filter(password=postData['login_pw']) :
            errors['login_pw'] = 'Please try again!'
        return errors
    def update_validator(self, postData):
        errors = {}
        if len(postData['update_first']) < 2:  
            errors["update_first"] = "User firstname should be at least 2 characters"
        if len(postData['lastname']) < 2:
            errors["lastname"] = "User lastname should be at least 2 characters"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address!"
        return errors 

class User(models.Model):
    first_name=models.CharField(max_length=45)
    last_name=models.CharField(max_length=45)
    email=models.CharField(max_length=45)
    password=models.CharField(max_length=45)
    birthday = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()    # add this line!