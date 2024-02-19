from django.contrib import admin
from .models import FilesModel,FolderModel

# Register your models here.
@admin.register(FolderModel)
class FolderAdmin(admin.ModelAdmin):
    list_display = ['uid','created_at']

@admin.register(FilesModel)
class FilesAdmin(admin.ModelAdmin):
    list_display = ['id','folder','file','created_at']

