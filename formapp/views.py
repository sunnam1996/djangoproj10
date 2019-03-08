from django.shortcuts import render
from .form import NameForm
from django.http import HttpResponse
def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponse('data submitted successfully')
    else:
        form = NameForm()
        return render(request,'name.html',{'form': form})




