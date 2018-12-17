from core.ai.shorttermstate import ShortTermState
from core.components import listing, Component


@listing.register
class AI(Component):
    NAME = 'ai'
    __slots__ = ["last_behavior", "personality"]

    # TODO Think about this structure, is it worth to keep the states out
    # TODO of the Personality?

    def __init__(self, personality):
        super().__init__()
        self.short_term_state = ShortTermState()
        self.last_behavior = None
        self.personality = personality

    def round_update(self):
        host_health = self.host.health
        if host_health:
            if not host_health.conscious or host_health.dead:
                return

        behavior = self.personality.get_behavior(
            self.host, self.last_behavior, self.short_term_state)
        if behavior:
            behavior.execute()
            if not behavior.finished:
                self.last_behavior = behavior

    def copy(self):
        return AI(self.personality.copy())
