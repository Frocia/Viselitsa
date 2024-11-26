
import random

def get_random_word():
    words = ["python", "hangman", "developer", "github", "programming", "algorithm"]
    return random.choice(words)

def display_hangman(tries):
    stages = [
        '''
           -----
           |   |
           O   |
          /|\  |
          / \  |
               |
        ---------
        ''',
        '''
           -----
           |   |
           O   |
          /|\  |
          /    |
               |
        ---------
        ''',
        '''
           -----
           |   |
           O   |
          /|\  |
               |
               |
        ---------
        ''',
        '''
           -----
           |   |
           O   |
          /|   |
               |
               |
        ---------
        ''',
        '''
           -----
           |   |
           O   |
           |   |
               |
               |
        ---------
        ''',
        '''
           -----
           |   |
           O   |
               |
               |
               |
        ---------
        ''',
        '''
           -----
           |   |
               |
               |
               |
               |
        ---------
        '''
    ]
    return stages[tries]

def play_game():
    word = get_random_word()
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6

    print("Добро пожаловать в игру 'Виселица'!")
    print(display_hangman(tries))
    print(word_completion)
    print("")

    while not guessed and tries > 0:
        guess = input("Введите букву или слово целиком: ").lower()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"Вы уже называли букву '{guess}'.")
            elif guess not in word:
                print(f"Буквы '{guess}' нет в слове.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(f"Отлично! Буква '{guess}' есть в слове.")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print(f"Вы уже пытались отгадать слово '{guess}'.")
            elif guess != word:
                print(f"Слово '{guess}' неверно.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Неверный ввод. Попробуйте снова.")

        print(display_hangman(tries))
        print(word_completion)
        print("")

    if guessed:
        print(f"Поздравляем! Вы угадали слово: {word}!")
    else:
        print(f"Вы проиграли. Загаданное слово было: {word}.")

if __name__ == "__main__":
    play_game()