# from django.db.models.fields.files import ImageFieldFile

from django.forms import *
from puntoe.models import Puntoe


class PuntoeForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['nombre'].widget.attrs['autofocus'] = True

    class Meta:
        model = Puntoe
        fields = '__all__'
        # widgets = {
        #     'nombre': TextInput(
        #         attrs={

        #             'placeholder': 'Ingrese Nombre',

        #         }

        #     ),
        #     'nro_dni': TextInput(
        #         attrs={

        #             'placeholder': 'Ingrese N° DNI',

        #         }

        #     ),

        #     'apellido': TextInput(
        #         attrs={

        #             'placeholder': 'Ingrese Apellido',

        #         }

        #     ),
        #     'vulneracion': TextInput(
        #         attrs={

        #             'placeholder': 'Seleccione Vulnerabilidad',

        #         }

        #     ),
        #     'tipodocumento': TextInput(
        #         attrs={

        #             'placeholder': 'Seleccione el Tipo de Documento',

        #         }

        #     ),
        #     'cantrecargas': NumberInput(
        #         attrs={

        #             'placeholder': 'Ingrese la cantidad de Recargas - Solo Numero',

        #         }

        #     ),
        #     'id_puntoencuentro': TextInput(
        #         attrs={

        #             'placeholder': 'Seleccione el punto de encuentro',

        #         }

        #     ),

        # }

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

    def clean(self):
        cleaned = super().clean()
        if len(cleaned['nombre']) >= 50:
            raise forms.ValidationError('Demaciados Caracteres')
            # self.add_error('nombre', 'Demaciados caracteres')
        return cleaned
