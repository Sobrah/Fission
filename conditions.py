INVALID_TYPES = [
    ".mp4",
    ".mp3",
    ".webm"
]


def conditions(url):
    for invalid_type in INVALID_TYPES:
        if url.endswith(invalid_type):
            return False
    
    return True