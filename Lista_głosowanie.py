from docxtpl import DocxTemplate
from Zbieranie_D import zbieranie_danych


def przygotuj_dane(dane):
    uczestnicy = dane.get("uczestnicy", [])

    wnioski_out = []
    for wniosek in dane.get("wnioski", []):
        glosy = wniosek.get("glosy", [])

        wynik = {
            "za": sum(1 for g in glosy if g["glos"] == "za"),
            "przeciw": sum(1 for g in glosy if g["glos"] == "przeciw"),
            "wstrzymal": sum(1 for g in glosy if g["glos"] == "wstrzymal")
        }

        wnioski_out.append({
            "tytul": wniosek["tytul"],
            "opis": wniosek.get("opis", ""),
            "wynik": wynik
        })

    return {
        "data": dane.get("data"),
        "uczestnicy": uczestnicy,
        "wnioski": wnioski_out
    }


def generuj_protokol(sciezka_wejscia, sciezka_wyjscia, dane):
    dokument = DocxTemplate(sciezka_wejscia)

    dane_do_szablonu = przygotuj_dane(dane)

    dokument.render(dane_do_szablonu)
    dokument.save(sciezka_wyjscia)


if __name__ == "__main__":
    dane = zbieranie_danych()
    generuj_protokol('testowy.docx', 'test1.docx', dane)