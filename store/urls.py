from django.urls import include, path
from .views import (UserProfileViewSet, CategoryViewSet, SubCategoryViewSet,
                    ProductViewSet, ProductImageViewSet,
                    ReviewViewSet, CartViewSet, CartItemViewSet,

)
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', UserProfileViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'subcategories', SubCategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'images', ProductImageViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'cart', CartViewSet)
router.register(r'cart item', CartItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]