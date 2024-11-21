from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Post

class HomePageView(TemplateView):
    template_name = "home.html"

class AboutPageView(TemplateView):
    template_name = "about.html"

class EducationPageView(TemplateView):
    template_name = "education.html"

class BlogListView(ListView):
    model = Post
    template_name = "post.html"


# Create your views here.
