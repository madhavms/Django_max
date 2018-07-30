from django import forms
from home.models import Post


class HomeForm(forms.ModelForm):
    title=forms.CharField(widget=forms.TextInput(          #gives bootstrap class

    attrs={
              'class': 'form-control',
              'placeholder':'Enter Title'

        }
        ))
    post=forms.CharField(widget=forms.Textarea(          #gives bootstrap class

    attrs={
          'class': 'form-control',
          'placeholder':'Write a post'

    }
    ))

    class Meta:
        model = Post
        fields = ('title','post',)
