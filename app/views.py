from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Perfume, Review
from .forms import ReviewForm
from django.utils import timezone

# library for query
from django.db.models import Q

from django.core.paginator import Paginator


def home(request):
    return render(request, 'index.html')

def perfumes(request, id):
    # review_form = ReviewForm()
    perfume = get_object_or_404(Perfume, id=id)
    return render(request, 'perfume.html', {"perfume": perfume})
    # return render(request, 'perfume.html', {"perfume": perfume, "review_form": review_form})


def new_review(request, id):
    new = Review()
    new.content = request.POST['content']
    new.perfume = get_object_or_404(Perfume, pk=id)
    new.user = request.user
    new.first_scent = request.POST['first_scent']
    new.put_scent = request.POST['put_scent']
    new.rest_scent = request.POST['rest_scent']

    # 다중 선택 항목
    type_list = request.POST.getlist('type_list')
    new.type_explain = ''
    for Type in type_list:
        new.type_explain += Type
        new.type_explain += ' '  # html 페이지에 띄울 때 문자열을 공백 기준으로 자르면 될 듯

    new.power = request.POST['power']

    new.save()
    return redirect('perfumes', id)

# form으로 리뷰 작성을 받을 경우
# def new_review(request, id):
#     filled_form = ReviewForm(request.POST)
#     if filled_form.is_valid():
#         finished_form = filled_form.save(commit=False)
#         finished_form.perfume = get_object_or_404(Perfume, id=id)
#         finished_form.save()
#     return redirect('perfumes', id)


def about(request):
    return render(request, 'about.html')


def category(request):
    return render(request, 'category.html')


def survey(request):
    return render(request, 'survey.html')


def reviews(request):
    return render(request, 'reviews.html')


def ranking(request):
    return render(request, 'ranking.html')

#### show real time search result ####
def search(request):
    searched = request.GET['searched']
    perfumes = Perfume.objects.filter(name__contains=searched)
    perfumeList = [(p.id, p.name) for p in perfumes[:10]]
    data = {'searchedList': perfumeList}
    return JsonResponse(data)

#### search result page ####
def searched(request):
    season_list = request.GET.getlist('season_list')  # ['summer']
    flavor_list = request.GET.getlist('flavor_list') # ['woody']
    gender_list = request.GET.getlist('gender_list') # ['man']
    # perfumes = Perfume.objects.filter(name__contains=searched)

    query = Q()
    for i, Season in enumerate(season_list):
        if i == 0: query = query & Q(season=Season)
        else: query = query | Q(season=Season)
        
    for i, Flavor in enumerate(flavor_list):
        if i == 0: query = query & Q(flavor=Flavor)
        else: query = query | Q(flavor=Flavor)
        
    for i, Gender in enumerate(gender_list):
        if i == 0: query = query & Q(gender=Gender)
        else: query = query | Q(gender=Gender)
        
    searched = request.GET['searched']
    if len(searched.replace(' ', '')):
        query = query & Q(name__contains=searched)
    print(query)
    perfumes = Perfume.objects.filter(query)
    paginator = Paginator(perfumes, 10)
    pageNum = request.GET.get('page')
    perfumes = paginator.get_page(pageNum)
    return render(request, 'search-result.html', {'searched':searched, 'perfumes': perfumes})
