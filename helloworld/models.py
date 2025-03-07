from django.db import models

# Create your models here.
from viewflow import jsonstore
from viewflow.workflow.models import Process


class HelloWorldProcess(Process):
    text = jsonstore.CharField(max_length=150)
    approved = jsonstore.BooleanField(default=False)

    class Meta:
        proxy = True
