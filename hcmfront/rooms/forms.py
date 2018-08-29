from django import forms
from .models import ReservRoom


class ReservRoomForm(forms.ModelForm):
    class Meta:
        model = ReservRoom
        fields = ['room', 'additional_supplies', 'capacity', 'hours', 'status']
        widgets = {
            'room': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'additional_supplies': forms.SelectMultiple(
                attrs={
                    'class': 'form-control',
                }
            ),
            'capacity': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                }),
            'hours': forms.SelectMultiple(
                attrs={
                    'class': 'form-control',
                }
            ),
        }

        labels = {
            'room': 'Select Room',
            'capacity': 'How many people will be?',
            'additional_supplies': 'Set you need',
            'hours': ''
        }
