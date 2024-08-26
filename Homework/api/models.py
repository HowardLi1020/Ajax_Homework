from django.db import models

# Create your models here.

class myMember(models.Model):
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField()
    user_password = models.CharField(max_length=100)
    user_age = models.IntegerField(null=True, blank=True)
    user_avatar = models.ImageField(upload_to='uploads/', null=True, blank=True)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'member'