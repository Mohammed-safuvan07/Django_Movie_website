from django.shortcuts import render, redirect
from .forms import tables_form

from myapp.models import table


# Create your views here.
def demo(request):
    values = table.objects.all()
    return render(request, 'index.html', {'value': values})


def info(request, id):
    value1 = table.objects.get(id=id)

    return render(request, 'info.html', {'value1': value1})


def add(request):
    if request.method == 'POST':
        name = request.POST.get('name', )
        year = request.POST.get('year', )
        desc = request.POST.get('desc', )
        image = request.FILES['image']
        val = table(name=name, year=year, desc=desc, image=image)
        val.save()

    return render(request, 'add_info.html')


def update(request, id):
    det = table.objects.get(id=id)
    form = tables_form(request.POST or None, request.FILES, instance=det)

    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'update.html', {'details': det, 'form': form})


def delete(request, id ):
    if request.method == 'POST':
        data = table.objects.get(id=id)
        data.delete()
        return redirect('/')
    return render(request, 'delete.html')
