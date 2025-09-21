from django.urls import path
from api.resources import FreteCreateView, FreteDeleteView, FreteDetailView, FreteListView, FreteListView

urlpatterns = [
    path('fretes/', FreteListView.as_view(), name='frete_list'),
    path('fretes/detalhes/<str:frete_uuid>', FreteDetailView.as_view(), name='fretes_detail'),
    path('fretes/adicionar/', FreteCreateView.as_view(), name='fretes_create'),
    path('fretes/excluir/<str:frete_uuid>', FreteDeleteView.as_view(), name='fretes-delete'),
]