from rest_framework import serializers

from .models import Spot, Dish, DishModifier, Category


class SpotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spot
        fields = ('id', 'name', 'details', 'location')
        read_only_fields = ('created_at',)


class DishModifierNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = DishModifier
        fields = ('id', 'parent', 'name', 'details')
        read_only_fields = ('created_at',)


class DishModifierSerializer(serializers.ModelSerializer):
    extra = serializers.SerializerMethodField()
    
    class Meta:
        model = DishModifier
        fields = ('id', 'name', 'details', 'extra')
        read_only_fields = ('created_at',)
    
    def get_extra(self, parent):
        qs = parent.get_children()
        serialized_data = DishModifierNestedSerializer(qs, many=True, read_only=False, context=self.context)
        return serialized_data.data


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')
        read_only_fields = ('created_at',)


class DishSerializer(serializers.ModelSerializer):
    dish_modifiers = DishModifierSerializer(many=True, read_only=False, required=False)
    category = CategoriesSerializer(many=True, read_only=False, required=False)
    
    class Meta:
        model = Dish
        fields = ('id', 'name', 'details','cost', 'dish_modifiers', 'category')
        read_only_fields = ('created_at',)

