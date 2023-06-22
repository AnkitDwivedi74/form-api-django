from django.shortcuts import render
from .models import Myform
from rest_framework import viewsets
from .serializers import Fromser


# Create your views here.

class Userview(viewsets.ModelViewSet):
    queryset = Myform.objects.all()
    serializer_class = Fromser

def testing(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')

        entry = Myform(name=name, email=email)
        entry.save()

        return render(request, 'done.html')

    return render(request, 'form.html')

