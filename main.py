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
    for sign in string.punctuation:
        if sign != '.' and sign != ',' and sign != '!' \
                and sign != '?' and sign != '-':
            text = text.replace(sign, '')
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
    text = text.replace(' - ', ' ')
    text = text.replace(' — ', ' ')
    text = text.split()
    return text


def dict_of_links(text_list):
    """ Makes dictionary of links from list. """
    _dict = {}
    links = []
    for i in range(len(text_list)-1):
        if text_list[i] not in _dict:
            for j in range(len(text_list)-1):
                if text_list[i] == text_list[j]:
                    links.append(text_list[j+1])
            _dict.update({text_list[i]: links})
        links = []
    _dict.update({text_list[len(text_list) - 1]: []})
    return _dict


def start_words(links):
    """ Generates start words list. """
    start = []
    words = links.keys()
    for char in words:
        if char[0] == char[0].upper() and \
                not(char.find('.') + 1) and not char.isdigit():
            start.append(char)
    return start


def stop_words(links):
    """ Generates stop words list. """
    stop = []
    words = links.keys()
    for char in words:
        if char[-1] == '.' or char[-1] == '!' or char[-1] == '?':
            stop.append(char)
    return stop


def text_generator(_dict, start, stop, num_sent):
    """ Generates crazy text. """
    crazy_text = ''
    for _ in range(num_sent):
        word = start[random.randint(0, len(start) - 1)]
        sent = word
        count = 1
        while count < 4:
            word = _dict[word][random.randint(0, len(_dict[word]) - 1)]
            if word not in stop:
                count += 1
                sent += ' ' + word
            else:
                word = _dict[word][random.randint(0, len(_dict[word]) - 1)]
        while count < 20:
            word = _dict[word][random.randint(0, len(_dict[word]) - 1)]
            count += 1
            sent += ' ' + word
            if word in stop:
                count = 1
                break
        if count == 20 and word not in stop:
            if sent[-1] == ',':
                sent = sent[:len(sent) - 1]
            sent += '.'
        crazy_text += sent + ' '

    return crazy_text


def main():
    """ Main function. """
    while True:
        try:
            txt_file = input('Enter file name, please: ')
            text = text_preparation(file_read(txt_file))
        except FileNotFoundError:
            print('File {} not found, '
                  'check that the input is correct!'.format(txt_file))
        else:
            break

    num_sent = int(input('Number of generate sentences: '))

    links = dict_of_links(text)
    start = start_words(links)
    stop = stop_words(links)

    print(text_generator(links, start, stop, num_sent))


if __name__ == '__main__':
    main()

