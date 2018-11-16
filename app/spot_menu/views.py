from rest_framework import viewsets

from .models import Spot, Dish, DishModifier, Category
from .serializers import SpotSerializer, DishSerializer, DishModifierSerializer, CategoriesSerializer


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoriesSerializer


class DishView(viewsets.ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    
    def get_queryset(self, *args, **kwargs):
        spot_pk = self.kwargs.get('spot_pk')
        dishes = super().get_queryset().filter(spot=spot_pk)
        return dishes
    
    def perform_create(self, serializer):
        spot_pk = self.kwargs.get('spot_pk')
        serializer.instance = Dish(spot_id=spot_pk)
        super().perform_create(serializer)


class DishModifiersView(viewsets.ModelViewSet):
    queryset = DishModifier.objects.all()
    serializer_class = DishModifierSerializer
    
    def get_queryset(self, *args, **kwargs):
        dish_pk = self.kwargs.get('dish_pk')
        return DishModifier.objects.filter(dish=dish_pk)
    
    def perform_create(self, serializer):
        dish_pk = self.kwargs.get('dish_pk')
        serializer.instance = DishModifier(dish_id=dish_pk)
        super().perform_create(serializer)


class SpotView(viewsets.ModelViewSet):
    queryset = Spot.objects.all()
    serializer_class = SpotSerializer
