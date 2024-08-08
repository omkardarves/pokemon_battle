from difflib import get_close_matches

def correct_spelling(name: str, names_list: list) -> str:
    name = name.lower()
    closest_matches = get_close_matches(name, names_list, n=1, cutoff=0.8)
    if closest_matches:
        return closest_matches[0]
    raise ValueError("Pokemon name has more than one-word mistakes.")
