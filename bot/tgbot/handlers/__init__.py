from .commands import register_commands
from .subscribes import register_subscribes
from .other import register_other

register_functions = (
    register_commands,
    register_subscribes,
    register_other,
)
