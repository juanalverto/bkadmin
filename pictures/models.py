from django.db import models
from users.models import User

# Create your models here.

class Picture(models.Model):
	photo = models.ImageField(upload_to='pictures')
	user = models.ForeignKey(User)
	