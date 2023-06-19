from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        # Perform additional form-level validation
        # Validate data and raise a ValidationError if needed
        return cleaned_data