from django.urls import path
from .views import policy_list_create, policy_detail

urlpatterns = [
    path('policies/', policy_list_create, name='policy_list_create'),
    path('policies/<int:pk>/', policy_detail, name='policy_detail'),
]