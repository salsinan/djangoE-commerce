from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Sale

# Create your views here.
def home_view(request):
    hello = 'hello world from the view'
    return render(request, 'sales/home.html', {'h': hello})

class SaleListView(ListView):
    model = Sale
    template_name = 'sales/main.html'

class SaleDetailView(DetailView):
    model = Sale
    template_name = 'sales/detail.html'