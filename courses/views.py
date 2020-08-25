from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Course

class CouseListView(ListView):
    model = Course

class CouseDetailView(DetailView):
    model = Course
    
    