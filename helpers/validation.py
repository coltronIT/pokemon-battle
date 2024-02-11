from enums.TypeEnum import Type


def verify_type_from_response(unsanitized_reponse: str) -> bool:
    try:
        return bool(Type(unsanitized_reponse))
    except ValueError:
        return False


def determine_quit_response(response: str) -> bool:
    return response == 'q'
