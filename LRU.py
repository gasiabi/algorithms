import random

# Definicja funkcji LRU Page Replacement
def lru(references, capacity):
    # Inicjalizacja pamięci na podstawie podanej pojemności
    memory = [" "] * capacity
    reference_list = []
    page_hit, page_fault = 0, 0

    print("\n LRU Page Replacement\n")

    # Iteracja przez listę odwołań do stron
    for ref in references:
        if ref not in memory:
            # Strona nie znajduje się w pamięci - błąd strony
            page_fault += 1
            if len(reference_list) < capacity:
                # Jeśli jest miejsce w pamięci, dodajemy stronę do referencji
                reference_list.append(ref)
                memory[reference_list.index(ref)] = ref
            else:
                # Znajdowanie strony najmniej używanej do zastąpienia
                check_list = memory[:]
                reversed_list = reference_list[::-1]
                for item in reversed_list:
                    if len(check_list) > 1:
                        if item in check_list:
                            check_list.remove(item)
                # Zamiana strony najmniej używanej na nową
                index_item = memory.index(check_list[0])
                memory[index_item] = ref
                reference_list.remove(check_list[0])
                reference_list.append(ref)
            print(f"{ref}     {' '.join(map(str, memory))}      błąd strony")
        else:
            # Strona znajduje się w pamięci - trafienie strony
            page_hit += 1
            reference_list.remove(ref)
            reference_list.append(ref)
            print(f"{ref}     {' '.join(map(str, memory))}      trafienie strony")

    # Obliczenie i wyświetlenie współczynnika trafień i błędów
    hit_rate = round((page_hit / (page_hit + page_fault)), 2)
    fault_rate = round((page_fault / (page_hit + page_fault)), 2)

    print(f"\nPage hits: {page_hit}")
    print(f"Page faults: {page_fault}")
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

    # Wywołanie funkcji LRU z zebranymi danymi
    lru(user_references, user_capacity)

# Wywołanie funkcji głównej
main()
