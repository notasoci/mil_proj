from django.views.generic import ListView
from .models import Miliciano

class HomePageView(ListView):
    model = Miliciano
    template_name = 'home.html'
    context_object_name = 'todos_los_milicianos_list' #new'

