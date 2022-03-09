from django.contrib.auth.decorators import login_required
from django.http import JsonResponse  # , HttpResponseRedirect
# from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from expte.models import Expte
# from expte.forms import ExpteForm


# def persona_list(request):
#     data = {
#        'title': 'Listado de Personas',
#        'personas': Persona.objects.all()
#
#    }
#    return render(request, 'persona_list.html', data)


class ExpteListView(ListView):
    model = Expte
    template_name = 'persona/persona_list.html'

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Exptes'
        # context['create_url'] = reverse_lazy('persona:persona_add')
        print(reverse_lazy('expte:expte_list'))
        return context


# class PersonaCreateViews(CreateView):
#     model = Persona
#     form_class = PersonaForm
#     template_name = 'persona/create_persona.html'
#     success_url = reverse_lazy('persona:persona_list')

#     @method_decorator(login_required)
#     def dispatch(self, request, *args, **kwargs):
#         return super().dispatch(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         data = {}
#         try:
#             action = request.POST['action']
#             if action == 'add':
#                 form = self.get_form()
#                 data = form.save()
#             else:
#                 data['error'] = 'No ingreso Ninguna Opción'
#         except Exception as e:
#             data['error'] = str(e)

#         return JsonResponse(data)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Agregar Personas'
#         context['entity'] = 'Personas'
#         context['action'] = 'add'
#         context['list_url'] = reverse_lazy('persona:persona_list')
#         return context


# class PersonaUpdateView(UpdateView):
#     model = Persona
#     form_class = PersonaForm
#     template_name = 'persona/create_persona.html'
#     success_url = reverse_lazy('persona:persona_list')

#     @method_decorator(login_required)
#     def dispatch(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         return super().dispatch(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         data = {}
#         try:
#             action = request.POST['action']
#             if action == 'edit':
#                 form = self.get_form()
#                 data = form.save()
#             else:
#                 data['error'] = 'No ingreso Ninguna Opción'
#         except Exception as e:
#             data['error'] = str(e)
#         return JsonResponse(data)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Editar Persona'
#         context['entity'] = 'Personas'
#         context['list_url'] = reverse_lazy('persona:persona_list')
#         context['action'] = 'edit'
#         return context


# class PersonaDeleteView(DeleteView):
#     model = Persona
#     template_name = 'persona/persona_delete.html'
#     success_url = reverse_lazy('persona:persona_list')

#     @method_decorator(login_required)
#     def dispatch(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         return super().dispatch(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         data = {}
#         try:
#             self.object.delete()
#         except Exception as e:
#             data['error'] = str(e)
#         return JsonResponse(data)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Eliminar Registro'
#         context['entity'] = 'Personas'
#         context['list_url'] = reverse_lazy('persona:persona_list')
#         return context


# class PersonaFormView(FormView):
#     form_class = PersonaForm
#     template_name = 'persona/create_persona.html'
#     success_url = reverse_lazy('persona:persona_list')

#     def form_valid(self, form):
#         print(form.is_valid())
#         print(form)
#         return super().form_valid(form)

#     def form_invalid(self, form):
#         print(form.is_valid())
#         print(form.errors)
#         return super().form_invalid(form)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Form | Persona'
#         context['entity'] = 'Personas'
#         context['action'] = 'add'
#         context['list_url'] = reverse_lazy('persona:persona_list')
#         return context
