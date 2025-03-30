import sys
from fpdf import FPDF

def transliterate(text):
    mapping = {
        "π": "a", "Ê": "c", "Í": "e", "≥": "l", "Ò": "n", "Û": "o", "ú": "s", "ü": "z", "ø": "z",
        "•": "A", "∆": "C", " ": "E", "£": "L", "—": "N", "”": "O", "å": "S", "è": "Z", "Ø": "Z"
    }
    for k, v in mapping.items():
        text = text.replace(k, v)
    return text

class PDF(FPDF):
    def cell_trans(self, w, h, txt, border=0, ln=0, align='', fill=False, link=''):
        # Wypisuje tekst po transliteracji
        super().cell(w, h, transliterate(txt), border, ln, align, fill, link)

# Utworz obiekt PDF
pdf = PDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.set_font("Arial", size=10)

# Tytul
pdf.set_font("Arial", 'B', 14)
pdf.cell(0, 10, transliterate("Sprawozdanie Finansowe - Bilans i RZiS"), ln=True, align="C")
pdf.ln(5)

# --- Sekcja 1: Szczegolowy bilans ñ AKTYWA ---
pdf.set_font("Arial", 'B', 12)
pdf.cell(0, 10, transliterate("1. Szczegolowy bilans ñ AKTYWA"), ln=True)
pdf.ln(2)
pdf.set_font("Arial", '', 10)

aktywa = [
    ["Pozycja", "Nazwa", "31.03.2024 (USD)", "31.03.2023 (USD)"],
    ["A.", "Aktywa trwale", "6023", "6264"],
    ["A.I.", "Wartosci niematerialne i prawne", "4185", "4272"],
    ["A.I.1", "Wartosc firmy (goodwill)", "3792", "3748"],
    ["A.I.2", "Inne wartosci niematerialne i prawne", "393", "524"],
    ["A.II.", "Rzeczowe aktywa trwale", "1194", "1307"],
    ["A.II.1", "Srodki trwale", "979", "1079"],
    ["A.II.2", "Aktywa z tytulu prawa uzytkowania", "215", "228"],
    ["A.III.", "Naleznosci dlugoterminowe", "158", "156"],
    ["A.III.1", "Od pozostalych jednostek", "158", "156"],
    ["A.IV.", "Inwestycje dlugoterminowe", "340", "339"],
    ["A.IV.1", "Udzialy w jednostkach stowarzyszonych", "13", "9"],
    ["A.IV.2", "Inne dlugoterminowe aktywa finansowe", "327", "329"],
    ["A.V.", "Dlugoterminowe rozliczenia miedzyokresowe", "146", "191"],
    ["A.V.1", "Aktywa z tytulu odroczonego podatku dochodowego", "22", "26"],
    ["A.V.2", "Inne rozliczenia miedzyokresowe", "124", "166"],
    ["B.", "Aktywa obrotowe", "7808", "8046"],
    ["B.I.", "Zapasy", "11", "14"],
    ["B.II.", "Naleznosci korterminowe", "2403", "2616"],
    ["B.II.1", "Od pozostalych jednostek", "2403", "2616"],
    ["B.III.", "Inwestycje korterminowe", "5039", "5014"],
    ["B.III.1", "Srodki pieniezne i inne aktywa pieniezne", "1163", "1118"],
    ["B.III.2", "Inne korterminowe aktywa finansowe", "3876", "3896"],
    ["B.IV.", "Korterminowe rozliczenia miedzyokresowe", "355", "400"],
    ["C.", "Nalezne wplaty na kapital", "0", "0"],
    ["D.", "Udzialy (akcje) wlasne", "0", "0"],
    ["", "Aktywa razem", "13831", "14310"]
]

col_widths = [20, 80, 35, 35]
for row in aktywa:
    for i, datum in enumerate(row):
        pdf.cell(col_widths[i], 8, str(datum), border=1)
    pdf.ln(8)

pdf.ln(5)

# --- Sekcja 2: Szczegolowy bilans ñ PASYWA ---
pdf.set_font("Arial", 'B', 12)
pdf.cell(0, 10, transliterate("2. Szczegolowy bilans ñ PASYWA"), ln=True)
pdf.ln(2)
pdf.set_font("Arial", '', 10)

