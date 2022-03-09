# from django.db.models.fields.files import ImageFieldFile

from django.forms import *
from proveedor.models import Proveedor
# from ubicacion.models import Departamento, Distrito


class ProveedorForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for form in self.visible_fields():
        #     form.field.widget.attrs['class'] = 'form-control'
        #     form.field.widget.attrs['autocomplete'] = 'off'
        # self.fields['tipodocumento'].widget.attrs['autofocus'] = True

    class Meta:
        model = Proveedor
        

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

    # def clean(self):
    #     cleaned = super().clean()
    #     if len(cleaned['nombre']) >= 50:
    #         raise forms.ValidationError('Demaciados Caracteres')
    #         # self.add_error('nombre', 'Demaciados caracteres')
    #     return cleaned
