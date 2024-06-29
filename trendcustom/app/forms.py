from django import forms
from django.contrib.auth.models import User
from .models import Keycap, Switch, Case, Plata, Stabilizer, Plate, Completed_Keyboard

class CompletedKeyboardForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        hidden_fields = ['user']
        
        for field_name in hidden_fields:
            self.fields[field_name].widget.attrs['style'] = 'display:none;'
    
    user = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.HiddenInput())
    case = forms.ModelChoiceField(queryset=Case.objects.all(), required=False)
    plata = forms.ModelChoiceField(queryset=Plata.objects.all(), required=False)
    plate = forms.ModelChoiceField(queryset=Plate.objects.all(), required=False)
    stabilizer = forms.ModelChoiceField(queryset=Stabilizer.objects.all(), required=False)
    switch = forms.ModelChoiceField(queryset=Switch.objects.all(), required=False)
    keycap = forms.ModelChoiceField(queryset=Keycap.objects.all(), required=False)

    class Meta:
        model = Completed_Keyboard
        fields = '__all__'

        