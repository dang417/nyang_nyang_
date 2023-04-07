from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm

# Create your views here.

def index(request):
    movies = Movie.objects.all()
    context = {'movies':movies}
    return render(request, 'movies/index.html', context)

def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES) #데이터(유저가 입력한 제목,내용) 박혀있는 폼
        #request.FILES 까지 넣어줘야 이미지 파일이 저장됨

        if form.is_valid(): #폼에 든 데이터들이 유효성 검사 통과한 데이터라면
            movies = form.save() #db에 저장
            #POST /articles/create/ -> 게시글 생성 요청에 대한 응답으로
            #게시글 생성하는 것으로 본인의 역할 마침
            return redirect('movies:detail', movies.pk)
        #유효하지 않다면 create 비어있는 폼으로 감

    else: #GET 방식이라면 폼 만드는 것까지만
        form = MovieForm() #데이터 안박힌 폼

    context = {'form':form}
    return render(request, 'movies/create.html', context)

def detail(request, pk):
    movies = Movie.objects.get(pk=pk)
    context = {'movies':movies}
    return render(request, 'movies/detail.html',context)



def update(request, pk):
    movies = Movie.objects.get(pk=pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movies)
        if form.is_valid():
            form.save()
            return redirect('movies:detail', pk=movies.pk)
    else:
        form = MovieForm(instance=movies)
    
    context = {'form':form, 'movies':movies}
    return render(request, 'movies/update.html', context)

def delete(request, pk):
    movies = Movie.objects.get(pk=pk)
    movies.delete()
    return redirect('movies:index')   
