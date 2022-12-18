from .commands import register_commands
from .subscribes import register_subscribes
from .survey import register_survey
from .other import register_other

register_functions = (
    register_commands,
    register_subscribes,
    register_survey,
    register_other,
)
