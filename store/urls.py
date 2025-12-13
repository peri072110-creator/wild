from django.urls import include, path
from rest_framework import routers
from .views import (
    UserProfileViewSet, SubCategoryDetailAPIView,
    ReviewViewSet, CartViewSet, CartItemViewSet,
    CategoryListAPIView, ProductImageViewSet,
    SubCategoryListAPIView, CategoryDetailAPIView,
    ProductDetailView, ProductListView,
    RegisterView, LoginView, LogoutView
)














router = routers.DefaultRouter()
router.register(r'users', UserProfileViewSet)
router.register(r'images', ProductImageViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'cart', CartViewSet)
router.register(r'cart-item', CartItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('category/', CategoryListAPIView.as_view(), name='category-list'),
    path('category/<int:pk>/', CategoryDetailAPIView.as_view(), name='category-detail'),
    path('subcategory/', SubCategoryListAPIView.as_view(), name='subcategory-list'),
    path('subcategory/<int:pk>/', SubCategoryDetailAPIView.as_view(), name='subcategory-detail'),
    path('product/', ProductListView.as_view(), name='product-list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

]
