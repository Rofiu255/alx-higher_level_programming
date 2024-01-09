#!/usr/bin/python3
def multiple_returns(sentence):
    sen_len = len(sentence)

    if (sen_len == 0):
        new_tuple = (sen_len, None)
    else:
        new_tuple = (sen_len, sentence[0])

    return (new_tuple)
