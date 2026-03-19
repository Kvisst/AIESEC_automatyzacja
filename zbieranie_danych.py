def zbieranie_danych():

    print("Podaj datę zebrania: ")
    data = input()

    print("Podaj numer zebrania: ")
    numer = input()

    print("Kto będzie przewodniczącym?: ")
    przewodniczący = input()

    print("Kto będzie protokolantem?: ")
    protokolant = input()

    lista = []

    while True:
        osoba = input("Dodaj osobę do listy obecności: ")
        lista.append(osoba)

        decyzja = input("Czy dodać kolejną osobę? (t/n): ").lower()
        if decyzja == 'n':
            break
    lista.sort(key=lambda x: x.split()[-1].lower())

    agenda = []

    while True:
        punkt = input("Dodaj punkt z porządku obrad (z numerem): ")
        agenda.append(punkt)

        decyzja = input("Czy dodać kolejny? (t/n): ").lower()
        if decyzja == 'n':
            break

    zatwierdzenie = agenda[1].removeprefix("II. ")
    druga = agenda[1].removeprefix("III. ")

    lista_zformatowana = "\n".join(lista)
    agenda_zformatowana = "\n".join(agenda)

    wynik = {
        'numer': numer,
        'data': data,
        'przewodniczący': przewodniczący,
        'protokolant': protokolant,
        'lista': lista_zformatowana,
        'liczba': len(lista),
        'agenda': agenda_zformatowana,
        'zatwierdzenie': zatwierdzenie,
        'druga': druga,
    }

    return wynik