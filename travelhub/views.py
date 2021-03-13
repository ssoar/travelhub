from django.urls import reverse_lazy
from django.views import generic
from .models import Country, City, Category, Tag, Place, Comment, Reply
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostSearchForm, CommentCreateForm
from django.db.models import Q


class CountriesIndexView(generic.ListView):
    model = Country
    paginate_by = 12
    queryset = Country.objects.filter(is_public=True)

    def get_queryset(self):
        queryset = super().get_queryset()
        self.form = form = PostSearchForm(self.request.GET or None)
        if form.is_valid():
            # 選択したタグが含まれた記事
            tags = form.cleaned_data.get('tags')
            if tags:
                for tag in tags:
                    queryset = queryset.filter(tags=tag)

            key_word = form.cleaned_data.get('key_word')
            if key_word:
                for word in key_word.split():
                    queryset = queryset.filter(
                        Q(name__icontains=word)| 
                        Q(slug__icontains=word)| 
                        Q(capital__icontains=word)|
                        Q(tags__name__icontains=word)|
                        Q(tags__slug__icontains=word)
                        )


        queryset = queryset.order_by('-updated_at')#.prefetch_related('tags')
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = PostSearchForm(self.request.GET or None)
        return context

class CountryDetailView(generic.DetailView):
    model = Country

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if not obj.is_public and not self.request.user.is_authenticated:
            raise Http404
        return obj

class CitiesIndexView(generic.ListView):
    model = City
    paginate_by = 12
    queryset = City.objects.filter(is_public=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = PostSearchForm(self.request.GET or None)
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        self.form = form = PostSearchForm(self.request.GET or None)
        if form.is_valid():
            # 選択したタグが含まれた記事
            tags = form.cleaned_data.get('tags')
            if tags:
                for tag in tags:
                    queryset = queryset.filter(tags=tag)

            key_word = form.cleaned_data.get('key_word')
            if key_word:
                for word in key_word.split():
                    queryset = queryset.filter(
                        Q(name__icontains=word)| 
                        Q(country__name__icontains=word)| 
                        Q(slug__icontains=word)| 
                        Q(country__slug__icontains=word)|
                        Q(tags__name__icontains=word)|
                        Q(tags__slug__icontains=word)
                        )


        queryset = queryset.order_by('-updated_at').prefetch_related('tags')
        return queryset

class CityDetailView(generic.DetailView):
    model = City
    context_object_name = 'city'

    def get_context_data(self, **kwargs):
        context = super(CityDetailView, self).get_context_data(**kwargs)
        q_word = context['city'].name
        context['place_list'] = Place.objects.filter(city__name__iexact=q_word)
        return context


    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if not obj.is_public and not self.request.user.is_authenticated:
            raise Http404
        return obj


class Home(generic.ListView):
    context_object_name = 'country'
    template_name = 'travelhub/home.html'
    queryset = Country.objects.all()

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['city_list'] = City.objects.all()
        context['category_list'] = Category.objects.all()
        context['tag_list'] = Tag.objects.all()
        context['search_form'] = PostSearchForm(self.request.GET or None)
        return context

class CommentCreate(generic.CreateView):
    """記事へのコメント作成ビュー。"""
    model = Comment
    form_class = CommentCreateForm

    def form_valid(self, form):
        city_pk = self.kwargs['pk']
        city = get_object_or_404(City, pk=city_pk)
        comment = form.save(commit=False)
        comment.target = city
        comment.save()
        return redirect('travelhub:citydetail', pk=city_pk)

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['city'] = get_object_or_404(City, pk=self.kwargs['pk'])
            return context


"""
class TagListView(ListView):
    queryset = Tag.objects.annotate(num_posts=Count(
        'post', filter=Q(post__is_public=True)))
"""