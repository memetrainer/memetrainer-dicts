import tqdm
from pathlib import Path

from audio_loader import load_audio


def main(lang_key, words, audiopath):
    for word in tqdm.tqdm(words):
        load_audio(lang_key, word, audiopath=audiopath)


if __name__ == "__main__":
    lang_key = "fr"
    audiopath = Path("new_dicts")

    words = """
    les produits d'entretien
    """
    words = [x.strip() for x in words.split("\n") if x.strip() != ""]

    main(lang_key, words, audiopath)
