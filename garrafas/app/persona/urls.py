from django.urls import path
from views.persona.views import PersonaListView, PersonaCreateView, PersonaUpdateView, PersonaDeleteView, PersonaFormView

app_name = 'persona'

urlpatterns = [
    path('list/', PersonaListView.as_view(), name='persona_list'),
    path('add/', PersonaCreateView.as_view(), name='persona_add'),
    path('edit/<int:pk>/', PersonaUpdateView.as_view(), name='persona_edit'),
    path('delete/<int:pk>/', PersonaDeleteView.as_view(), name='persona_delete'),
    path('form/', PersonaFormView.as_view(), name='persona_form'),
]
