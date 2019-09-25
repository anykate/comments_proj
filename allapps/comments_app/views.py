from django.shortcuts import render, redirect
from .forms import CommentForm
from .models import Comment


# Create your views here.
def index(request):
    form = CommentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('comments_app:index')
    comment_obj = Comment.objects.order_by('-date_added')
    return render(request, 'comments_app/index.html', {'form': form, 'comment_obj': comment_obj})
