# from django.conf.urls import url
from django.urls import path
# from django.http import HTTPresponse
from .views import s3Views

urlpatterns = [
    path("s3/", s3Views.s3_public_check, name="S3 Public Visibility"),
    # path("about/", AboutPageView.as_view(), name="about"),
]
