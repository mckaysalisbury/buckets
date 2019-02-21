from enums import BaseAction, Target

class Action:
    def __init__(self, base: BaseAction, target: Target):
        self.base = base
        self.target = target


    def __str__(self) -> str:
        if self.base in [BaseAction.Empty, BaseAction.Fill]:
            return f"{self.base.name} the {self.target.name} bucket."
        if self.base == BaseAction.Transfer:
            return f"Transfer the contents of the {self.target.other().name} bucket into the {self.target.name} bucket (but don't overfill)"
        raise NotImplementedError()
    
