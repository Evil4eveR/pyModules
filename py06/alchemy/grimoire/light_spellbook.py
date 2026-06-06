

def light_spell_allowed_ingredients():
    return ["earth", "fire", "air", "water"]


def light_spell_record(spell_name: str, ingredients: str):
    validate_result = validate_ingredients(ingredients)
    print(validate_result)
    if "INVALID" in validate_result:
        return "Spell rejected!"
    return f"Spell recorded: {spell_name} ({ingredients})"


from .light_validator import validate_ingredients