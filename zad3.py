
# Lista pytań użyta tylko w 3 wersji kodu
pytania = ["Jak masz na imie oraz nazwisko?",
           "Najczęstszym sposobem spędzania wolnego czasu jest dla Ciebie:",
           "W jakich okolicznościach czytasz książki najczęściej?",
           "Jeżeli spędzasz czas wolny czytając książki, jaki jest główny powód takiego wyboru?",
           "Po książki w jakiej formie sięgasz najczęściej?",
           "Ile książek czytasz średnio w ciągu roku?",
           "Jak często średnio czytasz książki?",
           "Po jakie gatunki książek sięgasz najczęściej?"
           ]

# Lista słowników użyta dla sprawdzania poprawności odpowiedzi oraz zamiany
# odwiedzi z jednej litery na pełną (dla uproszczenia wpisywania odpowiedzi)
odpowiedzi = [{},
              {"a": "oglądanie telewizji/filmów/seriali",
               "b": "czytanie książek/czasopism",
               "c": "słuchanie muzyki",
               "d": "spotkania z rodziną/przyjaciółmi",
               "e": "podróżowanie",
               "f": "uprawianie sportu"},
              {"a": "podczas podróży",
               "b": "w czasie wolnym (po pracy, na urlopie)",
               "c": "podczas pracy/nauki (to ich element)",
               "d": "w ogóle nie czytam"},
              {"a": "chęć poszerzenia wiedzy",
               "b": "czytanie mnie relaksuje/odpręża",
               "c": "fakt, że czytanie jest modne",
               "d": "czytanie to moje hobby",
               "e": "konieczność nauki w związku z wykonywaną pracą/studiami",
               "f": "odczuwam presję rodziny/środowiska, żeby czytać"},
              {"a": "papierowej (tradycyjnej)",
               "b": "e-booki (książki elektroniczne) na komputerze",
               "c": "e-booki na tablecie/telefonie",
               "d": "e-booki na specjalnym czytniku (np. Kindle)"},
              {"a": "0",
               "b": "żadnej w cało",
               "c": "1",
               "d": "2-3",
               "e": "4-10",
               "f": ">10"},
              {"a": "codziennie",
               "b": "raz w tygodniu",
               "c": "raz w miesiącu",
               "d": "raz na kilka miesięcy",
               "e": "raz na pół roku",
               "f": "raz na rok",
               "g": "wcale"},
              {"a": "romanse",
               "b": "kryminały/thrillery",
               "c": "psychologiczne",
               "d": "horrory",
               "e": "naukowe",
               "f": "inny"},
              ]

