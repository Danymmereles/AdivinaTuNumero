import random


class NumberGuessingGame:
    def __init__(self, min_value: int = 1, max_value: int = 100, max_attempts: int = 10):
        """
        Inicializa los valores del juego.
        :param min_value: Número mínimo del rango de adivinanza.
        :param max_value: Número máximo del rango de adivinanza.
        :param max_attempts: Máximo de intentos permitidos para adivinar el número.
        """
        self.min_value = min_value
        self.max_value = max_value
        self.max_attempts = max_attempts
        self.secret_number = random.randint(min_value, max_value)
        self.attempts = 0

    def guess(self, user_guess: int) -> str:
        """
        Comprueba el intento del usuario contra el número secreto.
        :param user_guess: El número proporcionado por el usuario.
        :return: Un mensaje que indica si el usuario ha adivinado o necesita intentar de nuevo.
        """
        if user_guess < self.min_value or user_guess > self.max_value:
            return f"Por favor, ingresa un número entre {self.min_value} y {self.max_value}."

        self.attempts += 1
        if user_guess < self.secret_number:
            return "Demasiado bajo. Intenta con un número más alto."
        elif user_guess > self.secret_number:
            return "Demasiado alto. Intenta con un número más bajo."
        else:
            return "¡Felicidades! Has adivinado el número correctamente."

    def has_attempts_left(self) -> bool:
        """
        Verifica si quedan intentos disponibles.
        :return: Verdadero si hay intentos restantes, Falso si no.
        """
        return self.attempts < self.max_attempts

    def attempts_left(self) -> int:
        """
        Devuelve el número de intentos restantes.
        :return: Número de intentos restantes.
        """
        return self.max_attempts - self.attempts

    def reset_game(self):
        """
        Reinicia el juego generando un nuevo número secreto y reiniciando los intentos.
        """
        self.secret_number = random.randint(self.min_value, self.max_value)
        self.attempts = 0
        print("\nJuego reiniciado. ¡Buena suerte!")

    def start_game(self):
        """
        Inicia el juego interactivo de adivinanza.
        """
        print(f"¡Bienvenido al juego de Adivina el Número!")
        print(f"Adivina un número entre {self.min_value} y {self.max_value}. Tienes {self.max_attempts} intentos.\n")

        while self.has_attempts_left():
            try:
                user_input = input("Ingresa tu número: ")
                user_guess = int(user_input)
                result = self.guess(user_guess)
                print(result)

                if "¡Felicidades!" in result:
                    break

                print(f"Intentos restantes: {self.attempts_left()}")
            except ValueError:
                print("Entrada inválida. Por favor, ingresa un número.")

        if not self.has_attempts_left():
            print(f"\nLo siento, te has quedado sin intentos. El número era {self.secret_number}.")
        self.play_again()

    def play_again(self):
        """
        Pregunta al usuario si quiere jugar de nuevo y reinicia o termina el juego.
        """
        choice = input("\n¿Quieres jugar de nuevo? (s/n): ").strip().lower()
        if choice == 's':
            self.reset_game()
            self.start_game()
        else:
            print("¡Gracias por jugar! Hasta la próxima.")


if __name__ == "__main__":
    game = NumberGuessingGame()
    game.start_game()
