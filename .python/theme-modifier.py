import json
import os

THEME_NAME = "Peaceful Dawn of the Blue Mountains"

def insert_background_color(color: str):
    """Insert a color in hexadecimal in the colors settings

    Args:
        color (string): Color in hexadecimal (ex: "#00598d4f")
    """
    if len(color) != 7 or color[0] != "#":
        raise ValueError("color must be a string of 7 element and start with '#'.")
    json_theme_path = f"{os.path.dirname(__file__)}/../themes/{THEME_NAME}-color-theme.json"
    with open(json_theme_path, 'r') as json_file:
        dico = json.load(json_file)
    for key in dico["colors"]:
        if "background" in key.lower() and "badge" not in key.lower():
            dico["colors"][key] = color + dico["colors"][key][7:]
    with open(json_theme_path, 'w') as json_file:
        json.dump(dico, json_file, indent=4)
    print("Done")

insert_background_color("#00598d")
