from django import forms
class new_accound (forms.Form):
    frist_name=forms.CharField(label="frist name")
    last_name=forms.CharField(label="last name")
    email=forms.CharField(label="email",widget=forms.EmailInput())
    user_name=forms.CharField(label="user name")
    bio=forms.CharField(label="bio",widget=forms.Textarea(),required=False)
    gender=forms.ChoiceField()
    password=forms.CharField(label="password",min_length=8,widget=forms.PasswordInput())
    confpassword=forms.CharField(label="confirm password",min_length=8,widget=forms.PasswordInput())
class login(forms.Form):
    user_name=forms.CharField(label="user name")
    password=forms.CharField(label="password",widget=forms.PasswordInput())
