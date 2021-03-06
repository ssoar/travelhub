from django.urls import reverse_lazy
from django.views import generic
from .models import Country, City, Category, Tag

class CountriesIndexView(generic.ListView):
    model = Country

class CountryDetailView(generic.DetailView):
    model = Country

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if not obj.is_public and not self.request.user.is_authenticated:
            raise Http404
        return obj

class CitiesIndexView(generic.ListView):
    model = City

class CityDetailView(generic.DetailView):
    model = City

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if not obj.is_public and not self.request.user.is_authenticated:
            raise Http404
        return obj


class Home(generic.ListView):
    context_object_name = 'home'
    template_name = 'travelhub/home.html'
    queryset = Country.objects.all()

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['city_list'] = City.objects.all()
        context['category_list'] = Category.objects.all()
        context['tag_list'] = Tag.objects.all()
        return context

"""
class TagListView(ListView):
    queryset = Tag.objects.annotate(num_posts=Count(
        'post', filter=Q(post__is_public=True)))
"""