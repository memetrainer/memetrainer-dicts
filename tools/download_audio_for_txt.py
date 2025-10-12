import glob
import tqdm
import os
from pathlib import Path

from audio_loader import load_audio

def load_dict_audio(lang_key, dictname, dict_txt_path):
    dictpath = dict_txt_path / dictname
    audiopath = dictpath / (dictname + "_audio")
    dictpath.mkdir(parents=True, exist_ok=True)
    audiopath.mkdir(parents=True, exist_ok=True)

    print("Start to download audio for", dictname, end=":\t")

    with open(dict_txt_path / (dictname + ".txt"), "r", encoding="UTF-8") as f:
        words = [w.split("\t")[0].strip() for w in f.read().split("\n") if w != ""]
    print("read", len(words), "words") 

    print("Loading: ", end="")
    for word in tqdm.tqdm(words):
        load_audio(lang_key, word, audiopath)
    print("\tSuccess!")


def get_dict_names(dict_txt_path):
    dicts = [x.split("/")[-1][:-4] for x in glob.glob(str(dict_txt_path / "*.txt"))]
    return dicts


def main(lang_key, dict_txt_path):
    dicts = get_dict_names(dict_txt_path)
    print("Found", len(dicts), "dictionaries:", dicts)

    for dictname in dicts:
        load_dict_audio(lang_key, dictname, dict_txt_path)


if __name__ == "__main__":
    lang_key = "fr"                    # language key (fr, nl, cz, pt, ...) - see gTTS_lang_codes.csv
    dict_txt_path = Path("new_dicts")  # put the txt files there (like fr_a1_1.txt, ...)

    main(lang_key, dict_txt_path)  