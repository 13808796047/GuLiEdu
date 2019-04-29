from django import forms

class UserRegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True,min_length=3,max_length=15,error_messages={
        'required':'密码必须填写',
        'min_length':'密码小于3位',
        'max_length':'密码超过15位',
    })