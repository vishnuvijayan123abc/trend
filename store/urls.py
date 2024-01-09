from django.urls import path
from store import views


urlpatterns = [
    path('login/',views.SigninView.as_view(),name="sign_up"),
    path("category/",views.CategoryView.as_view(),name="cat"),
    path("category/list/",views.CategoryListView.as_view(),name="cat_list"),
    path("category/edit/<int:pk>/",views.categoryUpdateView.as_view(),name="cat_edit"),
    path("signout/",views.SignoutView.as_view(),name="sign_out"),
    
]
