from django.http import HttpResponse
from django.shortcuts import render, redirect
import requests
# Create your views here.
from rest_framework.viewsets import ModelViewSet

from premiumcars.models import Car
from premiumcars.forms import AddCarForm, ConverterForm
from premiumcars.serializers import CarSerializer


def index(request):
    if 'save_published' in request.POST:
        form = AddCarForm(request.POST or None)
        if form.is_valid():
            brand = form.cleaned_data.get('brand')
            model = form.cleaned_data.get('model')
            price = form.cleaned_data.get('price')
            count = form.cleaned_data.get('count')
            car = Car(brand=brand, model=model, price=price, count=count)
            car.save()
    if 'car_delete' in request.POST and 'car_id' in request.POST:
        print(request.POST)
        try:
            id = request.POST['car_id']
            print(id)
            Car.objects.get(id=id).delete()
        except:
            pass
    if 'car_edit' in request.POST and 'car_id' in request.POST:
        try:
            print(21)
            id = request.POST['car_id']
            return redirect('edit', pk=id)
        except:
            pass

    add_car_form = AddCarForm()
    context = {
        'form': add_car_form,
        'cars': Car.objects.all()
    }
    return render(request, 'index.html', context=context)


def edit(request, pk):
    obj = Car.objects.get(pk=pk)
    if request.POST:
        form = AddCarForm(request.POST or None)
        if form.is_valid():
            obj.brand = form.cleaned_data.get('brand')
            obj.model = form.cleaned_data.get('model')
            obj.price = form.cleaned_data.get('price')
            obj.count = form.cleaned_data.get('count')
            obj.save()
            return redirect(index)

    form = AddCarForm()

    form.fields['brand'].initial = obj.brand
    form.fields['model'].initial = obj.model
    form.fields['price'].initial = obj.price
    form.fields['count'].initial = obj.count
    context = {'form': form}
    return render(request, 'edit.html', context=context)


def add_car(request):
    car = Car(brand='VW', model='passat b3', price=1000, count=100)
    car.save()
    return render(request, 'index.html')


def all_cars(request):
    cars = Car.objects.all()
    print(cars, (len(cars)))
    return render(request, 'index.html')


def del_car(request):
    last_index_car = len(Car.objects.all())

    Car.objects.get(id=last_index_car).delete()
    print(Car.objects.all())
    return render(request, 'index.html')


class CarsView(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
