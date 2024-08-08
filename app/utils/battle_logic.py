import math

def calculate_damage(attacker: dict, defender: dict) -> float:
    type1_damage = attacker['attack'] / 200 * 100 - (defender[f"against_{attacker['type1']}"] / 4 * 100)
    type2_damage = attacker['type2'] and attacker['attack'] / 200 * 100 - (defender[f"against_{attacker['type2']}"] / 4 * 100) or 0
    
    # Ensure damage is a finite number
    if math.isinf(type1_damage) or math.isnan(type1_damage):
        type1_damage = 0
    if math.isinf(type2_damage) or math.isnan(type2_damage):
        type2_damage = 0
    
    return max(type1_damage, type2_damage)

def battle(pokemon_a: dict, pokemon_b: dict) -> dict:
    damage_to_b = calculate_damage(pokemon_a, pokemon_b)
    damage_to_a = calculate_damage(pokemon_b, pokemon_a)
    
    # Ensure damages are finite numbers
    if math.isinf(damage_to_b) or math.isnan(damage_to_b):
        damage_to_b = 0
    if math.isinf(damage_to_a) or math.isnan(damage_to_a):
        damage_to_a = 0
    
    if damage_to_b > damage_to_a:
        return {"winner": pokemon_a['name'], "won_by": damage_to_b}
    elif damage_to_a > damage_to_b:
        return {"winner": pokemon_b['name'], "won_by": damage_to_a}
    else:
        return {"winner": "draw", "won_by": 0}
