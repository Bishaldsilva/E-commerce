from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('cart',views.cart,name='cart'),
    path('viewcart',views.viewcart,name='viewcart'),
    path('golog',views.golog,name='golog'),
    path('goreg',views.goreg,name='goreg'),
    path('login',views.login,name='golog'),
    path('reg',views.reg,name='goreg'),
    path('logout',views.logout,name='logout'),
    path('category',views.category,name='category'),
    path('products/<int:id>',views.products,name='products'),
    path('delete/<int:id>',views.delete,name='delete'),
]
