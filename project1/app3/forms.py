from django import forms

class ContactForm(forms.Form):
    choice=[
        ('Recruiter','Recruiter'),
        ('Student','Student'),
        ('Other','Other'),
    ]

    name=forms.CharField()
    email=forms.EmailField()
    about=forms.ChoiceField(widget=forms.RadioSelect,choices=choice,label='Which are you?')
    message=forms.CharField(required=False,widget=forms.Textarea,)