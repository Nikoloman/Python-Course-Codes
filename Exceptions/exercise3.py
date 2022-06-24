try:
    colors = {"red": "rojo", "green": "verde", "black": "negro"}
    print(colors["white"])
except KeyError:
    print("Error: The key doesn't matches with any of the keys in the dictionary")