def conjugate_regular(verb, pronoun, tense):
    root = verb[:-2]
    ending = verb[-2:]

    if tense == "Presente Simple":
        endings = {
            "yo": "o",
            "vos": "as" if ending == "ar" else "es",
            "él/ella": "a" if ending == "ar" else "e",
            "nosotros": "amos" if ending == "ar" else "emos" if ending == "er" else "imos",
            "ellos/ustedes": "an" if ending == "ar" else "en"
        }
        return root + endings[pronoun]

    elif tense == "Preterito Imperfecto":
        endings = {
            "yo": "aba" if ending == "ar" else "ía",
            "vos": "abas" if ending == "ar" else "ías",
            "él/ella": "aba" if ending == "ar" else "ía",
            "nosotros": "ábamos" if ending == "ar" else "íamos",
            "ellos/ustedes": "aban" if ending == "ar" else "ían"
        }
        return root + endings[pronoun]

    elif tense == "Perfecto Simple":
        endings = {
            "ar": {
                "yo": "é",
                "vos": "aste",
                "él/ella": "ó",
                "nosotros": "amos",
                "ellos/ustedes": "aron"
            },
            "er": {
                "yo": "í",
                "vos": "iste",
                "él/ella": "ió",
                "nosotros": "imos",
                "ellos/ustedes": "ieron"
            },
            "ir": {
                "yo": "í",
                "vos": "iste",
                "él/ella": "ió",
                "nosotros": "imos",
                "ellos/ustedes": "ieron"
            }
        }

        return root + endings[ending][pronoun]

    elif tense == "Imperativo":
        # Здесь будет представлена форма для 'vos', 'nosotros', 'ustedes'
        if pronoun == "vos":
            return root + "a" if ending == "ar" else root + "e"
        
        if pronoun == "usted":
            return root + "e" if ending == "ar" else root + "a"
        
        if pronoun == "ustedes":
            return root + "en" if ending == "ar" else root + "an"

        return verb + endings[pronoun]

    else:
        return "Unknown tense"