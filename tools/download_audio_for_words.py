import tqdm

from audio_loader import load_audio


if __name__ == "__main__":
    lang_key = "fr"
    slow_speed = True

    words = """
    les produits d'entretien
    """
    words = [x.strip() for x in words.split("\n") if x.strip() != ""]

    for word in tqdm.tqdm(words):
        load_audio(lang_key, word, slow=slow_speed, audiopath="new_dicts/")
