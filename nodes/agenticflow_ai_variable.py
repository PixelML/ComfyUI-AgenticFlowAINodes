import numpy as np
import torch


class AgenticflowAIVariable:
    """A node that handles variable values and provides type conversions.

    This node takes a variable input and a fallback value, attempting to convert the input
    into multiple data types (string, integer, and float). If the variable is empty or
    wrapped in curly braces (indicating an unresolved variable), it uses the fallback value.

    Attributes:
        INPUT_TYPES: Defines the input parameters - variable and fallback string
        RETURN_TYPES: Returns the value as (string, integer, float) tuple
        FUNCTION: The main processing function name
        CATEGORY: Node category in the ComfyUI interface
    """

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "variable": (
                    [
                        "",
                    ],
                ),
                "fallback": (
                    "STRING",
                    {
                        "default": "",
                        "single_line": True,
                    },
                ),
            }
        }

    RETURN_TYPES = ("STRING", "INT", "FLOAT")
    FUNCTION = "do_it"

    CATEGORY = "agenticflowai/variables"

    # @classmethod
    # def VALIDATE_INPUTS(cls, variable: str, fallback: str):
    #     # Since we populate dynamically, comfy will report invalid inputs. Override to always return True
    #     return True

    def do_it(self, variable: str, fallback: str):
        variable = variable.strip()
        fallback = fallback.strip()
        if variable == "" or (variable.startswith("{") and variable.endswith("}")):
            variable = fallback

        int_val = 0
        float_val = 0.0
        string_val = f"{variable}"
        try:
            int_val = int(variable)
        except Exception as _:
            pass
        try:
            float_val = float(variable)
        except Exception as _:
            pass
        return (string_val, int_val, float_val)


# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "AgenticflowAIVariable": AgenticflowAIVariable,
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "AgenticflowAIVariable": "AgenticflowAIVariable",
}
