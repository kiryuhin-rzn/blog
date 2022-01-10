from django.views import generic
from app_todo.models import TodoListItem
from app_todo.forms import ToDoForm
from django.http import HttpResponseRedirect
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import DetailView
from django import forms
from django.http import HttpResponse
from django.utils import timezone


class ToDoListView(generic.ListView):
    template_name = 'app_todo/todo_list.html'

    def get_queryset(self):
        #user = self.request.user
        #queryset = user.object(all).order_by('date_due')
        #self.content = get_object_or_404(TodoListItem, user = self.request.user)
        if self.request.user.is_authenticated:
            queryset = TodoListItem.objects.order_by('date_due').filter(user=self.request.user)
            return queryset
        else:
            return HttpResponse("Чтобы создать свой To Do лист, необходимо зарегистрироваться!")

    '''model = TodoListItem
    template_name = 'app_todo/todo_list.html'
    context_object_name = 'todo_list'
    user = request.user
    queryset = user.TodoListItem(all).order_by('date_due')'''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = ToDoForm()
        if self.request.user.is_authenticated:
            form.fields['user'].widget = forms.HiddenInput()
            form.fields['user'].initial = self.request.user
            context['form'] = form
            context['now'] = timezone.now()#timezone.localtime()

            return context
        else:
            context['context'] = "Чтобы создать свой To Do, необходимо зарегистрироваться!"
            return context


    def post(self, request, *args, **kwargs):
        form = ToDoForm(request.POST)

        if form.is_valid():
            context = form.save()
            context.user = self.request.user
            context.save()

            #user.content=context
            #user.save()
            #form.save_o2o()


            return HttpResponseRedirect('/todo')
        else:
            #form = ToDoForm()
            #return render(request, 'app_todo/todo_list.html', {'form': form})
            return HttpResponse("Чтобы создать свой To Do лист, необходимо зарегистрироваться!")


class ToDoDetailView(DetailView):
    model = TodoListItem
    template_name = 'app_todo/todo_detail.html'


class ToDoDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'app_todo.can_delete'
    model = TodoListItem
    template_name = 'app_todo/todo_delete.html'
    success_url = reverse_lazy('todo_list')
