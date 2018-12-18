"""Case-study #7 Generation of sentences
Developers:
Batenev P.A., Grigorev A.E., Dolgih N.A.
"""

import random
import string

def file_read(txt_file):
    """ Read text from the file and return list. """
    with open(txt_file) as f_in:
        return f_in.read()


def text_preparation(text):
    """ Removes extra characters and spaces. """
    for i in string.punctuation:
        if i != '.' and i != ',' and i != '!' and i != '?':
            text = text.replace(i, '')
        else:
            text = text
    text = text.replace(' !', '!')
    text = text.replace(' ?', '?')
    text = text.replace(' .', '.')
    text = text.replace(' ,', ',')
    text = text.replace('...', '')
    text = text.replace('«', '')
    text = text.replace('»', '')
    text = text.replace(';', '')
    text = text.split()
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
        if char[0] == char[0].upper() and not(char.find('.') + 1) \
                and not(char.find('!') + 1) and not(char.find('?') + 1):
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


def text_generator(_dict, start, stop, num_sent):
    """ Generates crazy text. """
    word = start[random.randint(0, len(start))]
    crazy_text = word
    count = 0
    while crazy_text.count('.') < num_sent:
        count += 1
        word = _dict[word][random.randint(0, len(_dict[word]) - 1)]
        if count <= 5 and not(word.find('.') + 1):
            crazy_text += ' ' + word
        elif 5 < count < 19:
            crazy_text += ' ' + word
            if word.find('.') + 1:
                count = 1
        elif count == 19:
            crazy_text += ' ' + stop[random.randint(0, len(stop) - 1)]
            count = 1
    if crazy_text[-1] != '.':
        crazy_text += '.'
    return crazy_text


def main():
    """ Main function. """
    while True:
        try:
            txt_file = input('Enter file name, please: ')
            text = text_preparation(file_read(txt_file))
        except FileNotFoundError:
            print('File {} not found, check that the input is correct!'.format(txt_file))
        else:
            break
    num_sent = int(input('Number of generate sentences: '))

    # print(text)

    links = dict_of_links(text)
    start = start_words(links)
    stop = stop_words(links)
    print(text_generator(links, start, stop, num_sent))



if __name__ == '__main__':
    main()

