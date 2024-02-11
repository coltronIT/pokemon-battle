from enum import StrEnum


class Question(StrEnum):
    ATTACK_TYPE = 'What attack type do you want your pokemon to use? (type q to exit): '
    POKEMON_TYPE = 'What type of pokemon do you want to battle? (type q to exit): '
