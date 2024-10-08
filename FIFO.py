import random

user_capacity = 0

# Definicja funkcji FIFO Page Replacement
def fifo(references, capacity):
    # Inicjalizacja pamięci na podstawie podanej pojemności
    memory = [" "] * capacity
    n, page_hit, page_fault = 0, 0, 0

    print("\n FIFO Page Replacement\n")

    # Iteracja przez listę odwołań do stron
    for i in references:
        # Sprawdzenie, czy strona jest już w pamięci
        if i in memory:
            page_hit += 1  # Zwiększenie licznika trafień
            print(f"{i}     {' '.join(map(str, memory))}      trafienie strony")
        else:
            page_fault += 1  # Zwiększenie licznika błędów
            memory[n] = i  # Zamiana najstarszej strony na nową
            # Aktualizacja wskaźnika do najstarszej strony
            if n != capacity - 1:
                n += 1
            else:
                n = 0
            print(f"{i}     {' '.join(map(str, memory))}      błąd strony")

    # Obliczenie i wyświetlenie współczynnika trafień i błędów
    hit_rate = round((page_hit / (page_hit + page_fault)), 2)
    fault_rate = round((page_fault / (page_hit + page_fault)), 2)

    print(f"\nLiczba trafień: {page_hit}")
    print(f"Liczba błędów: {page_fault}")
    print(f"Współczynnik trafień: {hit_rate}")
    print(f"Współczynnik błędów: {fault_rate}")

# Funkcja główna do zbierania danych od użytkownika
def main():
    # Wybór pojemności pamięci przez użytkownika
    while True:
        print("Czy chcesz wygenerować losowo pojemność (1-5) czy wybrać samodzielnie?\n"
              "1. Wygeneruj losowo\n"
              "2. Wybierz samodzielnie")
        answer1 = int(input("Podaj wybraną opcję (liczbę): "))
        if answer1 == 1:
            user_capacity = random.randint(1, 5)
            print(f"Wygenerowana pojemność: {user_capacity}")
            break
        elif answer1 == 2:
            user_capacity = int(input("Podaj wartość pojemności: "))
            break
        else:
            print("Podaj prawidłową liczbę.")

    # Wybór listy odwołań do stron przez użytkownika
    while True:
        print("Czy chcesz wygenerować losowo odwołania czy wybrać samodzielnie?\n"
              "1. Wygeneruj losowo\n"
              "2. Wybierz samodzielnie")
        answer2 = int(input("Podaj wybraną opcję (liczbę): "))
        if answer2 == 1:
            answer3 = int(input("Podaj liczbę odwołań: "))
            user_references = [random.randint(0, 9) for _ in range(answer3)]
            print(f"Wygenerowane odwołania: {' '.join(map(str, user_references))}")
            break
        elif answer2 == 2:
            user_references = input("Podaj odwołania oddzielone spacjami:\n").split()
            user_references = list(map(int, user_references))
            break
        else:
            print("Podaj prawidłową liczbę.")

    # Wywołanie funkcji FIFO z zebranymi danymi
    fifo(user_references, user_capacity)

# Wywołanie funkcji głównej
main()
