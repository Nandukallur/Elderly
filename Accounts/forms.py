from django import forms
from .models import CustomUser

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'user_type', 'phone_number','address','role','blood_pressure','diabetes','cholesterol','allergies','chronic_conditions','medications','diet_details','documents','emergency_contact','name_of_person']
        widgets = {
            'password': forms.PasswordInput(),
            'user_type': forms.Select(attrs={'onchange': 'showFields()'})
        }

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['role'].required = False
        self.fields['blood_pressure'].required = False
        self.fields['diabetes'].required = False
        self.fields['cholesterol'].required = False
        self.fields['allergies'].required = False
        self.fields['chronic_conditions'].required = False
        self.fields['medications'].required = False
        self.fields['diet_details'].required = False
        self.fields['documents'].required = False
        self.fields['emergency_contact'].required = False
        self.fields['name_of_person'].required = False
        