# Najprostsza wersja kodu, bez sprawdzania poprawności, bez pętli i if-ów
'''
odp_0 = input("Ankieta:\n"
              "Proszę wpisywać jako odpowiedzi na pytania 1-7 tylko 1 literę bez nawiasów\n\n"
              "Pytanie 0:\n"
              "Jak masz na imie oraz nazwisko?\n"
              )

odp_1 = input("Pytanie 1:\n"
              "Najczęstszym sposobem spędzania wolnego czasu jest dla Ciebie:\n"
              "a) oglądanie telewizji/filmów/seriali\n"
              "b) czytanie książek/czasopism\n"
              "c) słuchanie muzyki\n"
              "d) spotkania z rodziną/przyjaciółmi\n"
              "e) podróżowanie\n"
              "f) uprawianie sportu\n"
              )

odp_2 = input("Pytanie 2:\n"
              "W jakich okolicznościach czytasz książki najczęściej?\n"
              "a) podczas podróży\n"
              "b) w czasie wolnym (po pracy, na urlopie)\n"
              "c) podczas pracy/nauki (to ich element)\n"
              "d) w ogóle nie czytam\n"
              )

odp_3 = input("Pytanie 3:\n"
              "Jeżeli spędzasz czas wolny czytając książki, jaki jest główny powód takiego wyboru?\n"
              "a) chęć poszerzenia wiedzy\n"
              "b) czytanie mnie relaksuje/odpręża\n"
              "c) fakt, że czytanie jest modne\n"
              "d) czytanie to moje hobby\n"
              "e) konieczność nauki w związku z wykonywaną pracą/studiami\n"
              "f) odczuwam presję rodziny/środowiska, żeby czytać\n"
              )

odp_4 = input("Pytanie 4:\n"
              "Po książki w jakiej formie sięgasz najczęściej?\n"
              "a) papierowej (tradycyjnej)\n"
              "b) e-booki (książki elektroniczne) na komputerze\n"
              "c) e-booki na tablecie/telefonie\n"
              "d) e-booki na specjalnym czytniku (np. Kindle)\n"
              )

odp_5 = input("Pytanie 5:\n"
              "Ile książek czytasz średnio w ciągu roku?\n"
              "a) 0\n"
              "b) żadnej w całości - jedynie fragmenty\n"
              "c) 1\n"
              "d) 2-3\n"
              "e) 4-10\n"
              "f) >10\n"
              )

odp_6 = input("Pytanie 6:\n"
              "Jak często średnio czytasz książki?\n"
              "a) codziennie\n"
              "b) raz w tygodniu\n"
              "c) raz w miesiącu\n"
              "d) raz na kilka miesięcy\n"
              "e) raz na pół roku\n"
              "f) raz na rok\n"
              "f) wcale\n"
              )

odp_7 = input("Pytanie 7:\n"
              "Po jakie gatunki książek sięgasz najczęściej?\n"
              "a) romanse\n"
              "b) kryminały/thrillery\n"
              "c) psychologiczne\n"
              "d) horrory\n"
              "e) naukowe\n"
              "f) inny\n"
              )

print("pytanie: Jak masz na imie oraz nazwisko?\n"
      f"odpowiedź: {odp_0}\n")
print("pytanie: Najczęstszym sposobem spędzania wolnego czasu jest dla Ciebie:\n"
      f"odpowiedź: {odp_1}\n")
print("pytanie: W jakich okolicznościach czytasz książki najczęściej?\n"
      f"odpowiedź: {odp_2}\n")
print("pytanie: Jeżeli spędzasz czas wolny czytając książki, jaki jest główny powód takiego wyboru?\n"
      f"odpowiedź: {odp_3}\n")
print("pytanie: Po książki w jakiej formie sięgasz najczęściej?\n"
      f"odpowiedź: {odp_4}\n")
print("pytanie: Ile książek czytasz średnio w ciągu roku?\n"
      f"odpowiedź: {odp_5}\n")
print("pytanie: Jak często średnio czytasz książki?\n"
      f"odpowiedź: {odp_6}\n")
print("pytanie: Po jakie gatunki książek sięgasz najczęściej?\n"
      f"odpowiedź: {odp_7}\n")
'''

