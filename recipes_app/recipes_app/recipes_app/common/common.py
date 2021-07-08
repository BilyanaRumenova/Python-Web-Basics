class DisabledFormMixin():
    def __init__(self):
        for (_, field) in self.fields.items():
            field.widget.attrs['readonly'] = True
            field.widget.attrs['disabled'] = True