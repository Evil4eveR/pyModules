

def validate_ingredients(ingredients: str):
    result = "INVALID"
    for ingredient in light_spell_allowed_ingredients():
        if ingredient in ingredients:
            result = "VALID"
    return f"{ingredients} {result}"

from .light_spellbook import light_spell_allowed_ingredients
