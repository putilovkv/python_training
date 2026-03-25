# -*- coding: utf-8 -*-
import string
import random


def random_string(prefix, maxlength, use_digits=True, use_latin=True, use_punctuation=True, use_cyrillic=True, use_space=True, use_newline=False) -> str:
    digits = string.digits
    latin = string.ascii_letters
    punctuation = string.punctuation
    cyrillic = "абвгдеёжзиклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    symbols = ""
    if use_digits:
        symbols += digits
    if use_latin:
        symbols += latin
    if use_punctuation:
        symbols += punctuation
    if use_cyrillic:
        symbols += cyrillic
    if use_space:
        symbols += " "*10*(use_digits + use_latin + use_punctuation + use_cyrillic)
    if use_newline:
        symbols += "\n"*10*(use_digits + use_latin + use_punctuation + use_cyrillic)
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlength))])