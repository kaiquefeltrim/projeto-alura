from django import forms

class LoginForms(forms.Form):
    name_login = forms.CharField(
        label= "Usuario",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder": "Digite seu Usuario"
            }
        )
    )

    password_login = forms.CharField(
        label= "Senha",
        required=True,
        max_length=40,
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                "placeholder": "Digite seu Senha"
            }
        )
    )

class RegisterForms(forms.Form):
    name_register = forms.CharField(
        label= "Name",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder": "Digite seu Usuario"
            }
        )
    )

    email_register = forms.EmailField(
        label= "E-mail",
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                "class":"form-control",
                "placeholder": "exemplo@hotmail.com"
            }
        )
    )

    password_register = forms.CharField(
        label= "Senha",
        required=True,
        max_length=40,
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                "placeholder": "Digite seu Senha"
            }
        )
    )

    password_register2 = forms.CharField(
        label= "Confirma Senha",
        required=True,
        max_length=40,
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                "placeholder": "Digite seu Senha"
            }
        )
    )

    def clean_name_register(self):
        name = self.cleaned_data.get("name_register")

        if name:
            name= name.strip()
            if " " in name:
                raise forms.ValidationError("Não é possivel inserir espaços dentro do campo usuario")
            else:
                return name

    def clean_password_register2(self):
        password_register = self.cleaned_data.get("password_register")
        password_register2 = self.cleaned_data.get("password_register2")
       
        if password_register and password_register2:
            if password_register != password_register2:
                raise forms.ValidationError("As senhas estão difirentes")
            else:
                return password_register2


