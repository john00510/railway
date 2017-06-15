from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'pnr_status/', views.pnr_status, name='pnr_status'),
]

