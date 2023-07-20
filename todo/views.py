from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView, DetailView, UpdateView, ListView, DeleteView

from .forms import FormCreate
from .models import Task
from django.contrib.auth.mixins import LoginRequiredMixin


class CreateTask(LoginRequiredMixin, CreateView):
    model = Task
    template_name = "create.html"
    # fields = ["title", 'text', 'complete']
    form_class = FormCreate
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateTask, self).form_valid(form)


class ListTask(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'list_task'

    def get_context_data(self, **kwargs):
        context = super(ListTask, self).get_context_data(**kwargs)
        context['list_task'] = context['list_task'].filter(user=self.request.user)
        context['count'] = context['list_task'].filter(complete=False).count()
        return context


class DetailTask(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'detail.html'
    fields = "__all__"
    context_object_name = 'det_task'
    slug_field = 'title'
    slug_url_kwarg = 'title'

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            queryset = queryset.filter(user=self.request.user)
        return queryset


class EditTask(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = "update.html"
    fields = ['title', 'text', 'complete']
    success_url = reverse_lazy('home')
    slug_field = 'title'
    slug_url_kwarg = 'title'


class DeleteTask(DeleteView):
    model = Task
    success_url = reverse_lazy('home')
    template_name = 'delete.html'
    slug_field = 'title'
    slug_url_kwarg = 'title'

