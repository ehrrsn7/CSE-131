"""
Debug
"""
DEBUG = True
def debug(*txt, debug_msg=True):
    text = " "
    if debug_msg: text = "debug: "
    for item in txt: text += str(item) + " "
    if DEBUG: print(f"{text}")
