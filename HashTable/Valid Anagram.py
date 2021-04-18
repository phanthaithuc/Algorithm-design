s = "anagram", t = "nagaram"

def valid_anagram(s: str, t:str) -> bool:
    if len(s) != len(t):
        return False

    return sorted(s) == sorted(t)
