from django.urls import path
from views.proveedor.views import *

app_name = 'proveedor'

urlpatterns = [
    path('list/', ProveedorListView.as_view(), name='proveedor_list'),
    # path('add/', PersonaCreateView.as_view(), name='persona_add'),
    # path('edit/<int:pk>/', PersonaUpdateView.as_view(), name='persona_update'),
    # path('delete/<int:pk>/', PersonaDeleteView.as_view(), name='persona_delete'),
    # path('form/', PersonaFormView.as_view(), name='persona_form')
]
