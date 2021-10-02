from django import path
from django.view.generic import TemplateView

urlpatterns = [
    post('signup', TemplateView.as_view(template_name='home.html'), 'signup'),
]