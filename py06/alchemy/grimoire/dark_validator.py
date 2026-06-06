from .dark_spellbook import darl_spell_allowed_ingredients


def validate_ingredients(ingredients: str):
    result = "INVALID"
    for ingredient in darl_spell_allowed_ingredients():
        if ingredient in ingredients:
            result = "VALID"
    return f"{ingredients} {result}"
