import random

class HangmanGame:
    def __init__(self, max_attempts=6):
        self.word_list = [
            "python", "programacion", "juego", "ahorcado", "modularidad", "sonarqube", "limpieza", "analisis"
        ]
        self.max_attempts = max_attempts
        self.secret_word = ""
        self.guessed_letters = set()
        self.incorrect_letters = set()
        self.remaining_attempts = max_attempts

    def choose_random_word(self):
        """Elige una palabra aleatoria de la lista."""
        indice = random.randint(0,len(self.word_list)-1)
        self.secret_word = self.word_list[indice]

    def display_game_status(self):
        """Muestra el estado actual del juego."""
        print("\nPalabra a adivinar:")
        display_word = [
            letter if letter in self.guessed_letters else "_" for letter in self.secret_word
        ]
        print(" ".join(display_word))
        print(f"Intentos restantes: {self.remaining_attempts}")
        print(f"Letras incorrectas: {', '.join(sorted(self.incorrect_letters))}")

    def make_guess(self, letter):
        """
        Procesa la letra ingresada por el usuario.
        :param letter: La letra que el usuario adivina.
        """
        if letter in self.guessed_letters or letter in self.incorrect_letters:
            print(f"Ya has adivinado la letra '{letter}'. Intenta con otra.")
            return

        if letter in self.secret_word:
            print(f"¡Bien hecho! La letra '{letter}' está en la palabra.")
            self.guessed_letters.add(letter)
        else:
            print(f"Lo siento, la letra '{letter}' no está en la palabra.")
            self.incorrect_letters.add(letter)
            self.remaining_attempts -= 1

    def is_game_won(self):
        """Comprueba si el jugador ha ganado."""
        return all(letter in self.guessed_letters for letter in self.secret_word)

    def is_game_over(self):
        """Comprueba si el juego ha terminado por falta de intentos."""
        return self.remaining_attempts <= 0

    def reset_game(self):
        """Reinicia el juego."""
        self.guessed_letters.clear()
        self.incorrect_letters.clear()
        self.remaining_attempts = self.max_attempts
        self.choose_random_word()

    def start_game(self):
        """Controla el flujo del juego completo."""
        self.choose_random_word()
        print("¡Bienvenido al juego de Ahorcado!")
        print("Adivina la palabra antes de quedarte sin intentos.\n")

        while not self.is_game_over() and not self.is_game_won():
            self.display_game_status()
            guess = input("Ingresa una letra: ").lower()
            if len(guess) != 1 or not guess.isalpha():
                print("Por favor, ingresa una única letra válida.")
                continue

            self.make_guess(guess)

        self.display_game_status()
        if self.is_game_won():
            print("¡Felicidades! Has adivinado la palabra correctamente.")
        else:
            print(f"Lo siento, has perdido. La palabra era '{self.secret_word}'.")

        self.play_again()

    def play_again(self):
        """Pregunta al usuario si quiere jugar otra vez."""
        choice = input("\n¿Quieres jugar de nuevo? (s/n): ").strip().lower()
        if choice == 's':
            self.reset_game()
            self.start_game()
        else:
            print("Gracias por jugar. ¡Hasta la próxima!")


class HangmanUtilities:
    @staticmethod
    def get_random_word():
        """Devuelve una palabra aleatoria de una lista de palabras."""
        words = [
            "inteligencia", "software", "diseño", "agil", "sostenible", "refactorizacion", "arquitectura", "python"
        ]
        indice = random.randint(0,len(words)-1)
        return words[indice]

    @staticmethod
    def get_max_attempts(difficulty_level):
        """
        Devuelve el número de intentos permitidos basado en la dificultad.
        :param difficulty_level: Nivel de dificultad (fácil, medio, difícil).
        :return: Número de intentos.
        """
        difficulty_map = {
            "facil": 8,
            "medio": 6,
            "dificil": 4
        }
        return difficulty_map.get(difficulty_level, 6)

    @staticmethod
    def validate_difficulty():
        """Pide y valida el nivel de dificultad del usuario."""
        difficulty = input("Elige un nivel de dificultad (facil/medio/dificil): ").strip().lower()
        while difficulty not in ["facil", "medio", "dificil"]:
            print("Opción inválida. Por favor, elige entre facil, medio o dificil.")
            difficulty = input("Elige un nivel de dificultad (facil/medio/dificil): ").strip().lower()
        return difficulty


def main():
    print("Bienvenido a Ahorcado con opciones de dificultad!")
    difficulty = HangmanUtilities.validate_difficulty()
    max_attempts = HangmanUtilities.get_max_attempts(difficulty)

    game = HangmanGame(max_attempts)
    game.start_game()


if __name__ == "__main__":
    main()
