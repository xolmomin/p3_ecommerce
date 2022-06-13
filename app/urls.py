from django.urls import path

from app.views import index, product_details, order_list, customers, order_details, add_product, customer_details, \
    customer_add, customer_delete, customer_update, category, login_page, register_page, logout_page

urlpatterns = [
    path('', index, name='index'),
    path('add-product/', add_product, name='add_product'),
    # path('test/<int:year>/<int:month>/<int:day>', testing, name='testing'),
    path('product-details/<int:product_id>', product_details, name='product_details'),
    path('order-list/', order_list),
    path('order-details/', order_details),

    path('category/', category, name='category'),
    path('category/<str:category_slug>', index, name='category_by_slug'),
    path('customers/', customers, name='customers'),
    path('customer-details/<int:customer_id>', customer_details, name='customer_details'),
    path('customer-add/', customer_add, name='customer_add'),
    path('customer-update/<int:customer_id>', customer_update, name='customer_update'),
    path('customer-delete/<int:customer_id>', customer_delete, name='customer_delete'),

    path('login/', login_page, name='login_page'),
    path('logout/', logout_page, name='logout_page'),
    path('register/', register_page, name='register_page'),
]
