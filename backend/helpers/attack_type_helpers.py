from backend.enums.EffectivenessEnum import Effectiveness
from backend.enums.TypeEnum import Type


def handle_grass_attack_type(pokemon_type: Type) -> Effectiveness:
    return grass_type_effectiveness_mapper[pokemon_type]


def handle_water_attack_type(pokemon_type: Type) -> Effectiveness:
    return water_type_effectiveness_mapper[pokemon_type]


def handle_fire_attack_type(pokemon_type: Type) -> Effectiveness:
    return fire_type_effectiveness_mapper[pokemon_type]


def handle_normal_attack_type(pokemon_type: Type) -> Effectiveness:
    return normal_type_effectiveness_mapper[pokemon_type]


def determine_effectiveness(attack_type: Type, pokemon_type: Type) -> None | Effectiveness:
    if not attack_type or not pokemon_type:
        return
    
    for mapper_attack_type, attack_handler in attack_type_handler_mapper.items():
        if attack_type == mapper_attack_type:
            return attack_handler(pokemon_type)


grass_type_effectiveness_mapper = {
    Type.FIRE: Effectiveness.NOT_VERY_EFFECTIVE,
    Type.WATER: Effectiveness.SUPER_EFFECTIVE,
    Type.GRASS: Effectiveness.NOT_VERY_EFFECTIVE,
    Type.NORMAL: Effectiveness.EFFECTIVE
}

fire_type_effectiveness_mapper = {
    Type.WATER: Effectiveness.NOT_VERY_EFFECTIVE,
    Type.GRASS: Effectiveness.SUPER_EFFECTIVE,
    Type.FIRE: Effectiveness.NOT_VERY_EFFECTIVE,
    Type.NORMAL: Effectiveness.EFFECTIVE
}

water_type_effectiveness_mapper = {
    Type.GRASS: Effectiveness.NOT_VERY_EFFECTIVE,
    Type.FIRE: Effectiveness.SUPER_EFFECTIVE,
    Type.WATER: Effectiveness.NOT_VERY_EFFECTIVE,
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
