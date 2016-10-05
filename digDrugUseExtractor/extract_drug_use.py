import re

def drug_use_build_phrase(x):
    return r'(?:\b' + x + r's?\b)'

drug_use_words = [
    r"meth\s*head",
    r"meth-head",
    r"crack\s*head",
    r"crack-head",
    r"meth\s*monster",
    r"meth-monster",
    r"druggie",
    r"junkie",
    r"adict",
    r"dope\s*head",
    r"dope-head",
    r"acid\s*freak",
    r"acid-freak",
    r"acid\s*head",
    r"acid-head",
    r"bag\s*bitch",
    r"bag-bitch",
    r"coke\s*whore",
    r"coke-whore",
    r"dope\s*whore",
    r"dope-whore",
    r"crank\s*whore",
    r"crank-whore",
    r"pill\s*popper",
    r"pill-popper"
    ]

# If any of the following match, assume it is a negative statement
negative_regex_list = [
    r"don't\s+do\s+drugs?",
    r'do\s+not\s+do\s+drugs?',
    r'\bno\s+drugs\b',
    r'adrenaline'
]

# Typical sentence fragments to refer to drug users
regex_list = [
    "|".join(phrase_re_list),
    r'\bon\s+.{,15}?drugs?',
    r'\bshe\s+.{,4}?drugs',
    r'\btrak\s+.{,15}?arms',
    r'\buses\s+drugs',
    r'\buses\s+and.{,8}?drugs',
    r'\bsmells?\s+.{,8}?drugs',
    r'\bdoes\s.{,15}?drugs',
    r'\bshe\s+in.{,7}?drugs',
]

def extract_drug_use(text):
    """Returns an array of all mentions of drug use.
    Example mentions from ads:
    - she is a drug user
    - uses this money he uses it to buy drugs
    - SHE IS ON SOME HEAVY DRUGS
    - she's on drugs
    - TRAK MARKS ON ARMS
    - uses drugs during her sessions
    - provider also uses drugs
    - uses and sells drugs
    - smell like some drug she uses
    - does drugs -- negative is I don't smoke or do drugs
    - negative: I am not looking for someone who uses drugs
    - negative: no drugs
    - Shes In To Drugs
    - negative: who isn't on drugs
    - negative: I do not do drugs
    - meth head
    - crack head
    - crackhead/meth monster
    - druggie
    - junkie
    - adict
    - dopehead
    - acid freak
    - acid head
    - bag bitch
    - coke whore
    - dope whore
    - crank whore
    - pill popper

    """

    for negative in negative_regex_list:
        if re.findall(negative, text, re.I):
            return []


    # Common drug user slang
    phrase_re_list = []
    for x in drug_use_words:
         phrase_re_list.append(drug_use_build_phrase(x))

    result = []
    for r in regex_list:
        result += re.findall(r, text, re.I)

    return result