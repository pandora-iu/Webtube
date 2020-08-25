from django.urls import path
from .views import CouseListView, CouseDetailView

app_name = 'courses'

urlpatterns = [
    path('', CouseListView.as_view(), name='list_view'),
    path('<>', CouseDetailView.as_view(), name='detail_view'),
]
