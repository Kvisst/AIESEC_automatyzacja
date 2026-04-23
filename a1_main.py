from a3_zbieranie_danych import zbierz_metadane, zbierz_uchwaly
from a2_generator import generuj_z_szablonu


def main():
    meta = zbierz_metadane()
    jawne = zbierz_uchwaly("Jawne")
    niejawne = zbierz_uchwaly("Niejawne")

    context = {
        **meta,
        'jawne': jawne,
        'niejawne': niejawne
    }

    generuj_z_szablonu("szablon_scalanie.docx", "protokół_finalny.docx", context)

if __name__ == "__main__":
    main()