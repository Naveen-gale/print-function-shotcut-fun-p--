import json
import datetime

def p(*args, type=None, debug=False):
    msg = " ".join(str(a) for a in args)

    # Detect special cases
    if msg == "":
        msg = "⚠️ Message is empty"
        type = "warning"

    if msg == "None":
        msg = "⚠️ Value is None"
        type = "warning"

    # Debug control
    if type == "debug" and not debug:
        return

    # Default print (like real print)
    if type is None:
        print(msg)
        return

    # Colors
    colors = {
        "success": "\033[92m",
        "error": "\033[91m",
        "warning": "\033[93m",
        "info": "\033[94m",
        "debug": "\033[90m"
    }

    color = colors.get(type, "\033[0m")

    print(f"{color}{msg}\033[0m")