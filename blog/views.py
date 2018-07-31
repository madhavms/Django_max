 # -*- coding: utf-8 -*-
from django.views.generic import TemplateView
from blog.forms import HomeForm
from django.shortcuts import render,redirect
from blog.models import Post

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
            return redirect('/blog',pk=post.pk)
        args = {'form':form,'text':text}
        return render(request,self.template_name,args)
class PostView(TemplateView):
    template_name='home/posts.html'
    def get(self,request):

        posts=Post.objects.all().order_by('-created')
        args = {'posts':posts}
        return render(request,self.template_name,args)

class EditPost(TemplateView):
    template_name='home/post_edit.html'
    def post_edit(request, pk):
        post = get_object_or_404(Post, pk=pk)
        if request.method == "POST":
            form = HomeForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.user = request.user
                post.updated = timezone.now()
                post.save()
                return redirect('/blog', pk=post.pk)
        else:
            form = HomeForm()
        return render(request, 'home/post_edit.html', {'form': form})
