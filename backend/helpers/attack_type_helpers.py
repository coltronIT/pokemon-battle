from backend.enums.EffectivenessEnum import Effectiveness
from backend.enums.TypeEnum import Type


def handle_attack_type_from_mapper(
    pokemon_type: Type,
    type_effectiveness_mapper: dict[Type, Effectiveness]
) -> Effectiveness:
    for mapper_pokemon_type, effectiveness in type_effectiveness_mapper.items():
        if pokemon_type == mapper_pokemon_type:
            return effectiveness


def handle_grass_attack_type(pokemon_type: Type) -> Effectiveness:
    return handle_attack_type_from_mapper(pokemon_type, grass_type_effectiveness_mapper)


def handle_water_attack_type(pokemon_type: Type) -> Effectiveness:
    return handle_attack_type_from_mapper(pokemon_type, water_type_effectiveness_mapper)


def handle_fire_attack_type(pokemon_type: Type) -> Effectiveness:
    return handle_attack_type_from_mapper(pokemon_type, fire_type_effectiveness_mapper)


def handle_normal_attack_type(pokemon_type: Type) -> Effectiveness:
    return handle_attack_type_from_mapper(pokemon_type, normal_type_effectiveness_mapper)


def determine_effectiveness(attack_type: Type, pokemon_type: Type) -> None | Effectiveness:
    if not attack_type or not pokemon_type:
        return
    
    for mapper_attack_type, attack_handler in attack_type_handler_mapper.items():
        if attack_type == mapper_attack_type:
            return attack_handler(pokemon_type)

grass_type_effectiveness_mapper = {
    Type.FIRE: Effectiveness.NOT_VERY_EFFECTIVE,
    Type.WATER: Effectiveness.SUPER_EFFECTIVE,
    Type.GRASS: Effectiveness.EFFECTIVE,
    Type.NORMAL: Effectiveness.EFFECTIVE
}

fire_type_effectiveness_mapper = {
    Type.WATER: Effectiveness.NOT_VERY_EFFECTIVE,
    Type.GRASS: Effectiveness.SUPER_EFFECTIVE,
    Type.FIRE: Effectiveness.EFFECTIVE,
    Type.NORMAL: Effectiveness.EFFECTIVE
}

water_type_effectiveness_mapper = {
    Type.GRASS: Effectiveness.NOT_VERY_EFFECTIVE,
    Type.FIRE: Effectiveness.SUPER_EFFECTIVE,
    Type.WATER: Effectiveness.EFFECTIVE,
    Type.NORMAL: Effectiveness.EFFECTIVE
}

normal_type_effectiveness_mapper = {
    Type.GRASS: Effectiveness.EFFECTIVE,
    Type.FIRE: Effectiveness.EFFECTIVE,
    Type.WATER: Effectiveness.EFFECTIVE,
    Type.NORMAL: Effectiveness.EFFECTIVE
}

attack_type_handler_mapper = {
    Type.GRASS: handle_grass_attack_type,
    Type.FIRE: handle_fire_attack_type,
    Type.WATER: handle_water_attack_type,
    Type.NORMAL: handle_normal_attack_type
}
