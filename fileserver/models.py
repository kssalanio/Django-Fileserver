from django.contrib.auth.models import User
from django.db import models
import os

#instance is file model
def get_file_path(instance, filename):
    return os.path.join(str(instance.user.id), filename)

class File(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='files') #file is tied to a user; user can access all files through the column 'files'
    file = models.FileField(upload_to=get_file_path) #file location, django passes in parameters to get file path
