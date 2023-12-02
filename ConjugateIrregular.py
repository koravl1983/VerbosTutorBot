import json

# Функция для загрузки данных из JSON-файла
def load_irregular_verbs(filename):
	with open(filename, 'r', encoding='utf-8') as file:
		data = json.load(file)
	return data

# Загрузка данных
#irregular_forms = load_irregular_verbs('irregular_verbs.json')

def conjugate_irregular(verb, pronoun, tense):
	# Словарь для специальных форм неправильных глаголов
	irregular_forms = {
		"ser": 
		{
			"Presente Simple": {
				"yo": "soy",
				"vos": "eres",
				"él/ella": "es",
				"nosotros": "somos",
				"ellos/ustedes": "son"
			},   
			"Preterito Imperfecto": {
				"yo": "era",
				"vos": "eras",
				"él/ella": "era",
				"nosotros": "éramos",
				"ellos/ustedes": "eran"
			},
			"Perfecto Simple": {
				"yo": "fui",
				"vos": "fuiste",
				"él/ella": "fue",
				"nosotros": "fuimos",
				"ellos/ustedes": "fueron"
			},
			"Imperativo": {
				"vos": "sé",
				"usted": "sea",
				"ustedes": "sean"
			}
		},
		"estar": {
			"Presente Simple": {
				"yo": "estoy",
				"vos": "estás",
				"él/ella": "está",
				"nosotros": "estamos",
				"ellos/ustedes": "están"
			},
			"Preterito Imperfecto": {
				"yo": "estaba",
				"vos": "estabas",
				"él/ella": "estaba",
				"nosotros": "estábamos",
				"ellos/ustedes": "estaban"
			},
			"Perfecto Simple": {
				"yo": "estuve",
				"vos": "estuviste",
				"él/ella": "estuvo",
				"nosotros": "estuvimos",
				"ellos/ustedes": "estuvieron"
			},
			"Imperativo": {
				"vos": "está",
				"usted": "esté",
				"ustedes": "estén"
			}
		},
		"tener": {
			"Presente Simple": {
				"yo": "tengo",
				"vos": "tienes",
				"él/ella": "tiene",
				"nosotros": "tenemos",
				"ellos/ustedes": "tienen"
			},
			"Preterito Imperfecto": {
				"yo": "tenía",
				"vos": "tenías",
				"él/ella": "tenía",
				"nosotros": "teníamos",
				"ellos/ustedes": "tenían"
			},
			"Perfecto Simple": {
				"yo": "tuve",
				"vos": "tuviste",
				"él/ella": "tuvo",
				"nosotros": "tuvimos",
				"ellos/ustedes": "tuvieron"
			},
			"Imperativo": {
				"vos": "ten",
				"usted": "tenga",
				"ustedes": "tengan"
			}
		},
		"ir": {
			"Presente Simple": {
				"yo": "voy",
				"vos": "vas",
				"él/ella": "va",
				"nosotros": "vamos",
				"ellos/ustedes": "van"
			},
			"Preterito Imperfecto": {
				"yo": "iba",
				"vos": "ibas",
				"él/ella": "iba",
				"nosotros": "íbamos",
				"ellos/ustedes": "iban"
			},
			"Perfecto Simple": {
				"yo": "fui",
				"vos": "fuiste",
				"él/ella": "fue",
				"nosotros": "fuimos",
				"ellos/ustedes": "fueron"
			},
			"Imperativo": {
				"vos": "anda",
				"usted": "vaya",
				"ustedes": "vayan"
			}
		},
		"hacer": {
			"Presente Simple": {
				"yo": "hago",
				"vos": "haces",
				"él/ella": "hace",
				"nosotros": "hacemos",
				"ellos/ustedes": "hacen"
			},
			"Preterito Imperfecto": {
				"yo": "hacía",
				"vos": "hacías",
				"él/ella": "hacía",
				"nosotros": "hacíamos",
				"ellos/ustedes": "hacían"
			},
			"Perfecto Simple": {
				"yo": "hice",
				"vos": "hiciste",
				"él/ella": "hizo",
				"nosotros": "hicimos",
				"ellos/ustedes": "hicieron"
			},
			"Imperativo": {
				"vos": "haz",
				"usted": "haga",
				"ustedes": "hagan"
			}
		},
		"ver": {
			"Presente Simple": {
				"yo": "veo",
				"vos": "ves",
				"él/ella": "ve",
				"nosotros": "vemos",
				"ellos/ustedes": "ven"
			},
			"Preterito Imperfecto": {
				"yo": "veía",
				"vos": "veías",
				"él/ella": "veía",
				"nosotros": "veíamos",
				"ellos/ustedes": "veían"
			},
			"Perfecto Simple": {
				"yo": "vi",
				"vos": "viste",
				"él/ella": "vio",
				"nosotros": "vimos",
				"ellos/ustedes": "vieron"
			},
			"Imperativo": {
				"usted": "vea",
				"ustedes": "vean"
			}
		},
		"saber": {
			"Presente Simple": {
				"yo": "sé",
				"vos": "sabes",
				"él/ella": "sabe",
				"nosotros": "sabemos",
				"ellos/ustedes": "saben"
			},
			"Preterito Imperfecto": {
				"yo": "sabía",
				"vos": "sabías",
				"él/ella": "sabía",
				"nosotros": "sabíamos",
				"ellos/ustedes": "sabían"
			},
			"Perfecto Simple": {
				"yo": "supe",
				"vos": "supiste",
				"él/ella": "supo",
				"nosotros": "supimos",
				"ellos/ustedes": "supieron"
			},
			"Imperativo": {
				"usted": "sepa",
				"ustedes": "sepan"
			}
		},
		"decir": {
			"Presente Simple": {
				"yo": "digo",
				"vos": "dices",
				"él/ella": "dice",
				"nosotros": "decimos",
				"ellos/ustedes": "dicen"
			},
			"Preterito Imperfecto": {
				"yo": "decía",
				"vos": "decís",
				"él/ella": "decía",
				"nosotros": "decíamos",
				"ellos/ustedes": "decían"
			},
			"Perfecto Simple": {
				"yo": "dije",
				"vos": "dijiste",
				"él/ella": "dijo",
				"nosotros": "dijimos",
				"ellos/ustedes": "dijeron"
			},
			"Imperativo": {
				"vos": "di",
				"usted": "diga",
				"ustedes": "digan"
			}
		},
		"venir": {
			"Presente Simple": {
				"yo": "vengo",
				"vos": "vienes",
				"él/ella": "viene",
				"nosotros": "venimos",
				"ellos/ustedes": "vienen"
			},
			"Preterito Imperfecto": {
				"yo": "venía",
				"vos": "venías",
				"él/ella": "venía",
				"nosotros": "veníamos",
				"ellos/ustedes": "venían"
			},
			"Perfecto Simple": {
				"yo": "vine",
				"vos": "viniste",
				"él/ella": "vino",
				"nosotros": "vinimos",
				"ellos/ustedes": "vinieron"
			},
			"Imperativo": {
				"vos": "veni",
				"usted": "venga",
				"ustedes": "vengan"
			}
		},
		"salir": {
			"Presente Simple": {
				"yo": "salgo",
				"vos": "sales",
				"él/ella": "sale",
				"nosotros": "salimos",
				"ellos/ustedes": "salen"
			},
			"Preterito Imperfecto": {
				"yo": "salía",
				"vos": "salías",
				"él/ella": "salía",
				"nosotros": "salíamos",
				"ellos/ustedes": "salían"
			},
			"Perfecto Simple": {
				"yo": "salí",
				"vos": "saliste",
				"él/ella": "salió",
				"nosotros": "salimos",
				"ellos/ustedes": "salieron"
			},
			"Imperativo": {
				"vos": "sal",
				"usted": "salga",
				"ustedes": "salgan"
			}
		},
		"poner": {
			"Presente Simple": {
				"yo": "pongo",
				"vos": "pones",
				"él/ella": "pone",
				"nosotros": "ponemos",
				"ellos/ustedes": "ponen"
			},
			"Preterito Imperfecto": {
				"yo": "ponía",
				"vos": "ponías",
				"él/ella": "ponía",
				"nosotros": "poníamos",
				"ellos/ustedes": "ponían"
			},
			"Perfecto Simple": {
				"yo": "puse",
				"vos": "pusiste",
				"él/ella": "puso",
				"nosotros": "pusimos",
				"ellos/ustedes": "pusieron"
			},
			"Imperativo": {
				"vos": "pone",
				"usted": "ponga",
				"ustedes": "pongan"
			}
		},
		"leer": {
			"Presente Simple": {
				"yo": "leo",
				"vos": "lees",
				"él/ella": "lee",
				"nosotros": "leemos",
				"ellos/ustedes": "leen"
			},
			"Preterito Imperfecto": {
				"yo": "leía",
				"vos": "leías",
				"él/ella": "leía",
				"nosotros": "leíamos",
				"ellos/ustedes": "leían"
			},
			"Perfecto Simple": {
				"yo": "leí",
				"vos": "leíste",
				"él/ella": "leyó",
				"nosotros": "leímos",
				"ellos/ustedes": "leyeron"
			},
			"Imperativo": {
				"vos": "lee",
				"usted": "lea",
				"ustedes": "lean"
			}
		}
	}

	# Возвращаем специальную форму, если она существует
	if verb in irregular_forms and tense in irregular_forms[verb]:
		return irregular_forms[verb][tense].get(pronoun, "Unknown form")
	else:
		return "Unknown verb or tense"

