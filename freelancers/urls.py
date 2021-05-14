from django.urls import path
from .views import FreelancerView, TopSellerView, FreelancerView


urlpatterns = [
    path('', FreelancerView.as_view()),
    path('topseller', TopSellerView.as_view()),
    path('<pk>', FreelancerView.as_view()),
]
