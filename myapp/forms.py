from django import forms
from .models import Client, Immobile, RegistrarLocation


# Cadastro Cliente
class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

# Cadastro de um Imovél
class ImmobileForm(forms.ModelForm):
    immobile = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    class Meta:
        model = Immobile
        fields = '__all__'
        exclude = ('is_mobile',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.widget.__class__ in [forms.CheckboxInput, forms.RadioSelect]:
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'

# Registro de locação de um imóvel
class RegistrarLocationForm(forms.ModelForm):
    dt_start = forms.DateTimeField(widget=forms.DateInput(format='%d-%m-%Y',attrs={'type': 'date',}))
    dt_end = forms.DateTimeField(widget=forms.DateInput(format='%d-%m-%Y',attrs={'type': 'date',}))
    
    class Meta:
        model = RegistrarLocation
        fildes = '__al__'
        exclude = ('immobile', 'create_at',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

