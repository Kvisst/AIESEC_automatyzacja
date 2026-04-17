from docxtpl import DocxTemplate
from zbieranie_danych import zbieranie_danych

dane = zbieranie_danych()

def generuj_protokol(sciezka_wejscia, sciezka_wyjscia, dane):

    dokument = DocxTemplate(sciezka_wejscia)
    dokument.render(dane)
    dokument.save(sciezka_wyjscia)
    print("Protokół został wygenerowany!")


generuj_protokol('szablon.docx', 'protokół.docx', dane)