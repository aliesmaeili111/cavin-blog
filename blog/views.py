from django.shortcuts import render, get_object_or_404
from .models import Article,Category
from django.views.generic import ListView,DetailView
from account.models import User
from account.mixins import AuthorAccessMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q



class ArticleList(ListView):
 
    queryset = Article.objects.published()
    paginate_by =  12
    


class ArticleDetail(DetailView):

    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Article.objects.published(),slug=slug)
   
            
class CategoryList(ListView):
    template_name = "blog/category_list.html"
    paginate_by =  12
    
    def get_queryset(self):
        global category
        slug  = self.kwargs.get('slug')
        category = get_object_or_404(Category.objects.active(),slug=slug) 
        return category.articles.published()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = category
        return context
    
    
class AuthorList(ListView):
    template_name = "blog/author_list.html"
    paginate_by =  12
    
    def get_queryset(self):
        global author
        username  = self.kwargs.get('username')
        author = get_object_or_404(User,username=username)  
       
        return author.articles.published()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = author
        return context
    
    
class ArticlePreview(AuthorAccessMixin,DetailView):
    template_name = "blog/article_detail.html"
    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Article,pk=pk)
    
    

class SearchList(ListView):
    paginate_by = 5
    template_name = 'blog/search_list.html'
    
    def get_queryset(self):
        global search
        search = self.request.GET.get('q')
        return Article.objects.filter(Q(description__icontains = search) | Q(title__icontains = search))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = search
        return context
    
    
    
def about(request):
    return render(request,"blog/about.html")

