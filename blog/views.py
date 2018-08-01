 # -*- coding: utf-8 -*-
from django.views.generic import TemplateView
from blog.forms import HomeForm,CommentForm
from django.shortcuts import render,redirect,get_object_or_404
from blog.models import Post,Comment
from django.views.generic import UpdateView,DeleteView,CreateView
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.views.generic import DetailView
class HomeView(TemplateView):

    template_name='blog/home.html'

    def get(self,request):
        form=HomeForm()
        posts=Post.objects.all().order_by('-created')
        args = {'form':form,'posts':posts}
        return render(request,self.template_name,args)

    def post(self,request):
        form = HomeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user=request.user
            post.save()
            text = form.cleaned_data['post'] #takes post from forms.py
            form = HomeForm() #To remove text from form afetr submission
            return redirect('/blog')
        args = {'form':form,'text':text}
        return render(request,self.template_name,args)

class EditPost(UpdateView):
    model = Post
    form_class = HomeForm

    template_name = "blog/edit_post.html"





        # We can also get user object using self.request.user  but that doesnt work
        # for other models.



    def get_success_url(self, *args, **kwargs):
        return reverse("blog:view")

class DeletePost(DeleteView):
    model = Post
    template_name = "blog/delete_post.html"

    def get_success_url(self, *args, **kwargs):
        return reverse("blog:view")

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('blog:detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/post_comment.html', {'form': form,})
class DetailPost(DetailView):
    model = Post
    template_name = "blog/post.html"
