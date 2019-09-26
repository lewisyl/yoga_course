from __future__ import unicode_literals
from django.db import models
from dateutil import parser
import datetime
import re
import bcrypt

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
        if check_if_email_exist(postData['email']) == True:
            errors['email'] = "Registered email should be unique"
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

    def login_validator(self, postData):
        errors = {}
        user = User.objects.filter(email=postData['login_email'])
        if user:
            logged_user = user[0]
            if not bcrypt.checkpw(postData['login_pw'].encode(), logged_user.password.encode()):
                errors['login_pw'] = "Please try again!"
        else:
            errors['login_email'] = "Please try again!"
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

def check_if_email_exist(email_address):
    all_users = User.objects.all()
    for v in all_users:
        if email_address == v.email:
            return True
    return False