import random
full_waiting_time = 0  # Inicjalizacja całkowitego czasu oczekiwania na procesy
full_turn_around_time = 0  # Inicjalizacja całkowitego czasu obrotu procesów
processes = []  # Lista procesów

# Pętla pozwalająca wybrać sposób generowania liczby procesów
while True:
    print("Czy chcesz wygenerować losowo liczbę procesów w zakresie (1-100) czy wybrać samodzielnie?\n"
          "1. Wygeneruj losowo\n"
          "2. Wybierz samodzielnie")
    answer1 = int(input("Podaj wybraną opcję (liczbę): "))  # Wybór sposobu generowania liczby procesów
    if answer1 == 1:
        number_of_processes = random.randint(1, 100)  # Losowa liczba procesów w zakresie 1-100
        break
    elif answer1 == 2:
        number_of_processes = int(input("Podaj liczbę procesów: "))  # Wprowadzenie liczby procesów
        break
    else:
        print("Podaj prawidłową liczbę.")
        continue

# Pętla pozwalająca wybrać sposób generowania czasów nadejścia i wykonywania procesów
while True:
    print("Czy chcesz wygenerować wartości czasu nadejścia i wykonania losowo czy samodzielnie?\n"
          "1. Wygeneruj losowo\n"
          "2. Wybierz samodzielnie")
    answer2 = int(input("Podaj wybraną opcję (liczbę): "))  # Wybór sposobu generowania czasów
    if answer2 == 1:
        for i in range(1, number_of_processes + 1):  # Dla każdego procesu
            x = random.randint(0, 9)  # Losowy czas nadejścia
            y = random.randint(1, 9)  # Losowy czas wykonywania
            user_process = [i, x, y, 0, 0, 0]  # Tworzenie listy procesu
            processes.append(user_process)  # Dodawanie listy procesu do listy procesów
        break
    elif answer2 == 2:
        for i in range(1, number_of_processes + 1):  # Dla każdego procesu
            x = int(input("Podaj wartość czasy nadejścia: "))  # Wprowadzenie czasu nadejścia
            y = int(input("Podaj wartość czasy wykonywania: "))  # Wprowadzenie czasu wykonywania
            user_process = [i, x, y, 0, 0, 0]  # Tworzenie listy procesu
            processes.append(user_process)  # Dodawanie listy procesu do listy procesów
        break
    else:
        print("Podaj prawidłową liczbę.")

print("")

time = 0  # Aktualny czas
check_list = processes.copy()  # Kopia listy procesów do sprawdzania
new_list = []  # Nowa lista procesów
queue_time = 0  # Czas kolejki
print("                                 ALGORYTM FCFS")  # Tytuł algorytmu FCFS
print("")
while check_list:
    queue = []  # Inicjalizacja kolejki procesów
    for process in check_list:
        if process[1] <= queue_time:  # Sprawdzenie, czy proces dotarł do kolejki
            queue.append(process)

    if not queue:  # Jeśli kolejka jest pusta
        queue_time += 1  # Zwiększenie czasu kolejki o 1 jednostkę
        if queue_time > max(process[1] for process in processes if process[3] == 0):  # Sprawdzenie warunku zakończenia algorytmu
            break
        continue

    current_process = queue[0]  # Wybierz pierwszy proces z kolejki
    check_list.remove(current_process)  # Usuń ten proces z listy sprawdzającej
    index = processes.index(current_process)  # Pobierz indeks tego procesu
    new_list.append(current_process)  # Dodaj ten proces do nowej listy procesów

    process_id, arrival_time, burst_time, _, _, _ = current_process  # Pobierz dane tego procesu
    if time < arrival_time:  # Jeśli aktualny czas jest mniejszy niż czas nadejścia procesu
        time = arrival_time  # Ustaw aktualny czas na czas nadejścia procesu
        waiting_time = 0  # Ustaw czas oczekiwania na 0
    else:
        waiting_time = time - arrival_time  # Oblicz czas oczekiwania

    time += burst_time  # Zwiększ czas o wykonanie czasu trwania procesu
    completion_time = time  # Ustaw czas zakończenia na aktualny czas
    turn_around_time = completion_time - arrival_time  # Oblicz czas obrotu procesu

    processes[index][3] = completion_time  # Zapisz czas zakończenia w procesie
    processes[index][4] = turn_around_time  # Zapisz czas obrotu
    processes[index][5] = waiting_time

for process in new_list:
    new_index = processes.index(process)
    full_waiting_time = full_waiting_time + processes[new_index][5]
    full_turn_around_time = full_turn_around_time + processes[new_index][4]

average_waiting_time = full_waiting_time / number_of_processes
average_turn_around_time = full_turn_around_time / number_of_processes


header = ["Process ID", "Arrival Time", "Burst Time", "Completion Time", "Turnaround Time", "Waiting Time"]
separator = "-" * 93

print(separator)
print("| {:^10} | {:^12} | {:^10} | {:^15} | {:^15} | {:^12} |".format(*header))
print(separator)
for process in new_list:
    print("| {:^10} | {:^12} | {:^10} | {:^15} | {:^15} | {:^12} |".format(*process))
    print(separator)

print(f"Average waiting time {average_waiting_time}")
print(f"Average turn around time {average_turn_around_time}")
