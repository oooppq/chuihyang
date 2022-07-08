from django.shortcuts import get_object_or_404, redirect, render
from .models import Perfume

# Create your views here.
def home(request):
    if request.method == "GET":
        return render(request, 'index.html',{'is_searched':'0'})
    elif request.method == "POST":
        searched = request.POST['searched']
        perfumes = Perfume.objects.filter(name__contains=searched)
        if len(perfumes) >= 10:
            perfumes = perfumes[:10]
        return render(request, 'index.html', {'perfumes':perfumes, 'searched':searched, 'is_searched':'1'})
        #return redirect('perfumes', perfume[0].pk)

def perfumes(request, id):
    perfume = get_object_or_404(Perfume, id=id)
    return render(request, 'perfume.html', {"perfume":perfume})

def about(request):
    return render(request, 'about.html')

def category(request):
    return render(request, 'category.html')

def taste_test(request):
    return render(request, 'taste-test.html')

def reviews(request):
    return render(request, 'reviews.html')

def ranking(request):
    return render(request, 'ranking.html')