'''
Created on May 28, 2011

@author: hongphi
'''
from django import forms
#from captcha.fields import ReCaptchaField


class CommentForm(forms.Form):
    content = forms.CharField(widget = forms.Textarea({'rows' : 5, 'cols' : 55}))
#   capcha = ReCaptchaField()
    
