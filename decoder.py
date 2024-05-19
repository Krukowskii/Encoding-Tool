# Dictionary with codes for Polish alphabet letters
dekodowanie = {
    '223': 'a',
    '644': 'ą',
    '291': 'b',
    '608': 'c',
    '536': 'ć',
    '970': 'd',
    '626': 'e',
    '147': 'ę',
    '154': 'f',
    '505': 'g',
    '251': 'h',
    '570': 'i',
    '905': 'j',
    '365': 'k',
    '354': 'l',
    '512': 'ł',
    '749': 'm',
    '675': 'n',
    '616': 'ń',
    '199': 'o',
    '583': 'ó',
    '384': 'p',
    '577': 'q',
    '211': 'r',
    '293': 's',
    '341': 'ś',
    '678': 't',
    '213': 'u',
    '151': 'v',
    '307': 'w',
    '703': 'x',
    '252': 'y',
    '629': 'z',
    '801': 'ż',
    '664': 'ź',
    '804': ',',
    '824': '.',
    '828': ' '
}

# The text decoding function
def zdekoduj_tekst(kod):
    zdekodowany_tekst = ''
    i = 0
    while i < len(kod):
        if kod[i:i+3] in dekodowanie:
            zdekodowany_tekst += dekodowanie[kod[i:i+3]]
            i += 3
        else:
            zdekodowany_tekst += '?'
            i += 3
    return zdekodowany_tekst

while True:
    tekst_do_zdekodowania = input('Wpisz tekst do zdekodowania: ')
    wynik = zdekoduj_tekst(tekst_do_zdekodowania)
    print('Zdekodowany tekst:', wynik)
