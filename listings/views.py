from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from django.http.response import Http404, HttpResponseRedirect
from django.shortcuts import render
from .models import Listing
from realtors.models import Realtor


# Create your views here.

def index (request):
    listings = Listing.objects.all()  # selecting everthing from class
    paginator = Paginator(listings,6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context ={
        # 'key': value,
        # 'listings': listings,
        'listings':paged_listings
    }
    
    return render(request, 'listings/listings.html',context)

def detail(request,listing_id):
    try:
        listing = Listing.objects.get(pk=listing_id) # same as WHERE 
        mvp = Realtor.objects.order_by('-name').filter(is_mvp=True)[:1]
        context ={
            # 'key': value,
            # 'realtors': realtors,
            'mvp': mvp,
            'listing': listing
            }
    except Listing.DoesNotExist:
        raise Http404('Listing does not exist')
    return render (request,'listings/listing.html',context)

# search fuction
def search(request):
    listings = Listing.objects.all()  # selecting everthing from class
    # Keyword
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            listings = listings.filter(description__icontains=keywords)
    #area
    if 'area' in request.GET:
        area = request.GET['area']
        if area:
            listings = listings.filter(area__icontains=area)
    #county
    if 'county' in request.GET:
        county = request.GET['county']
        if county:
            listings = listings.filter(county__iexact=county)
    #price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            listings = listings.filter(price__lte=price)  #gte / lte  less than/greater than
    #bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            listings = listings.filter(bedrooms__icontains=bedrooms)

    paginator = Paginator(listings,3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context ={
        # 'key': value,
        # 'listings': listings,
        'listings':paged_listings
    }
    
    return render(request, 'listings/search.html',context)