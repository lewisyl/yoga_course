from __future__ import unicode_literals
from django.db import models
from apps.login_reg.models import User
import re

class ClassManager(models.Manager):
    def class_validator(self, postData):
        errors = {}
        if len(postData['class_name']) < 2:  
            errors["class_name"] = "Class name should be at least 2 characters"
        if len(postData['description']) < 2:
            errors["description"] = "Description should be at least 2 characters"
        if len(postData['locations']) < 8:
            errors["locations"] = "Location should be at least 8 characters"
        if postData['birthday'] == '':
            errors["birthday"] = "Please enter your Birthday"
        return errors 
class MessageManager(models.Manager):
    def message_validator(self, postData):
        errors = {}
        if postData['message'] == '':
            errors["message"] = "message should not be empty"
        return errors 
class CommentManager(models.Manager):
    def Comment_validator(self, postData):
        errors = {}
        if postData['comment'] == '':
            errors["comment"] = "Comment should not be empty"
        return errors 

class Class(models.Model):
    class_name=models.CharField(max_length=255)
    description=models.TextField()
    locations=models.CharField(max_length=255)
    start_at=models.DateTimeField()
    end_at=models.DateTimeField()
    trainner = models.ForeignKey(User,related_name='I_teach_this_class',on_delete=models.CASCADE)#在django2.0后，定义外键和一对一关系的时候需要加on_delete选项，此参数为了避免两个表里的数据不一致问题，不然会报错
    student = models.ManyToManyField(User,related_name='i_joined_these_classes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ClassManager()    # add this line!

class Message(models.Model):
    message=models.TextField()
    user=models.ForeignKey(User,related_name="user_message",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = MessageManager()    # add this line!


class Comment(models.Model):
    comment=models.TextField()
    user_com=models.ForeignKey(User,related_name='usercomment',on_delete=models.CASCADE)
    msg_com=models.ForeignKey(Message,related_name='messcomment',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CommentManager()    # add this line!


