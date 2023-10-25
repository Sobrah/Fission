def conditions(url):
    if url.endswith(".mp4") or url.endswith(".mp3"):
        return False
    
    return True