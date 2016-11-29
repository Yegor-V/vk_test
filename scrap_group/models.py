from django.db import models


class UserIds(models.Model):
    user_id = models.CharField(max_length=100)


class RequestHistory(models.Model):
    action = models.CharField(max_length=100)
