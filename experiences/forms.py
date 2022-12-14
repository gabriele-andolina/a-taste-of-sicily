from django import forms
from .models import Experience


class ExperienceForm(forms.ModelForm):

    class Meta:
        model = Experience
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
