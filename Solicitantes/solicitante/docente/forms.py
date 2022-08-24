from django.forms import ModelForm, EmailInput

from docente.models import Docente


class DocenteFormulario(ModelForm):
    class Meta:
        model = Docente
        fields = '__all__'
        witgets = {
            'email': EmailInput(attrs={'type': 'email'})
        }