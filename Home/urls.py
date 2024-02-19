from django.urls import path
from .import views

urlpatterns = [         # class based view . call as_view func
    path('handle/',views.HandleFileUpload.as_view()),
    path('',views.home , name='home'),
    path('download/<uid>/',views.download, name='download'),
]


