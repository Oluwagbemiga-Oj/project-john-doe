from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.views.decorators.http import require_POST
from .models import store_collection

def ecomm(request):
    template = loader.get_template("new_store.html")
    return HttpResponse(template.render())

def home(request):
    return render(request, 'home.html')

def inventory(request):
    return render(request, 'inventory.html')

def store(request):
    return render(request, 'store.html')

def search(request):
    return render(request, 'search.html')

def cart(request):
    return render(request, 'cart.html')

def profile(request):
    return render(request, 'profile.html')

def marketplace(request):
    return render(request, 'marketplace.html')

def welcome(request):
    template = loader.get_template("welcome.html")
    return HttpResponse(template.render())
    
def get_new_store_details(request):
    return render(request, 'get_new_store_details.html')


@require_POST
def add_new_store(request):
    if request.method == 'POST':
        # Retrieve form data from the request
        business_name = request.POST.get('businessName')
        business_description = request.POST.get('businessDescription')
        product_categories = request.POST.get('productCategories')
        color_palette = request.POST.get('colorPalette')
        tagline = request.POST.get('tagline')
        instagram = request.POST.get('instagram')
        twitter = request.POST.get('twitter')

        # Store the data in MongoDB
        storefront_data = {
            'business_name': business_name,
            'business_description': business_description,
            'product_categories': product_categories,
            'color_palette': color_palette,
            'tagline': tagline,
            'instagram': instagram,
            'twitter': twitter,
        }
        store_collection.insert_one(storefront_data)
        response_data = {
            "message": "Sign Up Successful"
        }    
        return JsonResponse(response_data)

     