pasywa = [
    ["Pozycja", "Nazwa", "31.03.2024 (USD)", "31.03.2023 (USD)"],
    ["A.", "Kapital (fundusz) wlasny", "9014", "9514"],
    ["A.I.", "Kapital podstawowy", "125", "134"],
    ["A.II.", "Kapital zapasowy", "39", "45"],
    ["A.III.", "Kapital z aktualizacji wyceny", "680", "646"],
    ["A.IV.", "Inne kapitaly rezerwowe", "583", "638"],
    ["A.V.", "Zyski (straty) z lat ubieglych", "6238", "6661"],
    ["A.VI.", "Zysk (strata) netto roku obrotowego", "1333", "1383"],
    ["A.VII.", "Udzialy niesprawujacych kontroli", "16", "7"],
    ["B.", "Zobowiazania i rezerwy na zobowiazania", "4817", "4796"],
    ["B.I.", "Rezerwy na zobowiazania", "234", "215"],
    ["B.I.1", "Rezerwa z tytulu odroczonego podatku", "210", "184"],
    ["B.I.2", "Rezerwy na swiadczenia emerytalne", "0", "0"],
    ["B.I.3", "Pozostale rezerwy", "24", "31"],
    ["B.II.", "Zobowiazania dlugoterminowe", "1421", "1239"],
    ["B.II.1", "Wobec jednostek zaleznym", "0", "0"],
    ["B.II.2", "Wobec jednostek wspolzaleznych", "0", "0"],
    ["B.II.3", "Wobec pozostalych jednostek", "1421", "1239"],
    ["B.III.", "Zobowiazania korterminowe", "2794", "2952"],
    ["B.III.1", "Wobec jednostek zaleznym", "0", "0"],
    ["B.III.2", "Wobec jednostek wspolzaleznych", "0", "0"],
    ["B.III.3", "Wobec pozostalych jednostek", "2794", "2952"],
    ["B.IV.", "Rozliczenia miedzyokresowe", "368", "390"],
    ["B.IV.1", "Ujemna wartosc firmy", "0", "0"],
    ["B.IV.2", "Inne rozliczenia miedzyokresowe", "368", "390"],
    ["", "Pasywa razem", "13831", "14310"]
]

for row in pasywa:
    for i, datum in enumerate(row):
        pdf.cell(col_widths[i], 8, str(datum), border=1)
    pdf.ln(8)

pdf.ln(5)

# --- Sekcja 3: Szczegolowy Rachunek Zyskow i Strat (wariant kalkulacyjny) ---
pdf.set_font("Arial", 'B', 12)
pdf.cell(0, 10, transliterate("3. Szczegolowy Rachunek Zyskow i Strat (wariant kalkulacyjny)"), ln=True)
pdf.ln(2)
pdf.set_font("Arial", '', 10)

rzis = [
    ["Pozycja", "Nazwa", "2023/2024 (USD)", "2022/2023 (USD)"],
    ["A.", "Przychody netto ze sprzedazy", "10770", "11012"],
    ["B.", "Koszt wlasny sprzedanych produktow", "7577", "7855"],
    ["C.", "Zysk brutto ze sprzedazy", "3193", "3157"],
    ["D.", "Koszty sprzedazy", "840", "793"],
    ["E.", "Koszty ogolnego zarzadu", "724", "720"],
    ["F.", "Zysk ze sprzedazy", "1629", "1644"],
    ["G.", "Pozostale przychody operacyjne", "4", "54"],
    ["H.", "Pozostale koszty operacyjne", "0", "0"],
    ["I.", "Zysk z dzialalnosci operacyjnej", "1633", "1698"],
    ["J.", "Przychody finansowe", "287", "221"],
    ["K.", "Koszty finansowe", "151", "123"],
    ["L.", "Zysk z dzialalnosci gospodarczej", "1766", "1797"],
    ["M.", "Zyski nadzwyczajne", "0", "0"],
    ["N.", "Straty nadzwyczajne", "0", "0"],
    ["O.", "Zysk nadzwyczajny", "0", "0"],
    ["P.", "Zysk brutto", "1766", "1797"],
    ["Q.", "Obowiazkowe obciazenia (podatek)", "433", "414"],
    ["R.", "Zysk netto", "1333", "1383"]
]

for row in rzis:
    for i, datum in enumerate(row):
        pdf.cell(col_widths[i], 8, str(datum), border=1)
    pdf.ln(8)

pdf.output("sprawozdanie.pdf")
print("PDF zostal wygenerowany jako sprawozdanie.pdf")
