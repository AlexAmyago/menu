from django.conf.urls import url, include
from rest_framework_nested import routers

from .views import DishView, DishModifiersView, CategoryView, SpotView

router = routers.DefaultRouter()

router.register(r'restaurants', SpotView, base_name='spots')
router.register(r'categories', CategoryView, base_name='Categories')

dishes_router = routers.NestedSimpleRouter(router, r'restaurants', lookup='spot')
dishes_router.register(r'dish', DishView, base_name='dish')

dishes_modifier_router = routers.NestedSimpleRouter(dishes_router, r'dish', lookup='dish')
dishes_modifier_router.register(r'modifiers', DishModifiersView, base_name='dish_modifiers')

categories_router = routers.NestedSimpleRouter(dishes_router, r'dish', lookup='dish')
categories_router.register(r'categories', DishModifiersView, base_name='categories')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include(dishes_router.urls)),
    url(r'^', include(dishes_modifier_router.urls)),
    url(r'^', include(categories_router.urls)),
]
