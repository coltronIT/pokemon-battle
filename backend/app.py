from fastapi import (
    FastAPI,
    HTTPException,
)
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from backend.enums.ErrorMessageEnum import ErrorMessage
from backend.helpers.attack_type_helpers import determine_effectiveness
from backend.helpers.validation import verify_type_from_response

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")


class GameInput(BaseModel):
    attack_type: str
    pokemon_type: str


@app.post("/play/")
async def play_game(game_input: GameInput):
    if not verify_type_from_response(game_input.attack_type) or not verify_type_from_response(game_input.pokemon_type):
        raise HTTPException(status_code=400, detail=ErrorMessage.NOT_VALID_TYPE.value)

    effectiveness = determine_effectiveness(attack_type=game_input.attack_type, pokemon_type=game_input.pokemon_type)
    return {"effectiveness": effectiveness}