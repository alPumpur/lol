from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView, DeleteView
from django.core.signing import BadSignature
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import AdvUser, Application
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView
from .forms import RegisterUserForm, CreateApplicationForm
from django.views import generic

def index(request):
    num_applications = Application.objects.filter(status_app__exact='П').count()
    num_complete = Application.objects.filter(status_app__exact='В').order_by('-date')[:4]
    context = {
        'num_applications': num_applications,
        'num_complete': num_complete
    }
    return render(request, 'main/index.html', context)


class BBLoginView(LoginView):
    template_name = 'main/login.html'


class RegisterUserView(CreateView):
    model = AdvUser
    template_name = 'main/register_user.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('main:register_done')


class RegisterDoneView(TemplateView):
    template_name = 'main/register_done.html'


def user_activate(request, sign):
    try:
        username = signer.unsign(sign)
    except BadSignature:
        return render(request, 'main/bad_signature.html')
    user = get_object_or_404(AdvUser, username=username)
    if user.is_activated:
        template = 'main/user_is_activated.html'
    else:
        template = 'main/activation_done.html'
        user.is_activated = True
        user.is_active = True
        user.save()
    return render(request, template)


@login_required
def profile(request):
    return render(request, 'main/profile.html')


class BBLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'main/logout.html'

class CreateApplicationView(CreateView):
    form_class = CreateApplicationForm
    template_name = 'main/create_application.html'
    success_url = reverse_lazy('main:index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateApplicationView, self).form_valid(form)

class ApplicationListView(generic.ListView):
    model = Application
    context_object_name = 'application_list'
    template_name = 'application_list.html'

class DeleteApplicationView(LoginRequiredMixin, DeleteView):
   model = Application
   template_name = 'main/application_delete.html'
   success_url = reverse_lazy('main:index')