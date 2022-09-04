class AcquisitionWrongType(Exception):
    def __init__(self):
        if self.args:
            self.message = self.args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f"Aquisitions are only used for base ingredients to add useful descriptions to how to get the item. Otherwise, for calculated entries use recipe adders. {self.message}"
        else:
            return f"Aquisitions are only used for base ingredients to add useful descriptions to how to get the item. Otherwise, for calculated entries use recipe adders."
