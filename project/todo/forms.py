from django import forms


class AddTodoForm(forms.Form):
    new_todo = forms.CharField(
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
