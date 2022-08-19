from django.http import JsonResponse
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Perfume, PostModel, Review
from .forms import PostForm, CommentForm
# from django.utils import timezone
import random

# library for query
from django.db.models import Q

from django.core.paginator import Paginator


def home(request):
    return render(request, 'index.html')


def perfumes(request, id):
    # review_form = ReviewForm()
    perfume = get_object_or_404(Perfume, id=id)
    reviews = Review.objects.filter(perfume=perfume).order_by('-date')
    flavor1 = perfume.flavor
    rec = Perfume.objects.filter(flavor=flavor1)[1:6]
    return render(request, 'perfume.html', {"perfume": perfume, 'reviews': reviews, 'rec':rec})


def new_review(request, id):
    new = Review()
    new.content = request.POST['content']
    new.perfume = get_object_or_404(Perfume, pk=id)
    try:
        new.user = request.user
    except:
        pass
    try:
        new.rating = request.POST['reviewStar']
    except:
        pass
    try:
        new.first_scent = request.POST['first_scent']
    except:
        pass
    try:
        new.put_scent = request.POST['put_scent']
    except:
        pass
    try:
        new.rest_scent = request.POST['rest_scent']
    except:
        pass

    # 다중 선택 항목
    type_list = request.POST.getlist('type_list')
    new.type_explain = ''
    for Type in type_list:
        new.type_explain += Type
        new.type_explain += ' '  # html 페이지에 띄울 때 문자열을 공백 기준으로 자르면 될 듯
    extra_explain = request.POST.get('extra_explain', '')
    for Type in extra_explain.split(' '):
        new.type_explain += Type
        new.type_explain += ' '

    new.power = request.POST.get('power', False)
    # if new.power is False:
    #     return redirect('perfumes', id)  # 기존 내용을 보존하고 redirect하고 싶은데 방법을 찾지 못함

    new.save()
    return redirect('perfumes', id)


def about(request):
    return render(request, 'about.html')

#### 카테고리 디폴트 페이지 (spring 향수들 목록) ####


def category(request):
    query = Q(season='spring')
    perfumes = Perfume.objects.filter(query)
    return render(request, 'category.html', {'perfumes': perfumes})


#### 다른 카테고리 선택 ####
def category_detail(request, id):
    if id == 1:
        pass
    elif id == 2:
        pass
    elif id == 3:
        pass
    elif id == 4:
        pass
    elif id == 5:
        pass
    elif id == 6:
        pass
    elif id == 7:
        pass
    elif id == 8:
        pass
    elif id == 9:
        pass

    return render(request, 'category_detail.html')


def survey(request):
    return render(request, 'survey.html')


#### 게시판 페이지 ####
def board(request):
    posts = PostModel.objects.filter().order_by('-date')
    paginator = Paginator(posts, 5)
    pagnum = request.GET.get('page')
    posts = paginator.get_page(pagnum)
    return render(request, 'board.html', {'posts': posts})


#### 게시물 작성 ####
def postcreate(request):
    if request.method == 'POST' or request.method == 'FILES':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('board')
    else:
        form = PostForm()
    return render(request, 'postcreate.html', {'form': form})


#### 개별 게시물 보여주기 ####
def post_detail(request, post_id):
    post = get_object_or_404(PostModel, id=post_id)
    comment_form = CommentForm()
    return render(request, 'post-detail.html', {'post': post, 'comment_form': comment_form})

#### 게시물 댓글 작성 ####


def new_comment(request, post_id):
    filled_form = CommentForm(request.POST)
    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.post = get_object_or_404(PostModel, pk=post_id)
        finished_form.save()
    return redirect('post_detail', post_id)

#### 게시물 삭제 ####


def delete(request, post_id):
    object = get_object_or_404(PostModel, pk=post_id)
    object.delete()
    return redirect('board')

#### 게시물 수정 ####


def edit(request, post_id):
    post = PostModel.objects.get(id=post_id)    # 수정하고자 하는 객체 갖고 와서
    if request.method == "POST":            # 만일 request method가 POST라면
        form = PostForm(request.POST, request.FILES)    # 입력 내용을 갖고와서
        if form.is_valid():                             # 입력 내용 검수한 뒤
            # 입력 내용 중 title을 수정하고자 하는 객체의 title에 저장!
            post.title = form.cleaned_data['title']
            # 입력 내용 중 body를 수정하고자 하는 객체의 body에 저장!
            post.body = form.cleaned_data['body']
            post.save()                                 # 그리고 수정된 값을 저장한 객체는 저장
            # 수정이 되었으면 detail 페이지(해당 그 게시물 페이지)로 이동
            return redirect('/post_detail/'+str(post.pk))
    else:                                        # 만일 request method가 GET이면
        form = PostForm()
        return render(request, 'post-edit.html', {'form': form})  # 입력 공간을 갖다준다


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
    flavor_list = request.GET.getlist('flavor_list')  # ['woody']
    gender_list = request.GET.getlist('gender_list')  # ['man']
    # perfumes = Perfume.objects.filter(name__contains=searched)

    query = Q()
    for i, Season in enumerate(season_list):
        if i == 0:
            query = query & Q(season=Season)
        else:
            query = query | Q(season=Season)

    for i, Flavor in enumerate(flavor_list):
        if i == 0:
            query = query & Q(flavor=Flavor)
        else:
            query = query | Q(flavor=Flavor)

    for i, Gender in enumerate(gender_list):
        if i == 0:
            query = query & Q(gender=Gender)
        else:
            query = query | Q(gender=Gender)

    searched = request.GET['searched']
    if len(searched.replace(' ', '')):
        query = query & Q(name__contains=searched)
    print(query)
    width = int(request.GET['window-width'])
    if width > 820:
        numToDisplay = 14
    elif width > 630:
        numToDisplay = 6
    else:
        numToDisplay = 4
    perfumes = Perfume.objects.filter(query)
    print(len(perfumes))
    paginator = Paginator(perfumes, numToDisplay)
    print(paginator.num_pages)
    pageNum = 1  # request.GET.get('page')

    perfumes = paginator.get_page(pageNum)
    return render(request, 'search-result.html', {'searched': searched, 'perfumes': perfumes})
