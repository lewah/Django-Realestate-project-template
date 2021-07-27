from realtors.models import Realtor
from django.shortcuts import render
from listings.models import Listing
from listings.choices import counties    # importing as a dictionary

# Create your views here.
def homepage (request):
  # listings = Listing.objects.all()   selecting everthing from class,importing data from app listings
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context ={
        # 'key': value,
        'listings': listings,
        'counties': counties,
    }
    
    return render(request, 'pages/index.html',context)

# def aboutpage(request):
#         return render(request, 'pages/about.html')

def aboutpage(request):
  mvp = Realtor.objects.order_by('-name').filter(is_mvp=True)[:1]
  realtors = Realtor.objects.order_by('-hire_date')
  context ={
        # 'key': value,
        'realtors': realtors,
        'mvp': mvp
    }
    
  return render(request, 'pages/about.html',context)
