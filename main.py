"""Case-study #7 Generation of sentences
Developers:
Batenev P.A., Grigorev A.E., Dolgih N.A.
"""

import random
import string

def file_read(txt_file):
    """ Read text from the file and return list. """
    with open(txt_file) as f_in:
        return f_in.read().split()


def text_preparation(text):
    """ Removes extra characters and spaces. """
    signs = [')', '(', '^', '%', '#', '$', ';', ':', '"', '=', '+', '-', '_', '–']
    for i in range(len(text)):
        if text[i][-1] in signs:
            text[i] = text[i][:-1]
        else:
            text[i] = text[i]
    for i in signs:
        a = ' i'
        if a in text:
            text.replace(a, i)
    return text


def dict_of_links(text_list):
    """ Makes a dictionary of links from the list. """
    d = {}
    l = []
    for i in range(len(text_list)-1):
        if text_list[i] not in d:
            for j in range(len(text_list)-1):
                if text_list[i] == text_list[j]:
                    l.append(text_list[j+1])
            d.update({text_list[i]: l})
        l = []
    d.update({text_list[len(text_list) - 1]: []})
    return d


def start_words(links):
    """ Generates a list of starting words. """
    start = []
    words = links.keys()
    for char in words:
        if char[0] == char[0].upper() and not(char.find('.') + 1):
            start.append(char)
    return start


def stop_words(links):
    """ Generates a list of final words. """
    stop = []
    words = links.keys()
    for char in words:
        if char[-1] == '.':
            stop.append(char)
    return stop


def text_generator():
    """ Generates crazy text. """
    # TODO


def main():
    """ Main function. """
    txt_file = input()
    text = text_preparation(file_read(txt_file))
    print(text)


if __name__ == '__main__':
    main()

