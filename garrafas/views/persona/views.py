from django.contrib.auth.decorators import login_required
from django.core.checks.messages import Error
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.urls.base import is_valid_path
from django.utils.decorators import async_only_middleware, method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from persona.models import *
from persona.forms import PersonaForm


class PersonaListView(ListView):
    model = Persona
    template_name = 'persona/persona_list.html'

    @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Persona.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un Error'

        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado - Personas'
        context['create_url'] = reverse_lazy('persona:persona_add')
        context['list_url'] = reverse_lazy('persona:persona_list')
        # print(reverse_lazy('persona:persona_list'))
        return context

class PersonaCreateView(CreateView):

    model = Persona
    form_class = PersonaForm
    template_name = 'persona/persona_create.html'
    success_url = reverse_lazy('persona:persona_list')

    @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Agregar Persona'
        context['list_url'] = reverse_lazy('persona:persona_list')
        context['action'] = 'add'
        return context

class PersonaUpdateView(UpdateView):

    model = Persona
    form_class = PersonaForm
    template_name = 'persona/persona_create.html'
    success_url = reverse_lazy('persona:persona_list')

    @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Persona'
        context['list_url'] = reverse_lazy('persona:persona_list')
        context['action'] = 'edit'
        return context

class PersonaDeleteView(DeleteView):
    model = Persona
    template_name = 'persona/persona_delete.html'
    success_url = reverse_lazy('Persona:persona_list')

    @method_decorator(login_required)
    # @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar Persona'
        context['list_url'] = reverse_lazy('persona:persona_list')
        return context

class PersonaFormView(FormView):
    form_class = PersonaForm
    template_name = 'persona/persona_create.html'
    success_url = reverse_lazy('persona:persona_list')

    def form_valid(self, form):
        print(form.is_valid)
        print (form)
        return super().form_valid(form)
    
    def form_invalid(self, form):
        print(form.is_valid)
        print (form.errors)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Agregar Persona - FORM'
        context['list_url'] = reverse_lazy('persona:persona_list')
        return context