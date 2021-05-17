import random

zahl = random.randint(0, 101)
attempts: int = 0

print("Willkommen zum Spiel FizzBuzz")
print(zahl)
print("Ist die Zahl durch 3 teilbar, dann gib das Wort `Fizz` ein!")
print("Ist die Zahl durch 5 teilbar, dann gib das Wort `Buzz` ein!")
print("Ist die Zahl durch 3 und 5 teilbar, dann gib das Wort `FizzBuzz` ein!")
print("Kommt keines der Ergebnisse in Frage, dann gib NONE ein")

while True:
    if attempts and versuch == 5:
        break
    attempts += 1
    try:
        button: str = input("Bitte gib jetzt dein Ergebnis ein: ")
        if (zahl % 15 == 0) and (button == "FizzBuzz"):
            print("Korrekt")
            print(f"Du hast nur {attempts} Versuche gebraucht")
            break
        elif (zahl % 5 == 0) and (button == "Buzz"):
            print("Korrekt")
            print(f"Du hast nur {attempts} Versuche gebraucht")
            break
        elif (zahl % 3 == 0) and (button == "Fizz"):
            print("Korrekt")
            print(f"Du hast nur {attempts} Versuche gebraucht")
            break
        elif (zahl % 15 != 0) and (button == "NONE"):
            print("Korrekt")
            print(f"Du hast nur {attempts} Versuche gebraucht")
            break
        elif (zahl % 5 != 0) and (button == "NONE"):
            print("Korrekt")
            print(f"Du hast nur {attempts} Versuche gebraucht")
            break
        elif (zahl % 3 != 0) and (button == "NONE"):
            print("Korrekt")
            print(f"Du hast nur {attempts} Versuche gebraucht")
            break
        else:
            print("Falsch!, versuch es erneut!")
    except ValueError as e:
        exit(1)
