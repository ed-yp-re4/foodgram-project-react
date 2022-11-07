from django.contrib import admin
from recipes.models import (Recipe, RecipeIngredientAmount, RecipeTag,
                            UserFavoriteRecipe, UserShoppingCart)


class TagInline(admin.TabularInline):

    model = RecipeTag
    extra = 3


class IngredientInline(admin.TabularInline):

    model = RecipeIngredientAmount
    extra = 3


class RecipeAdmin(admin.ModelAdmin):

    inlines = (TagInline, IngredientInline,)
    list_display = ('pk', 'author', 'name', 'text', 'cooking_time', 'image',)
    list_editable = ('author', 'name', 'text', 'cooking_time', 'image',)
    list_filter = ('tags__name',)


class RecipeTagAdmin(admin.ModelAdmin):

    list_display = ('pk', 'recipe', 'tag',)
    list_editable = ('recipe', 'tag',)
    list_filter = ('tag',)


class RecipeIngredientAmountAdmin(admin.ModelAdmin):

    list_display = ('pk', 'recipe', 'ingredient', 'amount',)
    list_editable = ('recipe', 'ingredient', 'amount',)
    search_fields = (
        'recipe__name',
        'recipe__author__email',
        'recipe__author__username',
    )
    raw_id_fields = ('ingredient', 'recipe')


class UserFavoriteRecipeAdmin(admin.ModelAdmin):

    list_display = ('pk', 'user', 'recipe',)
    list_editable = ('user', 'recipe',)
    search_fields = (
        'recipe__name',
        'recipe__author__email',
        'recipe__author__username',
    )


class UserShoppingCartAdmin(admin.ModelAdmin):

    list_display = ('pk', 'user', 'recipe',)
    list_editable = ('user', 'recipe',)
    search_fields = (
        'recipe__name',
        'recipe__author__email',
        'recipe__author__username',
    )


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeTag, RecipeTagAdmin)
admin.site.register(RecipeIngredientAmount, RecipeIngredientAmountAdmin)
admin.site.register(UserFavoriteRecipe, UserFavoriteRecipeAdmin)
admin.site.register(UserShoppingCart, UserShoppingCartAdmin)
