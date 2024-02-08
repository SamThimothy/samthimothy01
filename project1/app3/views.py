from django.shortcuts import render,redirect
from .forms import ContactForm
from .models import Contact_Model

# Create your views here.
def contact_view(request):
    form=ContactForm
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            print('Success')
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            about=form.cleaned_data['about']
            message=form.cleaned_data['message']
            ndata=Contact_Model(name=name,mail=email,choice=about,message=message)
            ndata.save()
            return redirect('/')
    return render(request,'app1/contact.html',{'form':form})


def data_view(request):
    data=Contact_Model.objects.all()
    return render(request,'app3/data.html',{'data':data})