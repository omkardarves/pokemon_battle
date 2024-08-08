from fastapi import APIRouter, HTTPException
from app.utils.data_loader import load_data
import math

router = APIRouter()

data = load_data("/home/dell/Fastapi-dir/pokemon_battle_simulator/dataset/pokemon.csv")

@router.get("/pokemons/")
async def list_pokemons(page: int = 1, size: int = 10):
    if page < 1 or size < 1:
        raise HTTPException(status_code=400, detail="Page and size must be positive integers.")
    
    start_index = (page - 1) * size
    end_index = start_index + size
    
    paginated_data = data.iloc[start_index:end_index].to_dict(orient="records")
    
    # Ensure all response values are JSON compliant
    for pokemon in paginated_data:
        for key, value in pokemon.items():
            if isinstance(value, float) and (math.isinf(value) or math.isnan(value)):
                pokemon[key] = 0
    
    return {"page": page, "size": size, "total": len(data), "data": paginated_data}
