
# WSI 2023Z LAB2 - Algorytm ewolucyjny
### Maksym Bieńkowski

## Zawartość archiwum

### Folder src
- specimen.py - abstrakcyjna klasa reprezentująca osobnika populacji i dziedzicząca po niej klasa reprezentująca osobnika dla problemu komiwojażera
- population.py - analogicznie - klasa abstrakcyjna reprezentująca populację oraz dziedzicząca klasa do problemu komiwojażera
- evolution.py - klasa odpowiedzialna za wielokrotne ewoluowanie populacji, zawierająca główną pętlę algorytmu
- constants.py - stałe

### main.py
Uruchamialny skrypt tworzący obiekt ewolucji i przeprowadzający ewolucję o podanych przez użytkownika parametrach. Po ukończeniu
ewolucji wyświetla wykres obrazujący postęp algorytmu na przestrzeni kolejnych pokoleń.
#### Flagi: 
- `-p [int]` - rozmiar populacji
- `-s [float]` - siła mutacji
- `-e [int]` - liczba pokoleń do obliczenia
Wszystkie argumenty posiadają domyślne wartości zadane w pliku `src/constants.py`, więc aby uruchomić skrypt dla nich,
należy po prostu z linii komendy uruchomić skrypt: `python3 -m main`
Przykładowe zawołanie skryptu dla 300 pokoleń populacji 130 osobników o sile mutacji 0.3:
`python3 -m main -p 130 -s 0.3 -e 300`

## Krótki opis rozwiązania
Zastosowano algorytm ewolucyjny bez krzyżowania, o mutacji polegającej na zamianie losowych par genów
oraz sukcesji elitarnej, wybierającej n najlepszych osobników z połączonej populacji rodziców i dzieci. Dla podanych
w treści zadania przykładowych danych radzi on sobie bardzo zadowalająco ze znajdowaniem optymalnych, lub przynajmniej dobrych ścieżek.
