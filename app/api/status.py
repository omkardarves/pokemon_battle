from fastapi import APIRouter
from state import battles
import math

router = APIRouter()

@router.get("/status/{battle_id}")
async def get_battle_status(battle_id: str):
    if battle_id in battles:
        result = battles[battle_id]
        
        # Ensure all response values are JSON compliant
        if 'won_by' in result and (math.isinf(result['won_by']) or math.isnan(result['won_by'])):
            result['won_by'] = 0
        
        return {"status": "BATTLE_COMPLETED", "result": result}
    
    return {"status": "BATTLE_INPROGRESS", "result": None}
