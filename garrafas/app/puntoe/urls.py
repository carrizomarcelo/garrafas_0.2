from django.urls import path
from puntoe.views import *
app_name = 'puntoe'

urlpatterns = [
    path('list/', PuntoeListView.as_view(), name='puntoe_list'),
    path('puntoe/add/', PuntoeCreateViews.as_view(), name='puntoe_add'),
    path('puntoe/edit/<int:pk>/', PuntoeUpdateView.as_view(), name='puntoe_edit'),
    path('puntoe/delete/<int:pk>/', PuntoeDeleteView.as_view(), name='puntoe_delete'),
    path('puntoe/form/', PuntoeFormView.as_view(), name='puntoe_form')
    # path('list/', puntoe_list)
]
