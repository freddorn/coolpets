from django.urls import path
from .views import (
    AllProductsView,
    AllProductsPriceHighView,
    AllProductsPriceLowView,
    ListingDetailView,
    leashes_category_view,
    collars_category_view,
    beds_category_view,
    carriers_category_view,
    feeding_category_view,
    harnesses_category_view,
    toys_category_view,
    categories_view
)

urlpatterns = [
    path('listing/<int:pk>/', ListingDetailView.as_view(),
         name="listing-detail"),
    path('categories/', categories_view, name="categories"),
    path('all-products/', AllProductsView.as_view(), name="all-products"),
    path('all-products/price-high/', AllProductsPriceHighView.as_view(),
         name="all-products-price-high"),
    path('all-products/price-low/', AllProductsPriceLowView.as_view(),
         name="all-products-price-low"),
    path('categories/leashes', leashes_category_view, name="leashes"),
    path('categories/collars', collars_category_view, name="collars"),
    path('categories/beds', beds_category_view, name="beds"),
    path('categories/carriers', carriers_category_view, name="carriers"),
    path('categories/feeding', feeding_category_view, name="feeding"),
    path('categories/harnesses', harnesses_category_view, name="harnesses"),
    path('categories/toys', toys_category_view, name="toys"),
]
