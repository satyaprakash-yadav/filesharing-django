from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . models import FilesModel # data exist in FileModels
from .serializers import FileSerializer, FileListSerializer
#                        for get request   for post request
# Create your views here.

def home(request):
    return render(request, 'home/home.html')

def download(request, uid):
    context = {'uid':uid}
    return render(request, 'home/download.html', context)

class HandleFileUpload(APIView):  # interact with api 
    def post(self, request):
        try:
            data = request.data

            serializer = FileListSerializer(data=data)
            if serializer.is_valid():
                serializer.save()   # method call to the create method
                return Response({'message' : 'upload successfully', 'data' : serializer.data})

            return Response({'message' : 'something went wrong','data':serializer.errors})
        except Exception as e:
            print(e)

        

    def get(self, request):
        data = FilesModel.objects.all()

        serializer = FileSerializer(data, many = True)
        return Response(serializer.data)

