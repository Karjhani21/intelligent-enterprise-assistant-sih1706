BAD_WORDS = {"idiot", "stupid", "damn", "fool", "hate"}

def contains_profanity(text: str) -> bool:
    words = text.lower().split()
    return any(word in BAD_WORDS for word in words)
