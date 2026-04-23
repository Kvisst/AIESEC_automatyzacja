from docxtpl import DocxTemplate

def generuj_z_szablonu(sciezka_szablonu, sciezka_wyjscia, kontekst):
    try:
        doc = DocxTemplate(sciezka_szablonu)
        doc.render(kontekst)
        doc.save(sciezka_wyjscia)
        print(f"Sukces! Dokument zapisany jako: {sciezka_wyjscia}")
    except Exception as e:
        print(f"Wystąpił błąd podczas generowania: {e}")