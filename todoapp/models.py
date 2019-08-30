from django.db import models
from django.core.validators import RegexValidator
from django import forms

class Todo(models.Model):
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
    
    title=models.CharField(max_length=40, default="Unknown")
    text=models.TextField()
    link_code=models.CharField(max_length=8,unique=True, validators=[alphanumeric])
    langs=[('c','C'),('cpp','CPP'),('py','Python')]
    lang=models.CharField(max_length=10, choices=langs, default='c')
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.link_code+" : "+self.text[:20]

