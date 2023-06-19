from django.http import HttpResponse
from django.shortcuts import render
from .forms import StudentForm

def index(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse('Success')

    else:
        form = StudentForm()

    return render(request, 'index.html', {'form': form})
