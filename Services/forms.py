from django import forms
from .models import Report,HomeNurse,Ambulance_service, Feedback

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['name', 'contact', 'location', 'image']


class HomenurseForm(forms.ModelForm):
    class Meta:
        model = HomeNurse
        fields = '__all__'


class AmbulanceForm(forms.ModelForm):
    class Meta:
        model =Ambulance_service
        fields = '__all__'


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'
