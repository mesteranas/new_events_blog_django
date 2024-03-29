from django import forms
class new_accound (forms.Form):
    frist_name=forms.CharField(label="frist name")
    last_name=forms.CharField(label="last name")
    email=forms.CharField(label="email",widget=forms.EmailInput())
    user_name=forms.CharField(label="user name")
    bio=forms.CharField(label="bio",widget=forms.Textarea(),required=False)
    gender=forms.ChoiceField(label="gender",choices=[("male","male"),("female","female")],required=True)
    password=forms.CharField(label="password",min_length=8,widget=forms.PasswordInput())
    confpassword=forms.CharField(label="confirm password",min_length=8,widget=forms.PasswordInput())
class login(forms.Form):
    user_name=forms.CharField(label="user name")
    password=forms.CharField(label="password",widget=forms.PasswordInput())
class RAddPost(forms.Form):
    title=forms.CharField(label="title")
    content=forms.CharField(label="content ",widget=forms.Textarea())
    resources=forms.CharField(label='resources',widget=forms.Textarea(),required=False)
    category=forms.ChoiceField(label="category",choices=[("technology","technology"),("sports","sports")])
class delete(forms.Form):
    password=forms.CharField(label="confirm password to delete account",widget=forms.PasswordInput())
class ChangePassword(forms.Form):
    currentPassword=forms.CharField(label="current password",widget=forms.PasswordInput())
    newPassword=forms.CharField(min_length=8,label="new password",widget=forms.PasswordInput())
    confNewPassword=forms.CharField(min_length=8,label="confirm new password",widget=forms.PasswordInput())
class editProfile(forms.Form):
    first_name=forms.CharField(label="first name")
    last_name=forms.CharField(label="last name")
    email=forms.CharField(label="email",widget=forms.EmailInput())
    bio=forms.CharField(label="bio",widget=forms.Textarea(),required=False)