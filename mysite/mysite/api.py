from rest_framework import routers
from recipe_api import api_views as myapp_views

router = routers.DefaultRouter()
router.register(r'user', myapp_views.UserViewset)
router.register(r'recipe', myapp_views.RecipeViewset)
router.register(r'step', myapp_views.StepViewset)
router.register(r'ingredient', myapp_views.IngredientViewset)
