# from django.db.models.fields.files import ImageFieldFile

from django.forms import *
from persona.models import Persona
from ubicacion.models import Departamento, Distrito


class PersonaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for form in self.visible_fields():
        #     form.field.widget.attrs['class'] = 'form-control'
        #     form.field.widget.attrs['autocomplete'] = 'off'
        # self.fields['tipodocumento'].widget.attrs['autofocus'] = True

    class Meta:
        model = Persona
        fields = ['tipodocumento',
                  'nro_dni',
                  'nombre',
                  'apellido',
                  'vulneracion',
                  'departamento_id',
                  'distrito_id',
                  'calle',
                  'nro_calle',
                  'obs',
                  'imgdni_front',
                  'imgdni_back',
                  'usuario_id'
                  ]
        widgets = {
            'nombre': TextInput(
                attrs={

                    'placeholder': 'Ingrese Nombre/s',

                }

            ),
            'tipodocumento': Select(
                attrs={
                    'placeholder': 'Seleccione el Tipo de Documento',
                    'class': 'aling-items-center',
                    }
            ),
            'nro_dni': TextInput(
                attrs={

                    'placeholder': 'Ingrese N° DNI',

                }

            ),

            'apellido': TextInput(
                attrs={

                    'placeholder': 'Ingrese Apellido',

                }

            ),
            'vulneracion': Select(
                attrs={

                    'placeholder': 'Seleccione Vulnerabilidad',

                }

            ),


            'departamento_id': NumberInput(
                attrs={

                    'placeholder': 'Seleccione el Departamento que figura en el Documento',
                      }

            ),
            'distrito_id': NumberInput(
                attrs={

                    'placeholder': 'Seleccione el Distrito que figura en el Documento',
                      }

            ),
            'calle': TextInput(
                attrs={

                    'placeholder': 'Calle que figura en el Documento',
                      }

            ),
            'nro_calle': NumberInput(
                attrs={

                    'placeholder': 'Nro de calle - 0 es S/N',
                      }

            ),
            'obs': Textarea(
                attrs={
                    'placeholder': 'Detalle del Domicilo',
                    'rows': '2',
                    'cols': '1'
                      }

            ),
            'usuario_id': NumberInput(
                attrs={
                    # 'type': 'hidden'
                }

            ),

        }

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
    #     if len(cleaned['nombre']) <= 3:
    #         raise forms.ValidationError('Escriba al menos 3 Caracteres')
    #         # self.add_error('nombre', 'Demaciados caracteres')
    #     return cleaned
