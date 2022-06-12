from django.shortcuts import render, get_object_or_404
from .models import *
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView


def main(request):
    post = Post.objects.all()
    return render(request, 'post_list.html', context={'post': post})


def post(request, slug):
    new = Post.objects.get(slug__iexact=slug)
    return render(request, 'post.html', context={'new': new})


class AuthorList(ListView):
    model = Author                                                                                                      # Обращение ко всей модели
    context_object_name = 'Authors'
    # queryset = Author.objects.all()                                                                                   # Обращение к определенным участкам
    template_name = 'news/author_list.html'                                                                             # Имя и путь шаблона

#   def get_queryset(self):
#       self.authorUser = get_object_or_404(Author, name=self.args[0])
#       return Author.objects.filter(authorUser=self.authorUser)

# class Post(DetailView):

class PostList(ListView):
    model = Post
    context_object_name = 'post'
    ordering = 'title'                                                                                                  # Поле для сортировки
    template_name = 'news/post_list_a.html'
    paginate_by = 3


# class MyForm(FormView):
#     form_class = myform
#     success_url = '/success/'
#
#     def form_valid(self, form):
#         return super(MyForm, self).form_valid(form)


# class PostCreate(CreateView):
#     model = Post
#     fields = '__all__'
#     template_name = 'news/post_form.html'