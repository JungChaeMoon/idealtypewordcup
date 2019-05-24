from django import forms
from .models import Candidate


class CandidateForm(forms.ModelForm):

    class Meta:
        model = Candidate
        fields = ['title', 'photo', 'contest']
        widgets = {'contest': forms.HiddenInput()}
