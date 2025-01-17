from .nodes import (
    agenticflow_ai_variable,
    io,
)

NODE_CLASS_MAPPINGS = {
    **agenticflow_ai_variable.NODE_CLASS_MAPPINGS,
    **io.NODE_CLASS_MAPPINGS,
}
