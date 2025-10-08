print("Esercizio 1 --- Negozio 1")

def calcola_sconto_negozio1(spesa: float) -> str:
    """Calcola il totale da pagare nel negozio 1 in base alla spesa."""
    if not spesa or spesa <= 0:
        return "Errore: la spesa deve essere un valore positivo e diverso da zero."

    sconto_percentuale = 20 if spesa > 500 else 10
    sconto = spesa * sconto_percentuale / 100
    totale = spesa - sconto

    return (
        f"Spesa iniziale: €{spesa:.2f}\n"
        f"Sconto applicato: {sconto_percentuale}% (€{sconto:.2f})\n"
        f"Totale da pagare: €{totale:.2f}"
    )

# Esempio di utilizzo
try:
    spesa_input = float(input("Inserisci l'importo della spesa: "))
    print("\n" + calcola_sconto_negozio1(spesa_input))
except ValueError:
    print("Errore: inserire un numero valido per la spesa.")

print("\n")


# ------------------------------------------------------------
# Esercizio 2 --- Negozio 2
# ------------------------------------------------------------

print("Esercizio 2 --- Negozio 2")

def calcola_sconto_negozio2(spesa: float) -> float:
    """Calcola lo sconto nel negozio 2 con soglia a 300 euro."""
    if spesa <= 300:
        return spesa * 0.10
    sconto_10 = 300 * 0.10
    sconto_20 = (spesa - 300) * 0.20
    return sconto_10 + sconto_20

try:
    spesa = float(input("Inserisci l'importo della spesa: "))

    if spesa <= 0:
        print("Errore: l'importo della spesa deve essere maggiore di zero.")
    else:
        sconto = calcola_sconto_negozio2(spesa)
        totale = spesa - sconto
        print(f"Spesa: €{spesa:.2f}")
        print(f"Sconto: €{sconto:.2f}")
        print(f"Importo finale: €{totale:.2f}")

except ValueError:
    print("Errore: inserisci un numero valido.")

print("\n")


# ------------------------------------------------------------
# Esercizio 3 --- Comparazione Negozi
# ------------------------------------------------------------

print("Esercizio 3 --- Comparazione Negozi")

try:
    spesa = float(input("Inserisci l'importo della spesa: "))

    if spesa <= 0:
        print("Errore: l'importo della spesa deve essere maggiore di zero.")
    else:
        sconto1 = calcola_sconto_negozio1(spesa_input=spesa)
        sconto1_valore = spesa * (20/100 if spesa > 500 else 10/100)
        totale1 = spesa - sconto1_valore

        sconto2 = calcola_sconto_negozio2(spesa)
        totale2 = spesa - sconto2

        print("\n--- Riepilogo ---")
        print(f"Negozio 1: Sconto €{sconto1_valore:.2f}, Totale da pagare €{totale1:.2f}")
        print(f"Negozio 2: Sconto €{sconto2:.2f}, Totale da pagare €{totale2:.2f}")

        print("\n--- Confronto ---")
        if abs(totale1 - totale2) < 0.01:
            print("È indifferente: il totale da pagare è praticamente lo stesso.")
        elif totale1 < totale2:
            print("Conviene acquistare nel **Negozio 1**.")
        else:
            print("Conviene acquistare nel **Negozio 2**.")

except ValueError:
    print("Errore: inserisci un numero valido.")
