from enums.ConsoleMessageEnum import ConsoleMessage
from enums.ErrorMessageEnum import ErrorMessage
from enums.ProgramStatusEnum import ProgramStatus
from enums.QuestionEnum import Question
from helpers.attack_type_helpers import determine_effectiveness
from helpers.validation import (
    determine_quit_response,
    verify_type_from_response,
)

class MainProgram:
    def __init__(self):
        self.program_status = ProgramStatus.RUN
        self.questions = [
            ('attack_type', Question.ATTACK_TYPE),
            ('pokemon_type', Question.POKEMON_TYPE)
        ]


    def main(self):
        is_valid_type = True

        while self.program_status == ProgramStatus.RUN:
            type_responses = {}

            for key, prompt in self.questions:
                response = input(prompt).lower()

                if determine_quit_response(response):
                    self.program_status = ProgramStatus.STOP
                    break

                if not verify_type_from_response(response):
                    print(ErrorMessage.NOT_VALID_TYPE)
                    break

                type_responses[key] = response

            if not is_valid_type:
                continue

            if len(type_responses) == len(self.questions):
                print(determine_effectiveness(**type_responses))

        print(ConsoleMessage.END_OF_PROGRAM)

program = MainProgram()
program.main()
