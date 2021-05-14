from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions
from .models import Freelancer
from .serializers import FreelancerSerializer


class FreelancerListView(ListAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Freelancer.objects.all()
    serializer_class = FreelancerSerializer
    pagination_class = None


class FreelancerView(RetrieveAPIView):
    queryset = Freelancer.objects.all()
    serializer_class = FreelancerSerializer


class TopSellerView(ListAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Freelancer.objects.filter(top_seller=True)
    serializer_class = FreelancerSerializer
    pagination_class = None
