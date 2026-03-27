# -*- coding: utf-8 -*-
import string
import random
import getopt
import sys
import os.path
import jsonpickle

def get_num_and_file_from_args_or_default(num_default=0, file_default="")->tuple[int,str]:
    try:
        opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of elements", "file"])
    except getopt.GetoptError as err:
        getopt.usage()
        sys.exit(2)
    num = num_default
    file = file_default
    for opt, arg in opts:
        if opt == "-n":
            num = int(arg)
        elif opt == "-f":
            file = arg
    return num, file

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

def save_to_json(data, file_name):
    file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", file_name)
    with open(file, "w", encoding='utf-8') as f:
        jsonpickle.set_encoder_options("json", indent=2, ensure_ascii=False)
        f.write(jsonpickle.encode(data))