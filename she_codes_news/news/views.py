from django.views import generic
from django.urls import reverse_lazy
from .models import NewsStory
from .forms import StoryForm
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.decorators import login_required
from django.shortcuts import render
# from django.contrib.auth.models import user
from django.contrib.auth import get_user_model


User = get_user_model()

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
    template_name = 'news/UserProfile.html'

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['user_stories'] = NewsStory.objects.filter(author=self.request.user)[:4]
            context['all_stories'] = NewsStory.objects.filter(author=self.request.user)
            return context 
    

class AuthorListView(generic.ListView):
    model = User
    template_name = 'news/authorList.html'
    context_object_name = 'author_list'
    # ordered_authors = User.objects.all().order_by('author.pk')


class AuthorDetailView(generic.DetailView):
    model = User
    template_name = 'news/AuthorDetail.html'
   
# class StoryUpdateButtonView(LoginRequiredMixin, generic.DetailView):
#     model = User

class StoryUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = NewsStory
    # fields = '__all__'
    template_name = 'news/storyUpdate.html'
    success_url = reverse_lazy('news:index')
    


# class StoriesByAuthor(generic.ListView):
#     template_name = 'news/storyAuthor.html'

#     def get_queryset(self):
#         '''Return all news stories.'''
#         return NewsStory.objects.all()

#     def get_context_data(self, **kwargs):
#             author = story.author
#             context = super().get_context_data(**kwargs)
#             context['user_stories'] = NewsStory.objects.filter(author=author)[:4]
#             context['all_stories'] = NewsStory.objects.filter(author=author)
#             return context 
#this is going to need to call on the other users, not self...probably something to do with forrienKey or PK or something...

# class StoriesByAuthor():
#     template_name = 'news/storyAuthor.html'
#     model = User
#     context_object_name = 'author'
#     slug_field = "Username"