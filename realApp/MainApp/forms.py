from django import forms
from .models import Job, JobApplication

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
        widgets = {
            'job_title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter job title',
            }),
            'job_description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Describe the job role, responsibilities, and expectations',
                'rows': 5,
                'style': 'resize: vertical; border: 2px solid #ced4da; border-radius: 8px;',
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., New York, Remote, etc.',
            }),
            'job_deadline': forms.DateInput(attrs={
                'type': 'date',  # HTML5 calendar date picker
                'class': 'form-control',
                'placeholder': 'Select deadline date',
            }),
            # Add additional fields with custom widgets if needed, for example:
            # 'salary': forms.NumberInput(attrs={
            #     'class': 'form-control',
            #     'placeholder': 'e.g., 60000',
            # }),
        }

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['job']
        widgets = {
            'job': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Select the job you’re applying for',
            }),
        }
