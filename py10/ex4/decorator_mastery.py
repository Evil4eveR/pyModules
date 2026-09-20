import inspect
import time
from collections.abc import Callable
from functools import wraps


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> str:
        print(f"Casting {func.__name__}...")
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f'Spell completed in {execution_time:.3f} seconds')
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    def actual_decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> str:
            bound = inspect.signature(func).bind(*args, **kwargs)
            power = bound.arguments["power"]
            if power < min_power:
                return "Insufficient power for this spell"
            result = func(*args, **kwargs)
            return result
        return wrapper
    return actual_decorator


def retry_spell(max_attempts: int) -> Callable:
    def actual_decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> str:
            for i in range(max_attempts):
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception:
                    if i + 1 < max_attempts:
                        print(
                            f"Spell failed, retrying..."
                            f" (attempt {i}/{max_attempts})"
                            )
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return actual_decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return (
            len(name) >= 3
            and all(c.isalpha() or c == " " for c in name)
        )

    @power_validator(min_power=30)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:
    print('Testing spell timer...')

    @spell_timer
    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target} for {power} damage"

    print(f"Result: {fireball('Dragon', 50)}")

    print('Testing power validator...')

    def heal(target: str, power: int) -> str:
        return f"Heal restores {target} for {power} HP"

    print(f"Invalid result: {heal('Dragon', 10)}")
    print(f"Valid result: {heal('Dragon', 100)}")

    print('Testing retry spell validator...')

    @retry_spell(5)
    def lightning(target: str, power: int) -> str:
        raise ValueError("spell blew up")

    print(f"Error testing: {lightning('Dragon', 10)}")

    print('Testing retry spell validator...')
    mageg = MageGuild()
    print(mageg.validate_mage_name("Ember"))
    print(mageg.validate_mage_name("Ember@#"))
    print(mageg.cast_spell('Dragon', 40))
    print(mageg.cast_spell('Dragon', 20))


if __name__ == "__main__":
    main()
