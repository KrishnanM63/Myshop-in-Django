from django.urls import path
from . import views
urlpatterns = [
    path("regiseter_form", views.regisetr_pg, name="regiseter_form"),
    path("login/", views.login_pg, name="login"),
    path("", views.home_pg, name="home"),
    path("add_cart/<str:post_id>", views.detail, name="add"),
    path("cart/", views.cart_view, name="cart"),
    path("remove_cart/<str:post_id>/", views.remove_cart, name="remove_cart"),
    path("update_cart/", views.update_cart, name="update_cart"),
    path("place_order/", views.place_order, name="place_order"),
    path("logout/",views.logout_fn,name="logout")
]


  
