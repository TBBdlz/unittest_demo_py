import random


class User:
    def __init__(self, name: str, email: str) -> None:
        # Generate user_id as random number
        self.user_id = random.randint(1000000, 10000000)
        self.name = name
        self._email = email

    def _get_email(self) -> str:
        return self._email

    def _set_email(self, new_email: str) -> None:
        self._email = new_email


class Player(User):
    def __init__(self, name: str, email: str, start_class: str) -> None:
        # Initialize the parent class
        super().__init__(name, email)
        self.game_class = start_class
        self.level = 1

    def __str__(self) -> str:
        return (
            f"Player(user_id={self.user_id}, name={self.name}, email={self._email}, "
            f"game_class={self.game_class}, level={self.level})"
        )

    def level_up(self, step: int = 1) -> None:
        self.level += step
