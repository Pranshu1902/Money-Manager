from django.views.generic.list import ListView
from django.forms import ModelForm
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm

from money.models import Transaction

# User Login view

class UserLoginView(LoginView):
    template_name = "login.html"
    success_url = "/add/"

class UserSignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "signup.html"
    success_url = "/add/"

# Transaction views

class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = ['amount', 'description', 'spent']

class AddTransactionView(CreateView, LoginRequiredMixin):
    form_class = TransactionForm
    template_name = 'add_transaction.html'

    def form_valid(self, form):
        form.save()
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect('/view/')

class ViewTransactionsView(ListView, LoginRequiredMixin):
    queryset = Transaction.objects.all()
    template_name = "view.html"
    context_object_name = "transactions"

class HomeView(ListView, LoginRequiredMixin):
    queryset = Transaction.objects.all()
    template_name = "home.html"
    context_object_name = "transactions"

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # username
        user = self.request.user
        context["user"] = user

        # total spent
        total_spent = 0
        for transaction in Transaction.objects.filter(user=user, spent=True):
            total_spent += transaction.amount
        
        context["total_spent"] = total_spent

        # total earned
        total_earned = 0
        for transaction in Transaction.objects.filter(user=user, spent=False):
            total_earned += transaction.amount
        
        context["total_earned"] = total_earned

        context["net"] = total_earned - total_spent

        return context
