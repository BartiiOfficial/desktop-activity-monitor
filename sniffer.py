import os
import time
import ctypes
from datetime import datetime

desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "odwiedzone_strony.txt")
ostatnia_aktywnosc = ""

def pobierz_tytul_okna():
    # Pobiera nazwę aktualnie aktywnego okna na ekranie Windowsa
    hwnd = ctypes.windll.user32.GetForegroundWindow()
    length = ctypes.windll.user32.GetWindowTextLengthW(hwnd)
    buff = ctypes.create_unicode_buffer(length + 1)
    ctypes.windll.user32.GetWindowTextW(hwnd, buff, length + 1)
    return buff.value

print("=== UNIWERSALNY MONITOR AKTYWNOŚCI ===")
print(f"Zapis na Pulpicie: {desktop_path}")
print("Monitoruje przeglądarki, aplikacje i gry (np. Roblox, Claude).")
print("Aby zakończyć, wciśnij w terminalu: CTRL + C\n")

while True:
    try:
        aktualne_okno = pobierz_tytul_okna()
        
        # Jeśli okno się zmieniło i nie jest puste
        if aktualne_okno and aktualne_okno != ostatnia_aktywnosc:
            # Pomijamy puste okna systemowe
            if "Wybór zadań" not in aktualne_okno and "Przełącznik" not in aktualne_okno:
                ostatnia_aktywnosc = aktualne_okno
                teraz = datetime.now().strftime("%H:%M:%S")
                wpis = f"[{teraz}] ---> {aktualne_okno}"
                
                print(wpis)
                
                # Zapis od razu do pliku na Pulpicie
                with open(desktop_path, "a", encoding="utf-8") as f:
                    f.write(wpis + "\n")
    except Exception:
        pass

    # Sprawdza co 1 sekundę
    time.sleep(1)