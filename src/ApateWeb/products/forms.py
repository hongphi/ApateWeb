'''
Created on May 28, 2011

@author: hongphi
'''
from django import forms



class CommentForm(forms.Form):
    content = forms.CharField(widget = forms.Textarea({'rows' : 5, 'cols' : 55}))
    
