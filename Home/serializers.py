import shutil   # use to create zip folder
from rest_framework import serializers  # use to create serializers
from . models import FolderModel,FilesModel # Models

class FileSerializer(serializers.ModelSerializer):  # this class zip single file
    class Meta:
        model = FilesModel # interact with FilesModel
        fields = '__all__'


class FileListSerializer(serializers.Serializer):   # get post request
    # step 1 :-
    folder = serializers.CharField(required = False)# doesn't required because we create automatically

    files = serializers.ListField(child = serializers.FileField(max_length= 100000 , allow_empty_file = False , use_url = False)) # convert multiple file into list and that files obj goes to the class create

    # step 3 :-
    def zip_files(self, folder):
        shutil.make_archive(f'media/zip/{folder}',  'zip' , f'media/ShareFiles/{folder}')
        #                       destiny             type        source

    # step 2 :-
    def create(self, validated_data):
        folder = FolderModel.objects.create()

        files = validated_data.pop('files')
        files_objs = []
        for file in files:
            files_obj = FilesModel.objects.create(folder = folder , file = file)
            files_objs.append(files_obj)

        self.zip_files(folder.uid)

        return {'files' : {} , 'folder' : str(folder.uid)}

        