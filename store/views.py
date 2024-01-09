from django.shortcuts import render,redirect
from api.models import Category
from django.contrib.auth.models import User
from django.views.generic import FormView,CreateView,View,UpdateView
from store.forms import LoginForm,CategoryForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.urls import reverse
from store.decrators import login_required
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator

# Create your views here.
dec=[login_required,never_cache]

class SigninView(FormView):
    template_name="login.html"
    form_class=LoginForm

    def post(self,request,*args, **kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user_obj=authenticate(request,username=uname,password=pwd)
            if user_obj:
                login(request,user_obj)
                print(request.user)
                return  redirect("cat_list")
            print("invalid")
            return render(request,"login.html",{"form":form})
@method_decorator(dec,name="dispatch")
class CategoryView(CreateView):
    template_name="category.html"
    form_class=CategoryForm


    def get_success_url(self):
        return reverse("cat")
@method_decorator(dec,name="dispatch")
class CategoryListView(View):
    def get(self,request,*args, **kwargs):
        qs=Category.objects.all()
        return render (request,"category_list.html",{"data":qs})

@method_decorator(dec,name="dispatch")
class categoryUpdateView(UpdateView):
    template_name="category_update.html"
    form_class=CategoryForm
    model=Category


    def get_success_url(self):
        return reverse("cat_list")
    

class SignoutView(View):
    def get(self,request,*args, **kwargs):
        logout(request)
        return redirect("sign_up")

