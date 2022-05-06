from calendar import c
from urllib import request
from django.shortcuts import render, redirect


from .models import  Pizza, Topping, Entry
from .forms import EntryForm

# Create your views here.
def index(request):
    return render(request, 'MainApp/index.html')

def pizzas(request):
    pizzas = Pizza.objects.all
    context = {'pizzas':pizzas}

    return render(request, 'MainApp/pizzas.html', context)

def pizza(request, pizza_id):
    pizza= Pizza.objects.get(id=pizza_id)

    toppings = pizza.topping_set.order_by('id')
    entries = pizza.entry_set.order_by('-id')
    context = {'pizza':pizza,'toppings':toppings, 'entries':entries}

    return render(request, 'MainApp/pizza.html',context)

def new_entry(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)


    if request.method !='POST':
        form = EntryForm()
    else:
        form = EntryForm(data= request.POST)

        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.pizza = pizza 
            new_entry.save()
            form.save()

            return redirect('MainApp:pizza', pizza_id=pizza_id)
    context = {'form': form, 'topic':pizza}
    return render(request, 'MainApp/new_entry.html',context)