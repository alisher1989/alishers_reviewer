from django.urls import path
from webapp.views import ProductsView, ProductView, ProductCreateView, ProductUpdateView, ProductDeleteView, \
    ReviewsView, ReviewCreateView, ReviewUpdateView, ReviewDeleteView

urlpatterns = [
    path('', ProductsView.as_view(), name='products_view'),
    path('product/<int:pk>/', ProductView.as_view(), name='product_view'),
    path('product/add/', ProductCreateView.as_view(), name='product_add'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('reviews/', ReviewsView.as_view(), name='reviews_view'),
    path('review/add-product/<int:pk>/', ReviewCreateView.as_view(), name='review_add'),
    path('product/<int:pk>/update-review/', ReviewUpdateView.as_view(), name='review_update'),
    path('product/<int:pk>/delete-review/', ReviewDeleteView.as_view(), name='review_delete'),

]

app_name = 'webapp'