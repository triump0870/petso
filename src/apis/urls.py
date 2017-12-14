from django.conf.urls import url, include
from apis.views import PetView, PetListCreateAPIView

urlpatterns = [
    url(r'^pets/$', PetListCreateAPIView.as_view(), name='pet-list'),
    url(r'^pets/(?P<pk>\d+)/$', PetView.as_view(), name='pet-detail')

]
