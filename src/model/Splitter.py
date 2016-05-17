"""
Splitter.py

Daniel Wang
May 2016
"""


import re


def split(t, min_len=3):
    splitter = re.compile('\\W*')
    return [s.lower() for s in splitter.split(t) if len(s) > min_len]
