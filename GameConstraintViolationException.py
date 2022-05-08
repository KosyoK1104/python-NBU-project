class GameConstraintViolationException(RuntimeError):
    def __init__(self, message):
        super().__init__(message)

    @staticmethod
    def invalid_enemy_type():
        return GameConstraintViolationException('The enemy type is not valid!')
