# Dictionary with codes for Polish alphabet letters
kodowanie = {
    'a': '223',
    'ą': '644',
    'b': '291',
    'c': '608',
    'ć': '536',
    'd': '970',
    'e': '626',
    'ę': '147',
    'f': '154',
    'g': '505',
    'h': '251',
    'i': '570',
    'j': '905',
    'k': '365',
    'l': '354',
    'ł': '512',
    'm': '749',
    'n': '675',
    'ń': '616',
    'o': '199',
    'ó': '583',
    'p': '384',
    'q': '577',
    'r': '211',
    's': '293',
    'ś': '341',
    't': '678',
    'u': '213',
    'v': '151',
    'w': '307',
    'x': '703',
    'y': '252',
    'z': '629',
    'ż': '801',
    'ź': '664',
    'A': '223',
    'Ą': '644',
    'B': '291',
    'C': '608',
    'Ć': '536',
    'D': '970',
    'E': '626',
    'Ę': '147',
    'F': '154',
    'G': '505',
    'H': '251',
    'I': '570',
    'J': '905',
    'K': '365',
    'L': '354',
    'Ł': '512',
    'M': '749',
    'N': '675',
    'Ń': '616',
    'O': '199',
    'Ó': '583',
    'P': '384',
    'Q': '577',
    'R': '211',
    'S': '293',
    'Ś': '341',
    'T': '678',
    'U': '213',
    'V': '151',
    'W': '307',
    'X': '703',
    'Y': '252',
    'Z': '629',
    'Ż': '801',
    'Ź': '664',
    ',': '804',
    '.': '824',
    ' ': '828'
}

# The text decoding function
def zakoduj_tekst(tekst):
    zakodowany_tekst = ''
    for litera in tekst:
        if litera in kodowanie:
            zakodowany_tekst += kodowanie[litera]
    return zakodowany_tekst

while True:
    tekst_do_zakodowania = input('Wpisz tekst do zakodowania: ')
    wynik = zakoduj_tekst(tekst_do_zakodowania)
    print('Zakodowany tekst:', wynik)
