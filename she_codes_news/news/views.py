from django.views import generic
from django.urls import reverse_lazy
from .models import NewsStory
from .forms import StoryForm
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.decorators import login_required
from django.shortcuts import render

class AddStoryView(LoginRequiredMixin, generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class IndexView(generic.ListView):
    template_name = 'news/index.html'

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['latest_stories'] = NewsStory.objects.all().order_by('-pub_date')[:4]
            context['all_stories'] = NewsStory.objects.all().order_by('-pub_date')
            return context

class StoryView(generic.DetailView):
    model = NewsStory
    template_name = "news/story.html"
    context_object_name = 'story'

class StoryViewByAuthor(LoginRequiredMixin, generic.ListView):
    template_name = 'news/postList.html'

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['user_stories'] = NewsStory.objects.all().order_by('-author')[:4]
            context['all_stories'] = NewsStory.objects.all().order_by('-author')
            return context 
    
    
    
    # userstory (request):
    #     user = request.user
    #     user_posts = NewsStory.objects.filter(author=request.user).order_by('-pub_date')
    #     template = 'postList.html'
    #     return render(request, template, {'user_posts':user_posts,'user': user})
