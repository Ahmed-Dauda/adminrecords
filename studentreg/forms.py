from django import forms
from django.forms import ModelForm

from studentreg.models import Salat, Dining, Lightout, Prep, Hygiene


class Salatform(forms.ModelForm):

    class Meta:
        model = Salat
        fields = '__all__'


class Diningform(forms.ModelForm):

    class Meta:
        model = Dining
        fields = '__all__'


class Lightoutform(forms.ModelForm):

    class Meta:
        model = Lightout
        fields = '__all__'


class Prepform(forms.ModelForm):

    class Meta:
        model = Prep
        fields = '__all__'

class Hygieneform(forms.ModelForm):

    class Meta:
        model = Hygiene
        fields = '__all__'       