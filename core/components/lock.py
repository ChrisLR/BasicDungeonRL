from core.components.base import Component


class Lock(Component):
    NAME = "lock"
    __slots__ = ["locked", "key"]

    def __init__(self, locked=True, key=None):
        super().__init__()
        self.locked = locked
        self.key = key
        self.failed_attempts = {}

    def unlock(self):
        self.locked = False

    def lock(self):
        self.locked = True

    def add_failed_attempt(self, character, level):
        """ Attempts to pick can only be made once per level. """
        self.failed_attempts[character] = level

    def has_failed(self, character):
        attempt = self.failed_attempts.get(character)
        if attempt is None:
            return False

        if character.experience.level == attempt:
            return True

        return False

    def copy(self):
        return Lock(self.locked, self.key)

