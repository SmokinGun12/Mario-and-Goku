class Character:
    def __init__(self, name, catchphrase):
        self.name = name
        self.catchphrase = catchphrase
    
    def speak(self, message):
        return f"{self.name}: {message}"

# Crear los personajes
goku = Character("Goku", "¡Vamos a pelear!")
mario = Character("Mario", "¡It's-a me, Mario!")

# Conversación
print(goku.speak("¡Hola Mario! ¿Qué haces por aquí?"))
print(mario.speak("¡Hola Goku! Estoy buscando monedas y luchando contra Bowser. ¿Y tú?"))
print(goku.speak("Estoy entrenando para hacerme más fuerte. ¿Te gustaría entrenar conmigo?"))
print(mario.speak("¡Oh, mamma mia! Prefiero saltar sobre cosas, pero podría intentarlo."))
print(goku.speak("¡Genial! ¡Quizá te enseñe el Kamehameha!"))
print(mario.speak("¡Eso suena increíble! ¿Pero no necesitaré champiñones para eso?"))
print(goku.speak("¡No, solo energía! ¡Vamos a intentarlo!"))
print(mario.speak("¡Let's-a go!"))
