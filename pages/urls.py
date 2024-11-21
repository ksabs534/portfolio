from django.urls import path
from .views import HomePageView, AboutPageView, EducationPageView, BlogListView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("post/", BlogListView.as_view(), name="post"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("education/", EducationPageView.as_view(), name="education"),
    
]
