import random
import heapq

full_waiting_time = 0  # Całkowity czas oczekiwania na procesy
full_turn_around_time = 0  # Całkowity czas obrotu procesów
processes = []  # Lista procesów

# Pętla pozwalająca wybrać sposób generowania liczby procesów
while True:
    print("Czy chcesz wygenerować losowo liczbę procesów w zakresie (1-100) czy wybrać samodzielnie?\n"
          "1. Wygeneruj losowo\n"
          "2. Wybierz samodzielnie")
    answer1 = int(input("Podaj wybraną opcję (liczbę): "))  # Wybór sposobu generowania liczby procesów
    if answer1 == 1:
        number_of_processes = random.randint(1, 100)  # Losowa liczba procesów w zakresie 1-25
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
            x = random.randint(1, 9)  # Losowy czas nadejścia
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
queue = []  # Kolejka procesów
print("                                 ALGORYTM SJF")  # Tytuł algorytmu SJF
print("")
while check_list or queue:
    # Wyszukaj procesy, które nadeszły w aktualnym czasie
    for process in check_list[:]:
        if process[1] <= time:
            heapq.heappush(queue, (process[2], process))
            check_list.remove(process)

    if not queue:
        time += 1
        continue

    # Wykonaj najkrótszy proces
    _, current_process = heapq.heappop(queue)
    index = processes.index(current_process)

    new_list.append(current_process)

    process_id, arrival_time, burst_time, _, _, _ = current_process

    if time < arrival_time:
        time = arrival_time
        waiting_time = 0
    else:
        waiting_time = time - arrival_time

    time += burst_time
    completion_time = time
    turn_around_time = completion_time - arrival_time

    processes[index][3] = completion_time
    processes[index][4] = turn_around_time
    processes[index][5] = waiting_time

# Wyświetl ostatecznie posortowane wyniki w formie tabeli

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

print(f"Średni czas oczekiwania {average_waiting_time}")
print(f"Średni czas obrotu {average_turn_around_time}")
