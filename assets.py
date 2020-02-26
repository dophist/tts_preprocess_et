# -*- coding: utf-8 -*-

from collections import defaultdict

audible_symbols = {'@': 'ät', '$': 'dollar', '%': 'protsent', '&': 'ja', '+': 'pluss',
                   '=': 'võrdub', '€': 'euro', '£': 'nael', '§': 'paragrahv', '°': 'kraad',
                   '±': 'pluss miinus', '‰': 'promill', '×': 'korda', 'x': 'korda',
                   '*': 'korda', '∙': 'korda', ':': 'jagada', '-': 'miinus'}  # TODO jagada vs jagatud

# sümbolid, mis häälduvad vaid siis, kui asuvad kahe arvu vahel
audible_connecting_symbols = ('×', 'x', '*', ':', '-')

# sümbolid ja lühendid, mis käänduvad vastavalt eelnevale arvule (nt 1 meeter vs 5 meetrit)
units = ('$', '%', '‰', '€', '£', '°', 'a', 'atm', 'km', 'km²', 'm', 'm²', 'm³', 'mbar', 'cm',
         'ct', 'd', 'dB', 'eks', 'h', 'ha', 'hj', 'hl', 'mm', 'tk', 'p', 'rbl', 'rm', 'lk',
         'pk', 's', 'sl', 'spl', 'sek', 'tk', 'tl', 'kr', 'min', 't', 'mln', 'mld', 'mg',
         'g', 'kg', 'ml', 'l', 'cl', 'dl')

# kaassõnad, mille korral eelnev või järgnev arvsõna läheb omastavasse käändesse
genitive_prepositions = ('üle', 'alla')
genitive_postpositions = ('võrra', 'ümber', 'pealt', 'peale', 'ringis', 'paiku', 'aegu', 'eest')
# sõnad, mille korral järgnev arvsõna läheb nimetavasse käändesse (kui oma kääne määramata)
nominative_preceeding_words = ('kell', 'number', 'aasta', 'kl', 'nr', 'a')

