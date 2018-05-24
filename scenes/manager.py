class SceneManager(object):
    def __init__(self, director, scenes=None):
        """
        A Manager to control the flow of scenes.
        :param director: The main loop director.
        :param scenes: The scenes to display in order.
        """
        self.director = director
        self.scenes = scenes or []
        self.current_index = None
        for scene in self.scenes:
            scene.manager = self
        self.callbacks = {}

    @property
    def initial_scene(self):
        return self.scenes[0]

    def register_transition_callback(self, scene, callback, **kwargs):
        """
        Allows to call code when transitioning to a scene
        :param scene: The Scene to listen for
        :param callback: The code to call
        :param kwargs: Additional kwargs to use when calling
        """
        if scene in self.callbacks:
            self.callbacks.append((callback, kwargs))
        else:
            self.callbacks[scene] = [(callback, kwargs)]

    def next(self):
        if self.current_index is None:
            self.current_index = 0
        else:
            self.current_index += 1

        if not self.current_index > len(self.scenes):
            next_scene = self.scenes[self.current_index]
            self.transition_callback(next_scene)
            self.director.replace_scene(next_scene)

    def previous(self):
        if self.current_index is None:
            self.current_index = 0
        else:
            self.current_index -= 1

        if not self.current_index <= 0:
            next_scene = self.scenes[self.current_index]
            self.transition_callback(next_scene)
            self.director.replace_scene(next_scene)

    def transition_callback(self, scene):
        callbacks = self.callbacks.get(scene)
        if callbacks:
            for callback, kwargs in callbacks:
                callback(**kwargs)
