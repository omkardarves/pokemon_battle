from fastapi import APIRouter, BackgroundTasks
from uuid import uuid4
from app.utils.battle_logic import battle
from app.utils.data_loader import load_data
from app.utils.spell_checker import correct_spelling
from app.state import battles

router = APIRouter()

data = load_data("/home/dell/Fastapi-dir/pokemon_battle_simulator/dataset/pokemon.csv")
pokemon_names = data['name'].tolist()

@router.post("/battle/")
async def start_battle(pokemon_a: str, pokemon_b: str, background_tasks: BackgroundTasks):
    battle_id = str(uuid4())
    pokemon_a = correct_spelling(pokemon_a, pokemon_names)
    pokemon_b = correct_spelling(pokemon_b, pokemon_names)
    background_tasks.add_task(run_battle, battle_id, pokemon_a, pokemon_b)
    return {"battle_id": battle_id}

def run_battle(battle_id: str, pokemon_a: str, pokemon_b: str):
    pokemon_a_data = data[data['name'] == pokemon_a].to_dict('records')[0]
    pokemon_b_data = data[data['name'] == pokemon_b].to_dict('records')[0]
    result = battle(pokemon_a_data, pokemon_b_data)
    battles[battle_id] = result
