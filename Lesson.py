import random
import time
from EspanolVerbsTutor import conjugate, regular_verbs, irregular_verbs, tenses, pronouns, pronouns_imperativo, normalize

class Lesson:
    def __init__(self):
        self.lesson_started = False
        
        self.mistakes = 0
        self.total_answers = 0

        self.NewConjugation()
        self.start_time = time.time()
    
    def CurrentPronoun(self):
        return self.pronouns[self.current_pronoun_index]

    def CheckAnswer(self, answer):
         correct_conjugation = conjugate(self.selected_verb, self.CurrentPronoun(), self.selected_tense)
         self.current_pronoun_index += 1
         
         self.total_answers += 1
         
         if normalize(answer) != normalize(correct_conjugation):
             self.mistakes += 1
             return f"Error! Respuesta correcta: {correct_conjugation}"
         else:
             return "Correcto! Muy bien!"
         
    def ConjugationFinished(self):
        l = len(self.pronouns)
        return self.current_pronoun_index >= l
    
    def NewConjugation(self):
        self.selected_verb = random.choice(regular_verbs + irregular_verbs)
        self.selected_tense = random.choice(tenses)
        self.pronouns = pronouns
        if self.selected_tense == "Imperativo":
            self.pronouns = pronouns_imperativo
        self.current_pronoun_index = 0


        

        



            




