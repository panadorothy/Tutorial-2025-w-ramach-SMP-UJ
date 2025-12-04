import random                # Importujemy moduł random do losowego mieszania słów

def play_game():
    print("🔵 Добро пожаловать в игру «Собери предложение»!")  # Powitanie gracza
    print("Это игра для развития речи и внимания.\n")          # Krótki opis gry

    # Lista prostych zdań odpowiednich dla dzieci (wersja rosyjska)
    sentences = [
        "Кот ловит мышку",
        "Собака играет мячом",
        "Мама читает книгу",
        "Я люблю рисовать",
        "Птица поёт на дереве"
    ]

    sentence = random.choice(sentences)  # Losujemy jedno zdanie z listy
    print(f"🟡 Оригинальное предложение: {sentence}")  # Wyświetlamy zdanie (pomoc dla logopedy)

    # Prosta tokenizacja zdania poprzez split() (zastępuje NLTK)
    tokens = sentence.split()

    # Tworzymy kopię listy słów, aby nie mieszać oryginału
    shuffled = tokens[:]
    random.shuffle(shuffled)  # Losowo mieszamy kolejność słów

    print("\n🔀 Слова перемешаны:")  # Informujemy gracza
    print(" | ".join(shuffled))      # Wyświetlamy słowa oddzielone kreską

    print("\nПопробуй собрать предложение в правильном порядке!")  # Instrukcja
    user_answer = input("Введи правильное предложение: ").strip()  # Pobieramy odpowiedź gracza

    # Porównujemy odpowiedź użytkownika z oryginalnym zdaniem
    if user_answer == sentence:
        print("🟢 Молодец! Это правильный ответ!")  # Komunikat sukcesu
    else:
        print("🔴 Почти! Правильный вариант:")       # Komunikat błędu
        print(sentence)                              # Pokazujemy prawidłową odpowiedź

# Główna część programu — uruchamiamy grę tylko gdy plik jest wykonywany bezpośrednio
if __name__ == "__main__":
    play_game()  # Wywołujemy funkcję startującą grę

