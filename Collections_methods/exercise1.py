text = "un día que el viento soplaba con fuerza#mira como se mueve aquella barola -dijo un monje#lo que se muebe es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro"

lines = text.split("#")

for i, line in enumerate(lines):
    lines[i] = line.capitalize()
    if i == 0:
        lines[i] = lines[i] + "..."
    else:
        lines[i] = "- " + lines[i] + "."

for line in lines:
    print(line)