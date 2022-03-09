from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse  # , HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from proveedor.forms import ProveedorForm
from proveedor.models import Proveedor


# def puntoe_list(request):
#     data = {
#         'title': 'Lista - Puntos de Encuentro',
#         'puntoe': Puntoe.objects.all()
#        }
#     return render(request, 'puntoe/puntoe_list.html', data)
class ProveedorListView(ListView):
    model = Proveedor
    template_name = 'proveedor/proveedor_list.html'

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Proveedor.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un Error'

        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listade proveedores'
        # context['create_url'] = reverse_lazy('puntoe:puntoe_add')
        print(reverse_lazy('proveedor:proveedor_list'))
        return context


# class PuntoeCreateViews(CreateView):
#     model = Puntoe
#     form_class = PuntoeForm
#     template_name = 'puntoe/create_puntoe.html'
#     success_url = reverse_lazy('puntoe:puntoe_list')

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
#         context['title'] = 'Agregar Puntoe'
#         context['entity'] = 'Puntoe'
#         context['action'] = 'add'
#         context['list_url'] = reverse_lazy('puntoe:puntoe_list')
#         return context


# class PuntoeUpdateView(UpdateView):
#     model = Puntoe
#     form_class = PuntoeForm
#     template_name = 'puntoe/create_puntoe.html'
#     success_url = reverse_lazy('puntoe:puntoe_list')

#     # @method_decorator(login_required)
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
#         context['title'] = 'Editar Puntoe'
#         context['entity'] = 'Puntoe'
#         context['list_url'] = reverse_lazy('puntoe:puntoe_list')
#         context['action'] = 'edit'
#         return context


# class PuntoeDeleteView(DeleteView):
#     model = Puntoe
#     template_name = 'puntoe/puntoe_delete.html'
#     success_url = reverse_lazy('puntoe:puntoe_list')

#     # @method_decorator(login_required)
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
#         context['entity'] = 'Puntoe'
#         context['list_url'] = reverse_lazy('puntoe:puntoe_list')
#         return context


# class PuntoeFormView(FormView):
    form_class = PuntoeForm
    template_name = 'puntoe/create_puntoe.html'
    success_url = reverse_lazy('puntoe:puntoe_list')

    def form_valid(self, form):
        print(form.is_valid())
        print(form)
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.is_valid())
        print(form.errors)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Form | Puntoe'
        context['entity'] = 'Puntoe'
        context['action'] = 'add'
        context['list_url'] = reverse_lazy('puntoe:puntoe_list')
        return context
