def mikado(numero_bastoncini, numero_regole, dipendenza_sopra, dipendenza_sotto):
    # Lista che tiene traccia del numero di dipendenze rimaste per ogni bastoncino
    bastoncini_liberi = [0] * numero_bastoncini  

    # Aggiorniamo il numero di dipendenze per ogni bastoncino
    for regola in range(numero_regole):
        bastoncino_sopra = dipendenza_sopra[regola]  # Bastoncino che ha dipendenze sopra di sé
        bastoncino_sotto = dipendenza_sotto[regola]  # Bastoncino che ha dipendenze sotto di sé
       
        # Incrementiamo il numero di dipendenze per il bastoncino sotto
        bastoncini_liberi[bastoncino_sotto] += 1
   

    # Step 2: Creiamo una lista di bastoncini che non hanno dipendenze (bastoncini_liberi == 0)
    bastoncini_da_rimuovere = []  # Lista dei bastoncini che possiamo rimuovere subito
    for i in range(numero_bastoncini):
        if bastoncini_liberi[i] == 0:
            bastoncini_da_rimuovere.append(i)  # Aggiungiamo i bastoncini senza dipendenze alla lista
    

    # Step 3: Ordinamento dei bastoncini in base alle regole di dipendenza
    ordine_di_rimozione = []  # Qui salviamo l'ordine in cui rimuoviamo i bastoncini

    while bastoncini_da_rimuovere:
        bastoncino = bastoncini_da_rimuovere.pop(0)  # Rimuoviamo il primo bastoncino dalla lista
        ordine_di_rimozione.append(bastoncino)  # Aggiungiamo il bastoncino rimosso all'ordine di rimozione
       
        # Aggiorniamo il numero di dipendenze per ogni bastoncino che dipende da quello appena rimosso
        for regola in range(numero_regole):
            if dipendenza_sopra[regola] == bastoncino:  # Se il bastoncino rimosso è quello sopra
                bastoncino_sotto = dipendenza_sotto[regola]  # Troviamo il bastoncino sotto
                bastoncini_liberi[bastoncino_sotto] -= 1  # Riduciamo il numero di dipendenze
                if bastoncini_liberi[bastoncino_sotto] == 0:
                    bastoncini_da_rimuovere.append(bastoncino_sotto)  # Se il bastoncino sotto non ha più dipendenze, lo aggiungiamo alla lista
    

    # Se abbiamo rimosso tutti i bastoncini, restituiamo l'ordine di rimozione
    if len(ordine_di_rimozione) == numero_bastoncini:
        return ordine_di_rimozione
    else:
        return "Impossibile trovare un ordine valido"  # Se non possiamo rimuovere tutti i bastoncini, restituiamo un errore

# Esempio di utilizzo
numero_bastoncini = 10
numero_regole = 6
dipendenza_sopra = [8, 4, 3, 2, 6, 3]
dipendenza_sotto = [5, 8, 8, 7, 8, 7]

ordine = mikado(numero_bastoncini, numero_regole, dipendenza_sopra, dipendenza_sotto)
print(ordine)
