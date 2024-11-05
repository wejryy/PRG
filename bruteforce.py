import hashlib
import random
import string
from concurrent.futures import ThreadPoolExecutor, as_completed

# Konstanty
DELKA_TEXTU = 10
POZADOVANY_HASH = "d364ad912ca36035306d40332185e260"
POCET_VLAKEN = 8  # Počet vláken pro paralelní zpracování
PULSNI_KROK = 1000

# Funkce pro vytvoření MD5 hashe z textu
def vytvor_md5_hash(text):
    return hashlib.md5(text.encode('utf-8')).hexdigest()

# Funkce pro generování náhodného textu
def generuj_nahodny_text(délka=DELKA_TEXTU):
    znaky = string.ascii_letters + string.digits
    return ''.join(random.choice(znaky) for _ in range(délka))

# Funkce pro kontrolu jednoho pokusu
def kontroluj_pokus():
    nahodny_text = generuj_nahodny_text()
    hash_result = vytvor_md5_hash(nahodny_text)
    return nahodny_text, hash_result

# Hlavní funkce pro paralelní hledání
def najdi_hash_parallelne():
    pokusy = 0
    with ThreadPoolExecutor(max_workers=POCET_VLAKEN) as executor:
        while True:
            # Spuštění několika paralelních pokusů
            futures = [executor.submit(kontroluj_pokus) for _ in range(POCET_VLAKEN)]
            
            # Zpracování výsledků jednotlivých vláken
            for future in as_completed(futures):
                pokusy += 1
                nahodny_text, hash_result = future.result()
                
                # Pokud najdeme požadovaný hash, vrátíme výsledek a ukončíme
                if hash_result == POZADOVANY_HASH:
                    print(f"\nNalezen správný hash!\nText: {nahodny_text} | Hash: {hash_result} | Počet pokusů: {pokusy}")
                    return
                
                # Výpis stavu každých PULSNI_KROK pokusů
                if pokusy % PULSNI_KROK == 0:
                    print(f"Počet pokusů: {pokusy} | Aktuální text: {nahodny_text} | Aktuální hash: {hash_result}")

# Spustíme hlavní funkci
najdi_hash_parallelne()
