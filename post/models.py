from django.db import models
from login.models import User
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User)
    text = models.TextField()
    subject = models.CharField(max_length=20)
    date = models.DateField(timezone.now())
    def __unicode__(self):
    	return self.subject