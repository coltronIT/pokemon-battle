import pytest

from backend.helpers.attack_type_helpers import (
    handle_grass_attack_type,
    handle_water_attack_type,
    handle_fire_attack_type,
    handle_normal_attack_type,
)

@pytest.mark.parametrize(
    'pokemon_type, expected_outcome',
    [
        ('grass', 'Not Very Effective'),
        ('water', 'Super Effective'),
        ('fire', 'Not Very Effective'),
        ('normal', 'Effective')
    ]
)
def test_grass_attack_type(pokemon_type, expected_outcome):
    assert handle_grass_attack_type(pokemon_type) == expected_outcome


@pytest.mark.parametrize(
    'pokemon_type, expected_outcome',
    [
        ('grass', 'Not Very Effective'),
        ('water', 'Not Very Effective'),
        ('fire', 'Super Effective'),
        ('normal', 'Effective')
    ]
)
def test_water_attack_type(pokemon_type, expected_outcome):
    assert handle_water_attack_type(pokemon_type) == expected_outcome

