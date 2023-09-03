from django import forms
from tasks.models import TaskModel

class TaskForm(forms.ModelForm):
    due_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    class Meta:
        model = TaskModel
        fields= ['title', 'description','due_date', 'category', 'priority', 'status']
        