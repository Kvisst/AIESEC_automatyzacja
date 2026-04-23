def zbierz_metadane():
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
        osoba = input("Dodaj osobę do listy obecności (lub 'n' aby skończyć): ")
        if osoba.lower() == 'n': break
        lista.append(osoba)

    agenda = []
    while True:
        punkt = input("Dodaj punkt z porządku obrad (lub 'n' aby skończyć): ")
        if punkt.lower() == 'n': break
        agenda.append(punkt)

    return {
        'numer': numer,
        'data': data,
        'przewodniczący': przewodniczący,
        'protokolant': protokolant,
        'lista': lista,
        'agenda': "\n".join(agenda)
    }


def zbierz_uchwaly(typ_glosowania):
    lista = []
    try:
        ilosc = int(input(f"Ile wniosków na głosowanie {typ_glosowania}? "))
    except ValueError:
        return []

    for i in range(ilosc):
        print(f"Wniosek nr {i + 1}:")
        lista.append({
            'tresc': input("Treść: "),
            'wnioskodawca': input("Wnioskodawca: ")
        })
    return lista