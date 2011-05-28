'''
Created on May 28, 2011

@author: hongphi
'''
from django import forms



class CommentForm(forms.Form):
    content = forms.Textarea({'rows' : 10, 'cols' : 30})