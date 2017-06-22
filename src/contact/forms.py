# coding=utf-8
from django import forms
from django.contrib.auth import get_user_model
#from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .models import Contact

User = get_user_model()

class ContactForm(forms.ModelForm):
    email = forms.EmailField(required=True, help_text="Valid email, you prick")
    comment = forms.CharField(max_length=5000, required=True, widget=forms.Textarea)
    
    class Meta:
        model= Contact
        fields = ('name',)
        
    # def clean_email(self):
    #     email = self.cleaned_data["email"]
    #     if User.objects.filter(email=email).exists():
    #         raise forms.ValidationError("Dupa")
    #     return email
        
    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        email = cleaned_data.get("email")
        if email.startswith("e"):
            self._errors["email"] = self.error_class(["Eeeee"])
            self._errors["name"] = self.error_class(["Nananna", "dudpap"])
            self._errors["comment"] = self.error_class(["Dupa"])
            #raise forms.ValidationError("Email cannot start with E")
        
            del cleaned_data["email"]
        
        # password = cleaned_data['password']
        # final_password = make_password(password)
        # del cleaned_data['password']
        # cleaned_data['password'] = final_password
        
        return cleaned_data
    
