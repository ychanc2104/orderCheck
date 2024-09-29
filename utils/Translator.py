import gettext
import os
from definitions import ROOT_DIR

def get_error(key: str, language: str="en"):
    return get_translator(language)(key)

def get_translator(language: str="en"):
    try:
        localedir = os.path.join(ROOT_DIR, "resources/translations")
        print(f"Localedir: {localedir}")
        translator = gettext.translation(
            "messages", localedir=localedir, languages=[language]
        )
        translator.install()
        return translator.gettext
    except FileNotFoundError:
        return lambda x: x
