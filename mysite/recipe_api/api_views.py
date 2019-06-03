from rest_framework import viewsets
from . import models
from . import serializers

class UserViewset(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer

class RecipeViewset(viewsets.ModelViewSet):
    queryset = models.Recipe.objects.all()
    serializer_class = serializers.RecipeSerializer

class StepViewset(viewsets.ModelViewSet):
    queryset = models.Step.objects.all()
    serializer_class = serializers.StepSerializer

class IngredientViewset(viewsets.ModelViewSet):
    queryset = models.Ingredient.objects.all()
    serializer_class = serializers.IngredientSerializer
