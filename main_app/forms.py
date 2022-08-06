from .models import Messages
from django.forms import ModelForm, TextInput, Textarea

class MessagesForm(ModelForm):
    class Meta:
        model = Messages
        fields = ['form_name', 'message']

        widgets = {
            'form_name': TextInput(attrs={
                'class': 'form_input_class',
                'placeholder': 'Имя'
            }),
            'message': Textarea(attrs={
                'class': 'form_input_class',
                'placeholder': 'Сообщение',
                'cols': "100%",
                'rows': "3"
            })
        }