abbreviations = defaultdict(None, {'a': 'aasta',
                                   'aa': 'arveldusaasta',
                                   'adm': 'admiral',
                                   'aj': 'ajutine',
                                   'ak': 'arvelduskonto',
                                   'akad': 'akadeemik',
                                   'al': 'alates',
                                   'apr': 'aprill',
                                   'atm': 'atmosfäär',
                                   'aug': 'august',
                                   'aü': 'ametiühing',
                                   'bulg': 'bulgaaria keeles',
                                   'ca': 'umbes',
                                   'cl': 'sentiliiter',
                                   'cm': 'sentimeeter',
                                   'ct': 'karaat',
                                   'dB': 'detsibell',
                                   'dal': 'dekaliiter',
                                   'dets': 'detsember',
                                   'dipl': 'diplom',
                                   'dir': 'direktor',
                                   'dl': 'detsiliiter',
                                   'dots': 'dotsent',
                                   'dr': 'doktor',
                                   'e': 'ehk',
                                   'e.m.a': 'enne meie ajaarvamist',
                                   'eKr': 'enne Kristuse sündi',
                                   'eks': 'eksemplar',
                                   'end': 'endine',
                                   'g': 'gramm',
                                   'h': 'tund',
                                   'ha': 'hektar',
                                   'hbr': 'heebrea keeles',
                                   'hisp': 'hispaania keeles',
                                   'hj': 'hobujõud',
                                   'hl': 'hektoliiter',
                                   'hn': 'hiina keeles',
                                   'hr': 'härra',
                                   'hrl': 'harilikult',
                                   'ik': 'isikukood',
                                   'ingl': 'inglise keeles',
                                   'ins': 'insener',
                                   'it': 'itaalia keeles',
                                   'j': 'jõgi',
                                   'j.a': 'juures asuv',
                                   'jaan': 'jaanuar',
                                   'jj': 'ja järgmine',
                                   'jm': 'ja muud',
                                   'jms': 'ja muud sellised',
                                   'jmt': 'ja mitmed teised',
                                   'jn': 'joonis',
                                   'jne': 'ja nii edasi',
                                   'jpn': 'jaapani keeles',
                                   'jpt': 'ja paljud teised',
                                   'jr': 'juunior',
                                   'jrk': 'järjekord',
                                   'jsk': 'jaoskond',
                                   'jt': 'ja teised',
                                   'juh': 'juhataja',
                                   'jun': 'juunior',
                                   'jv': 'järv',
                                   'k': 'keel',
                                   'k.a': 'kaasa arvatud',
                                   'kcal': 'kilokalor',
                                   'kd': 'köide',
                                   'kg': 'kilogramm',
                                   'khk': 'kihelkond',
                                   'kin': 'kindral',
                                   'kin-ltn': 'kindralleitnant',
                                   'kin-mjr': 'kindralmajor',
                                   'kk': 'keskkool',
                                   'kl': 'kell',
                                   'klh': 'kolhoos',
                                   'km': 'kilomeeter',
                                   'km/h': 'kilomeetrit tunnis',
                                   'km²': 'ruutkilomeeter',
                                   'knd': 'kandidaat',
                                   'kod': 'kodanik',
                                   'kol': 'kolonel',
                                   'kol-ltn': 'kolonelleitnant',
                                   'kop': 'kopikas',
                                   'kpl': 'kauplus',
                                   'kpt': 'kapten',
                                   'kpt-ltn': 'kaptenleitnant',
                                   'kpt-mjr': 'kaptenmajor',
                                   'kr': 'kroon',
                                   'krt': 'korter',
                                   'kt': 'kohusetäitja',
                                   'kub': 'kubermang',
                                   'kv': 'kvartal',
                                   'l': 'liiter',
                                   'ld': 'ladina keeles',
                                   'lg': 'lõige',
                                   'lj': 'linnajagu',
                                   'lk': 'lehekülg',
                                   'lm': 'liidumaa',
                                   'lo': 'linnaosa',
                                   'lp': 'lugupeetud',
                                   'lpn': 'lipnik',
                                   'ltn': 'leitnant',
                                   'lüh': 'lühend',
                                   'm': 'meeter',
                                   'm.a.j': 'meie ajaarvamise järgi',
                                   'm/s': 'meetrit sekundis',
                                   'mag': 'magister',
                                   'mbar': 'millibaar',
                                   'mg': 'milligramm',
                                   'mh': 'muu hulgas',
                                   'min': 'minut',
                                   'mjr': 'major',
                                   'mk': 'maakond',
                                   'ml': 'milliliiter',
                                   'mld': 'miljard',
                                   'mln': 'miljon',
                                   'mm': 'millimeeter',
                                   'mnt': 'maantee',
                                   'mob': 'mobiiltelefon',
                                   'ms': 'muuseas',
                                   'm²': 'ruutmeeter',
                                   'm³': 'kuupmeeter',
                                   'n': 'neiu',
                                   'n-srs': 'nooremseersant',
                                   'n-vbl': 'nooremveebel',
                                   'n-ö': 'nii-öelda',
                                   'nim': 'nimeline',
                                   'nn': 'niinimetatud',
                                   'nov': 'november',
                                   'nr': 'number',
                                   'nt': 'näiteks',
                                   'näd': 'nädal',
                                   'okt': 'oktoober',
                                   'osk': 'osakond',
                                   'p': 'punkt',
                                   'p.o': 'peab olema',
                                   'pKr': 'pärast Kristuse sündi',
                                   'pa': 'poolaasta',
                                   'pk': 'postkast',
                                   'pl': 'plats',
                                   'pms': 'peamiselt',
                                   'port': 'portugali keeles',
                                   'pr': 'proua',
                                   'prl': 'preili',
                                   'prof': 'professor',
                                   'ps': 'poolsaar',
                                   'pst': 'puiestee',
                                   'ptk': 'peatükk',
                                   'raj': 'rajoon',
                                   'rbl': 'rubla',
                                   'reg-nr': 'registreerimisnumber',
                                   'rg-kood': 'registrikood',
                                   'rk': 'raamatukogu',
                                   'rkl': 'riigikoguliige',
                                   'rm': 'ruumimeeter',
                                   'rms': 'reamees',
                                   'rmtk': 'raamatukogu',
                                   'rmtp': 'raamatupidamine',
                                   'rtj': 'raudteejaam',
                                   'rts': 'rootsi keeles',
                                   'rum': 'rumeenia keeles',
                                   's': 'sekund',
                                   's.a': 'sel aastal',
                                   's.o': 'see on',
                                   's.t': 'see tähendab',
                                   'saj': 'sajand',
                                   'sealh': 'sealhulgas',
                                   'seals': 'sealsamas',
                                   'sek': 'sekund',
                                   'sen': 'seenior',
                                   'sept': 'september',
                                   'sh': 'sealhulgas',
                                   'skp': 'selle kuu päeval',
                                   'sks': 'saksa keeles',
                                   'sl': 'supilusikatäis',
                                   'sm': 'seltsimees',
                                   'snd': 'sündinud',
                                   'spl': 'supilusikatäis',
                                   'srn': 'surnud',
                                   'srs': 'seersant',
                                   'st': 'see tähendab',
                                   'std': 'staadion',
                                   'stj': 'saatja',
                                   'surn': 'surnud',
                                   'sü': 'säilitusüksus',
                                   'sünd': 'sündinud',
                                   't': 'tund',
                                   'tehn': 'tehniline',
                                   'tel': 'telefon',
                                   'tk': 'tükk',
                                   'tl': 'teelusikatäis',
                                   'tlk': 'tõlkija',
                                   'tn': 'tänav',
                                   'tr': 'trükk',
                                   'ts': 'tsentner',
                                   'tv': 'televisioon',
                                   'u': 'umbes',
                                   'ukj': 'uue, Gregoriuse kalendri järgi',
                                   'ukr': 'ukraina keeles',
                                   'ung': 'ungari keeles',
                                   'v': 'vald',
                                   'v-ltn': 'vanemleitnant',
                                   'v-mdr': 'vanemmadrus',
                                   'v-vbl': 'vanemveebel',
                                   'v.a': 'välja arvatud',
                                   'van': 'vananenud',
                                   'vbl': 'veebel',
                                   'veebr': 'veebruar',
                                   'vkj': 'vana, Juliuse kalendri järgi',
                                   'vkr': 'vanakreeka keeles',
                                   'vm': 'või muud',
                                   'vms': 'või muud sellist',
                                   'vrd': 'võrdle',
                                   'vt': 'vaata',
                                   'õa': 'õppeaasta',
                                   'õp': 'õpetaja',
                                   'õpil': 'õpilane'})

