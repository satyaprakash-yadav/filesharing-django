from django.db import models
import uuid
import os

# Before creating file model configure media directory
# Create your models here.

# step 1 :-
class FolderModel(models.Model):    # 
    uid = models.UUIDField(primary_key=True , editable= False , default=uuid.uuid4)
    created_at = models.DateField(auto_now= True)

# step 3 :-
def get_upload_path(instance , filename):
    return os.path.join('ShareFiles/'+str(instance.folder.uid) , filename)

# step 2 :-
class FilesModel(models.Model):
    folder = models.ForeignKey(FolderModel , on_delete=models.CASCADE)
    file = models.FileField(upload_to=get_upload_path)
    created_at = models.DateField(auto_now=True)


 

