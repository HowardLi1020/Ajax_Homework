from django.db import models

# Create your models here.
class myMember(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=20)
    user_password = models.CharField(max_length=128)
    user_email = models.CharField(unique=True, max_length=100)
    user_birth = models.DateField()
    user_avator = models.CharField(max_length=50)
    last_update = models.DateTimeField()

    class Meta:
        db_table = 'member'