cardinal_numbers = defaultdict(lambda: '', {'0': 'null',
                                            '1': 'üks',
                                            '2': 'kaks',
                                            '3': 'kolm',
                                            '4': 'neli',
                                            '5': 'viis',
                                            '6': 'kuus',
                                            '7': 'seitse',
                                            '8': 'kaheksa',
                                            '9': 'üheksa',
                                            2: 'tuhat',
                                            3: 'miljon',
                                            4: 'miljard',
                                            5: 'triljon',
                                            6: 'kvadriljon',
                                            7: 'kvintiljon',
                                            8: 'sekstiljon',
                                            9: 'septiljon',
                                            ',': 'koma',
                                            })

ordinal_numbers = defaultdict(lambda: '', {
    'üks': 'esimene',
    'kaks': 'teine',
    'kolm': 'kolmas',
    'neli': 'neljas',
    'viis': 'viies',
    'kuus': 'kuues',
    'seitse': 'seitsmes',
    'kaheksa': 'kaheksas',
    'üheksa': 'üheksas',
    'kümme': 'kümnes',
    'kümmend': 'kümnes',
    'teist': 'teistkümnes',
    'sada': 'sajas',
    'tuhat': 'tuhandes',
    'miljon': 'miljones',
    'miljard': 'miljardes',
    'triljon': 'triljones',
    'kvadriljon': 'kvadriljones',
    'kvintiljon': 'kvintiljones',
    'sekstiljon': 'sekstiljones',
    'septiljon': 'septiljones',
})

roman_numbers = defaultdict(lambda: 0, {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000})

alphabet = {
    'A': 'aa',
    'B': 'bee',
    'C': 'tsee',
    'D': 'dee',
    'E': 'ee',
    'F': 'eff',
    'G': 'gee',
    'H': 'haa',
    'I': 'ii',
    'J': 'jott',
    'K': 'kaa',
    'L': 'ell',
    'M': 'emm',
    'N': 'enn',
    'O': 'oo',
    'P': 'pee',
    'Q': 'kuu',
    'R': 'err',
    'S': 'ess',
    'Š': 'šaa',
    'Z': 'zett',
    'Ž': 'žee',
    'T': 'tee',
    'U': 'uu',
    'V': 'vee',
    'W': 'kaksisvee',
    'Õ': 'õõ',
    'Ä': 'ää',
    'Ö': 'öö',
    'Ü': 'üü',
    'X': 'iks',
    'Y': 'igrek'
}