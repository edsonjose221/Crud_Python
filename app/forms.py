from django.forms import ModelForm, fields, models
from app.models import Carros

# Create the form class.

class CarrosForm(ModelForm):
    class Meta:
        model = Carros
        fields = ['modelo', 'marca', 'ano']