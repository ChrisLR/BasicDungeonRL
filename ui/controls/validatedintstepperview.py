from clubsandwich.ui import IntStepperView


class ValidatedIntStepperView(IntStepperView):
    """ Similar to an Int Stepper View but does a validation callback. """
    def __init__(self, validation_callback, value, callback, min_value=None, max_value=None, *args, **kwargs):
        self.validation_callback = validation_callback
        super().__init__(value, callback, min_value, max_value, *args, **kwargs)

    @property
    def value(self):
        return int(self.label_view.text)

    @value.setter
    def value(self, new_value):
        if self.validation_callback(self.value, new_value):
            self.label_view.text = str(new_value)
            if self.superview:
                self.superview.set_needs_layout()
