from django.shortcuts import render, HttpResponse, redirect
from .models import Post
from .forms import PostForm


# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'post_list.html', context)


def post_delete(request, post_id):
    if request.method == 'POST':
        post = Post.objects.get(pk=post_id)
        post.delete()
        return redirect('post_list')


def post_modify(request, post_id):
    if request.method == "POST":
        # 수정 저장
        post = Post.objects.get(pk=post_id)
        form = PostForm(request.POST, instance=post)  # 새로 입력된 인스턴스 데이터를 form 인스턴스에 새로 담는다.
        if form.is_valid():
            form.save()  # 변경한 form을 저장한다 (수정, 업데이트)
            return redirect('post_list')
    else:
        # 수정 입력
        post = Post.objects.get(pk=post_id)  # 특정 데이터를 인스턴스에 담는다.
        form = PostForm(instance=post)  # 기존에 존재하는 데이터를 가져온다. (수정화면에 내용 포함)
        context = {
            'post': post,
            'form': form,
        }
        return render(request, 'post_modify.html', context)
