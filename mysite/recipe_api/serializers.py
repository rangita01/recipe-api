from rest_framework import serializers
from . import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('id', 'username','email','first_name','last_name','password')

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Recipe
        fields = ('id', 'user','name')

class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Step
        fields = ('id', 'recipe', 'step_text')

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ingredient
        fields = ('id', 'recipe', 'ingredient')
