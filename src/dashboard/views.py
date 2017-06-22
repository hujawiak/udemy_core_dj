from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.http import HttpResponse, Http404
from django.views.generic import TemplateView, View, DetailView, ListView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import ModelFormMixin
from django.views.generic.base import TemplateResponseMixin, ContextMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.messages.views import SuccessMessageMixin
from .models import Book
from .forms import BookForm


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **kwargs):
        view = super(LoginRequiredMixin, cls).as_view(**kwargs)
        return login_required(view)

class MultipleObjectMixin(object):
    def get_object(self, queryset=None, *args, **kwargs):
        slug = self.kwargs.get("slug")
        if slug:
            try:
                obj = self.model.objects.get(slug=slug)
            except self.model.MultipleObjectsReturned:
                obj = self.get_queryset().first()
            return obj
        raise Http404

class BookDetailView(ModelFormMixin, MultipleObjectMixin, DetailView):
    model = Book
    template_name = 'book_detail.html'
    form_class = BookForm
    
    def get_context_data(self, **kwargs):
        context = super(BookDetailView, self).get_context_data()
        context['form'] = self.get_form()
        return context
    
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            self.object = self.get_object()
            form = self.get_form()
            if form.is_valid():
                return self.form_valid(form)
            else:
                return self.form_invalid(form)

class BookDeleteView(MultipleObjectMixin, DeleteView):
    model = Book
    template_name = 'book_confirm_delete.html'
    
    def get_success_url(self):
        return reverse('profiles:book_list')
    
class BookListView(ListView):
    model = Book
    template_name = "book_list.html"
    
class BookCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    #model = Book
    #fields = ["title", "description"]
    form_class = BookForm
    template_name = "form.html"
    
    
    def form_valid(self, form):
        form.instance.added_by = self.request.user
        #form.instance.last_edited_by = self.request.user
        return super(BookCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("profiles:book_list")
    
    def get_success_message(self, cleaned_data):
        success_message = '"{}" has been created at {}'.format(cleaned_data['title'], self.object.timestamp)
        return success_message
    
class BookUpdateView(MultipleObjectMixin, UpdateView):
    model = Book
    form_class = BookForm
    template_name = "form.html"




class DashboardTemplateView(LoginRequiredMixin,TemplateView):
    template_name = 'about.html'
    
    def get_context_data(self, **kwargs):
        context = super(DashboardTemplateView, self).get_context_data(**kwargs)
        context['title'] = "About dupa"
        return context
    
class MyView(LoginRequiredMixin, TemplateResponseMixin, ContextMixin,View):
    
    #@method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return HttpResponse("Hello world!")
    
