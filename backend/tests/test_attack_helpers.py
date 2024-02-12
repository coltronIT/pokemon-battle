from backend.helpers.attack_type_helpers import handle_attack_type_from_mapper


def test_handle_attack_type_from_mapper_for_grass_type():
    pokemon_type = 'grass'
    type_effectiveness_mapper = {
        'grass': 'Not Very Effective',
        'water': 'Super Effective',
        'fire': 'Not Very Effective',
    }
    expected_outcome = 'Not Very Effective'
    result = handle_attack_type_from_mapper(pokemon_type, type_effectiveness_mapper)

    assert result == expected_outcome

def test_handle_attack_type_from_mapper_for_water_type():
    pokemon_type = 'water'
    type_effectiveness_mapper = {
        'grass': 'Not Very Effective',
        'water': 'Super Effective',
        'fire': 'Not Very Effective',
    }
    expected_outcome = 'Super Effective'
    result = handle_attack_type_from_mapper(pokemon_type, type_effectiveness_mapper)

    assert result == expected_outcome
