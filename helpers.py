def paint(text, color, style):
    STYLES = {
        "normal": 0,
        "bold": 1,
        "light": 2,
        "italic": 3,
        "underline": 4,
        "blink": 5,
    }
    COLORS = {
        "black": 30,
        "red": 31,
        "green": 32,
        "yellow": 33,
        "blue": 34,
        "purple": 35,
        "cyan": 36,
        "white": 37,
    }
    
    return f"\033[{STYLES[style]};{COLORS[color]}m{text}\033[0;0m"