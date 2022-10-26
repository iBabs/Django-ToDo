from asyncio import tasks
from django import forms
from .models import Mytodos


class MyAppForm(forms.Model):
    class Meta:
        model = Mytodos
        fields = {
            "task",
            "deatails"
        }