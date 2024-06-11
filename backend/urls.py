from django.urls import path
from .views import FileUploadView, QueryView

urlpatterns = [
    path('upload/', FileUploadView.as_view(), name='file-upload'),
    path('query/', QueryView.as_view(), name='query')
]

