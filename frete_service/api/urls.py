from django.urls import path
from api.resources import FreteGetAllView

urlpatterns = [
    path('fretes/', FreteGetAllView.as_view(), name='frete-list'),
]