#!/usr/bin/python3
def multiple_returns(sentence):

    str_len = len(sentence)
    first_character = sentence[:1] if (sentence) else None
    return (str_len, first_character,)
