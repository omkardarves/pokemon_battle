# Pokémon Battle Simulator

## Description
A Pokémon Battle Simulator built with FastAPI.

## Setup

1. **Clone the repository**:
    ```sh
    git clone <repository-url>
    cd pokemon_battle_simulator
    ```

2. **Create and activate a virtual environment**:
    ```sh
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Run the application**:
    ```sh
    uvicorn app.main:app --reload
    ```

5. **Run the tests**:
    ```sh
    pytest --cov=app tests/
    ```

## APIs

### Listing API
- **URL**: `/api/pokemons/`
- **Method**: `GET`
- **Parameters**: 
  - `page`: Page number (default: 1)
  - `size`: Page size (default: 10)

### Battle API
- **URL**: `/api/battle/`
- **Method**: `POST`
- **Body**:
    ```json
    {
      "pokemon_a": "Bulbasaur",
      "pokemon_b": "Charmander"
    }
    ```

### Status API
- **URL**: `/api/status/{battle_id}`
- **Method**: `GET`

## OpenAPI Schema
You can access the OpenAPI schema at `/docs` once the server is running.

## Postman Collection
Include a Postman collection if available.


## UML Diagram
                            +-----------------+
                            |  Pokemon        |
                            +-----------------+
                            |  - name         |
                            |  - type1        |
                            |  - type2        |
                            |  - attack       |
                            +-----------------+
                                   ^
                                   |
                            +-----------------+
                            |  BattleLogic    |
                            +-----------------+
                |  + calculate_damage(pokemon_a, pokemon_b) |
                            +-----------------+

                            +-----------------+
                            |  BattleAPI      |
                            +-----------------+
                |  + start_battle(pokemon_a, pokemon_b)     |
                |  + get_battle_status(battle_id)           |
                            +-----------------+
                                   ^
                                   |
                            +-----------------+
                            |  StatusAPI      |
                            +-----------------+
                |       + get_status(battle_id)             |
                            +-----------------+

                            +-----------------+
                            |  ListingAPI     |
                            +-----------------+
                |       + list_pokemons(page, size)         |
                            +-----------------+

                            +-----------------+
                            |  DataLoader     |
                            +-----------------+
                |       + load_data(filepath)               |
                            +-----------------+

                            +-----------------+
                            |  SpellChecker   |
                            +-----------------+
                |       + check_spelling(name)              |
                            +-----------------+
