from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

class Recipe(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

class Step(models.Model):
    recipe = models.ForeignKey(Recipe,on_delete=models.CASCADE)
    step_text = models.TextField(null=True)

class Ingredient(models.Model):
    receipe = models.ForeignKey(Recipe,on_delete=models.CASCADE)
    ingredient = models.TextField(null=True)
