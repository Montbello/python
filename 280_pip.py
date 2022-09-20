
# pip
# Python Paketmanager

# Python Package Index (PyPI)
# https://pypi.org/

# pip aktualisieren
# python -m pip install --upgrade pip

# Paket installieren
# pip install emoji

# Infos zu einem Paket anzeigen
# pip show emoji

# In allen Paketen suchen
# Momentan (2022-05) abgestellt: ... due to unmanageable load ...
# pip search emoji

import emoji
print(emoji.emojize(":thumbs_up:"))  # 👍
print(emoji.demojize("👍"))  # :thumbs_up:

# Den Ort von dem Paket auf der eigenen Festplatte anzeigen lassen:
import importlib.util
print(importlib.util.find_spec('emoji').origin)
# C:\Users\cord\AppData\Local\Programs\Python\Python310\lib\site-packages\emoji\__init__.py

# :middle_finger:
print(emoji.emojize(":middle_finger:"))  # 🖕
