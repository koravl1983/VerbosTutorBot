import random
import unicodedata
import time
from ConjugateIrregular import conjugate_irregular
from ConjugateRegular import conjugate_regular

# Список глаголов и местоимений
regular_verbs = ["hablar", "comer", "vivir", "escribir", "cantar", "correr"]
irregular_verbs = ["ser", "estar", "tener", "ir", "hacer", "ver", "saber", "venir", "salir", "poner", "leer",
                   "decir", "decir", "poder", "traer", "dar", "haber", "pasar", "pedir", "sentir"]
pronouns = ["yo", "vos", "él/ella", "nosotros", "ellos/ustedes"]
pronouns_imperativo = ["vos", "usted", "ustedes"]
tenses = ["Presente Simple", "Preterito Imperfecto", "Perfecto Simple", "Imperativo"] # , "Futuro Simple"


# Функция для удаления ударений из строки
def normalize(s):
    s = str(s).lower()
    return ''.join(c for c in unicodedata.normalize('NFD', s)
                   if unicodedata.category(c) != 'Mn')

# Функция для спряжения глагола
def conjugate(verb, pronoun, tense):
    if verb in regular_verbs:
        return conjugate_regular(verb, pronoun, tense)
    elif verb in irregular_verbs:
        return conjugate_irregular(verb, pronoun, tense)

def main():
    correct_answers = 0
    total_answers = 0
    total_time = 0

    while True:
        # Выбор случайного глагола и времени
        verbs = regular_verbs + irregular_verbs
        selected_verb = random.choice(verbs)
        selected_tense = random.choice(tenses)

        # Определение местоимений для спряжения в зависимости от времени
        selected_pronouns = pronouns if selected_tense != "Imperativo" else ["vos", "nosotros"]

        # Просим пользователя проспрягать глагол по местоимениям
        print(f"Conjugate the verb '{selected_verb}' in '{selected_tense}':")
        for pronoun in selected_pronouns:
            start_time = time.time()
            user_input = input(f"{pronoun}: ")
            end_time = time.time()
            total_time += end_time - start_time

            correct_conjugation = conjugate(selected_verb, pronoun, selected_tense)
            if normalize(user_input) == normalize(correct_conjugation):
                print("Correct!")
                correct_answers += 1
            else:
                print(f"Incorrect. The correct conjugation for '{pronoun}' is '{correct_conjugation}'.")
            total_answers += 1

        # Спрашиваем, хочет ли пользователь продолжить
        continue_conjugating = input("If you'd like to stop enter ''no'': ")
        if continue_conjugating.lower() == "no":
            break

    # Вывод статистики
    print(f"\nTotal answers: {total_answers}")
    print(f"Correct answers: {correct_answers}")
    print(f"Incorrect answers: {total_answers - correct_answers}")
    print(f"Accuracy: {correct_answers / total_answers * 100:.2f}%")
    print(f"Error rate: {(total_answers - correct_answers) / total_answers * 100:.2f}%")
    print(f"Average response time: {total_time / total_answers:.2f} seconds")

if __name__ == "__main__":
    main()