# Dłuższa wersja kodu bez używania pętli for, ale z pętlą while,
# bo bez niej nie dało się zaimplementować sprawdzanie wpisanych danych.
'''
odp_0 = input("Ankieta:\n"
              "Proszę wpisywać jako odpowiedzi na pytania 1-7 tylko 1 literę bez nawiasów\n\n"
              "Pytanie 0:\n"
              "Jak masz na imie oraz nazwisko?\n"
              )

odp_1 = input("Pytanie 1:\n"
              "Najczęstszym sposobem spędzania wolnego czasu jest dla Ciebie:\n"
              "a) oglądanie telewizji/filmów/seriali\n"
              "b) czytanie książek/czasopism\n"
              "c) słuchanie muzyki\n"
              "d) spotkania z rodziną/przyjaciółmi\n"
              "e) podróżowanie\n"
              "f) uprawianie sportu\n"
              )
while odp_1 not in odpowiedzi[1]:
    odp_1 = input("Niepoprawna odpowiedź, prosze wybrać odpowiedź z listy\n")
odp_1 = odpowiedzi[1].get(odp_1)

odp_2 = input("Pytanie 2:\n"
              "W jakich okolicznościach czytasz książki najczęściej?\n"
              "a) podczas podróży\n"
              "b) w czasie wolnym (po pracy, na urlopie)\n"
              "c) podczas pracy/nauki (to ich element)\n"
              "d) w ogóle nie czytam\n"
              )
while odp_2 not in odpowiedzi[2]:
    odp_2 = input("Niepoprawna odpowiedź, prosze wybrać odpowiedź z listy\n")
odp_2 = odpowiedzi[2].get(odp_2)

odp_3 = input("Pytanie 3:\n"
              "Jeżeli spędzasz czas wolny czytając książki, jaki jest główny powód takiego wyboru?\n"
              "a) chęć poszerzenia wiedzy\n"
              "b) czytanie mnie relaksuje/odpręża\n"
              "c) fakt, że czytanie jest modne\n"
              "d) czytanie to moje hobby\n"
              "e) konieczność nauki w związku z wykonywaną pracą/studiami\n"
              "f) odczuwam presję rodziny/środowiska, żeby czytać\n"
              )
while odp_3 not in odpowiedzi[3]:
    odp_3 = input("Niepoprawna odpowiedź, prosze wybrać odpowiedź z listy\n")
odp_3 = odpowiedzi[3].get(odp_3)

odp_4 = input("Pytanie 4:\n"
              "Po książki w jakiej formie sięgasz najczęściej?\n"
              "a) papierowej (tradycyjnej)\n"
              "b) e-booki (książki elektroniczne) na komputerze\n"
              "c) e-booki na tablecie/telefonie\n"
              "d) e-booki na specjalnym czytniku (np. Kindle)\n"
              )
while odp_4 not in odpowiedzi[4]:
    odp_4 = input("Niepoprawna odpowiedź, prosze wybrać odpowiedź z listy\n")
odp_4 = odpowiedzi[4].get(odp_4)

odp_5 = input("Pytanie 5:\n"
              "Ile książek czytasz średnio w ciągu roku?\n"
              "a) 0\n"
              "b) żadnej w całości - jedynie fragmenty\n"
              "c) 1\n"
              "d) 2-3\n"
              "e) 4-10\n"
              "f) >10\n"
              )
while odp_5 not in odpowiedzi[5]:
    odp_5 = input("Niepoprawna odpowiedź, prosze wybrać odpowiedź z listy\n")
odp_5 = odpowiedzi[5].get(odp_5)

odp_6 = input("Pytanie 6:\n"
              "Jak często średnio czytasz książki?\n"
              "a) codziennie\n"
              "b) raz w tygodniu\n"
              "c) raz w miesiącu\n"
              "d) raz na kilka miesięcy\n"
              "e) raz na pół roku\n"
              "f) raz na rok\n"
              "f) wcale\n"
              )
while odp_6 not in odpowiedzi[6]:
    odp_6 = input("Niepoprawna odpowiedź, prosze wybrać odpowiedź z listy\n")
odp_6 = odpowiedzi[6].get(odp_6)

odp_7 = input("Pytanie 7:\n"
              "Po jakie gatunki książek sięgasz najczęściej?\n"
              "a) romanse\n"
              "b) kryminały/thrillery\n"
              "c) psychologiczne\n"
              "d) horrory\n"
              "e) naukowe\n"
              "f) inny\n"
              )
while odp_7 not in odpowiedzi[7]:
    odp_7 = input("Niepoprawna odpowiedź, prosze wybrać odpowiedź z listy\n")
odp_7 = odpowiedzi[7].get(odp_7)

print("pytanie: Jak masz na imie oraz nazwisko?\n"
      f"odpowiedź: {odp_0}\n")
print("pytanie: Najczęstszym sposobem spędzania wolnego czasu jest dla Ciebie:\n"
      f"odpowiedź: {odp_1}\n")
print("pytanie: W jakich okolicznościach czytasz książki najczęściej?\n"
      f"odpowiedź: {odp_2}\n")
print("pytanie: Jeżeli spędzasz czas wolny czytając książki, jaki jest główny powód takiego wyboru?\n"
      f"odpowiedź: {odp_3}\n")
print("pytanie: Po książki w jakiej formie sięgasz najczęściej?\n"
      f"odpowiedź: {odp_4}\n")
print("pytanie: Ile książek czytasz średnio w ciągu roku?\n"
      f"odpowiedź: {odp_5}\n")
print("pytanie: Jak często średnio czytasz książki?\n"
      f"odpowiedź: {odp_6}\n")
print("pytanie: Po jakie gatunki książek sięgasz najczęściej?\n"
      f"odpowiedź: {odp_7}\n")
'''

# Kod ze sprawdzaniem i pętlami

udzielone_odp = []
print("Ankieta:\n"
      "Proszę wpisywać jako odpowiedzi na pytania 1-7 tylko 1 literę bez nawiasów\n\n")

for i in range(0, 8):
    print(f"Pytanie {i}:\n{pytania[i]}")
    for j in odpowiedzi[i]:
        print(j, ") ", odpowiedzi[i].get(j), sep="")

    odp = input()

    if i == 0:
        udzielone_odp.append(odp)
        continue

    while odp not in odpowiedzi[i]:
        odp = input("Niepoprawna odpowiedź, prosze wybrać odpowiedź z listy\n")

    udzielone_odp.append(odpowiedzi[i].get(odp))

for i in range(0, 8):
    print(f"pytanie: {pytania[i]}\n"
          f"odpowiedź: {udzielone_odp[i]}\n")

