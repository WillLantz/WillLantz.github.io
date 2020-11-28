from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Hobbies
from .models import Portfolio
from django.template import loader
from .forms import PortForm
from .forms import ContactForm


# Create your views here. Home, Hobbies, Portfolio, Contact
def home(request):
    template = loader.get_template('PortfolioDatabase/home.html')  # Creating the template and loading it in
    context = {}
    return render(request, 'PortfolioDatabase/home.html')


def hobbies(request):
    hobbies_list = Hobbies.objects.all()
    context = {
        'hobbies_list': hobbies_list,  # loading the hobbies list into the context
    }
    return render(request, 'portfoliodatabase/hobbies.html', context)


def portfolio(request):
    port_list = Portfolio.objects.all()
    context = {
        'port_list': port_list
    }
    return render(request, 'portfoliodatabase/portfolio.html', context)


def hobbydetail(request, item_id):
    item = Hobbies.objects.get(pk=item_id)
    context = {
        'item': item
    }
    return render(request, 'portfoliodatabase/hobbydetail.html', context)


def portfoliodetail(request, port_id):
    item = Portfolio.objects.get(pk=port_id)
    context = {
        'item': item
    }
    return render(request, 'portfoliodatabase/portfoliodetail.html', context)


def contact(request):
    form = ContactForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('portfoliodatabase:contact')

    return render(request, 'portfoliodatabase/contact.html', {'form': form})


def add_port(request):
    form = PortForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('portfoliodatabase:portfolio')

    return render(request, 'portfoliodatabase/portitem.html', {'form': form})


def update_port(request, id):
    item = Portfolio.objects.get(id=id)
    form = PortForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('portfoliodatabase:portfolio')

    return render(request, 'portfoliodatabase/portitem.html', {'form': form, 'item': item})


def delete_port(request, id):
    item = Portfolio.objects.get(id=id)

    if request.method == 'POST':
        item.delete()
        return redirect('portfoliodatabase:portfolio')

    return render(request, 'portfoliodatabase/port_delete.html', {'item': item})

