# Create your views here.
from django.views.generic import TemplateView, DetailView


class HomePageView(TemplateView):
    template_name = 'main/pages/home_page.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['current_page'] = 'home'
        return context

home_page = HomePageView.as_view()
