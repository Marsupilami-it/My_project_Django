from django.urls import path

import adminapp.views as adminapp

app_name = 'adminapp'

urlpatterns = [
    # ShopUser
    path('', adminapp.ShopUserList.as_view(), name='index'),
    path('user/create/', adminapp.ShopUserCreateView.as_view(), name='user_create'),
    path('user/delete/<int:user_pk>/', adminapp.ShopUserDeleteView.as_view(), name='user_delete'),
    path('user/update/<int:user_pk>/', adminapp.ShopUserUpdateView.as_view(), name='user_update'),

    # MotoCategory
    path('categories/', adminapp.categories, name='categories'),
    path('category/create/', adminapp.MotoCategoryCreateView.as_view(), name='category_create'),
    path('category/update/<int:pk>/', adminapp.MotoCategoryUpdateView.as_view(), name='category_update'),
    path('category/<int:pk>/products/', adminapp.category_products, name='category_products'),
    path('product/<int:pk>/', adminapp.MotoDetail.as_view(), name='moto_detail'),
    path('category/<int:pk>/product/create/', adminapp.product_create, name='product_create'),
]