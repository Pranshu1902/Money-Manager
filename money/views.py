from django.views.generic.list import ListView
from django.forms import ModelForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
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

class AddTransactionView(CreateView):
    form_class = TransactionForm
    template_name = 'add_transaction.html'

    def form_valid(self, form):
        form.save()
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect('/view/')

class ViewTransactionsView(ListView):
    queryset = Transaction.objects.all()
    template_name = "view.html"
    context_object_name = "transactions"
