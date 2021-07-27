from realestate.realtors.models import Realtor
from django.shortcuts import render

# Create your views here.
def realtor (request):
    realtors = Realtor.objects.all()  # selecting everthing from class
    context ={
        # 'key': value,
        'realtors': realtors
    }
    return render(request, '',context)


