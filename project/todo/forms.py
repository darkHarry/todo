from django import forms
from django.forms import ModelForm
from todo.models import Todo


class AddTodoForm(forms.Form):
    new_todo = forms.CharField(
        max_length=100,
        required=True,
        label="",
        widget=forms.TextInput(attrs={
            "placeholder": "things to do...",
            "autofocus": "",
            "autocomplete": "off",
        }))

    def clean_new_todo(self):
        new_todo = self.cleaned_data["new_todo"]

        return new_todo


class EditTodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ["todo_text"]

    def __init__(self, *args, **kwargs):
        super(EditTodoForm, self).__init__(*args, **kwargs)
        self.fields["todo_text"].widget = forms.TextInput(attrs={
            "value": self.fields["todo_text"],
            "required": "",
        })
