# Raport z projektu: Porównanie BFS i DFS w labiryncie

## 1. Opis problemu

Projekt dotyczy problemu znajdowania ścieżki w labiryncie. Labirynt jest zapisany jako dwuwymiarowa siatka znaków. Punkt `S` oznacza start, punkt `G` oznacza cel, znak `#` oznacza ścianę, a pozostałe pola są możliwe do przejścia.

Zadaniem algorytmu jest znalezienie poprawnej ścieżki od startu do celu, jeśli taka ścieżka istnieje.

## 2. Opis danych

W projekcie wykorzystano kilka przykładowych labiryntów zapisanych bezpośrednio w kodzie. Dane są celowo proste, aby można było łatwo przeanalizować działanie algorytmów podczas prezentacji. Przygotowano labirynt prosty, labirynt z przeszkodami, dłuższy korytarz oraz przypadek bez rozwiązania.

## 3. Uzasadnienie wyboru algorytmów

BFS i DFS są klasycznymi algorytmami sztucznej inteligencji używanymi do przeszukiwania przestrzeni stanów. W tym projekcie stanem jest aktualne pole labiryntu, a przejścia między stanami odpowiadają ruchom do sąsiednich pól.

BFS został wybrany, ponieważ w grafie nieważonym znajduje najkrótszą ścieżkę. DFS został wybrany jako algorytm porównawczy, ponieważ działa inaczej: idzie możliwie głęboko jedną ścieżką, a dopiero później się cofa.

## 4. Krótkie wyjaśnienie działania metody

BFS korzysta z kolejki FIFO. Najpierw sprawdza wszystkie pola oddalone o jeden krok od startu, później o dwa kroki itd. Dzięki temu pierwsze dojście do celu oznacza znalezienie najkrótszej ścieżki.

DFS korzysta ze stosu LIFO. Algorytm wybiera jednego sąsiada i kontynuuje przechodzenie coraz dalej, dopóki może. Jeśli trafi na ślepą uliczkę, cofa się i sprawdza kolejne możliwości.

W obu algorytmach zapisywany jest słownik `parent`, który pozwala odtworzyć ścieżkę od celu z powrotem do startu.

## 5. Opis testów

Przygotowano testy jednostkowe w `pytest`. Testy sprawdzają:

- poprawne wczytywanie labiryntu,
- wykrywanie punktu startowego i celu,
- pomijanie ścian i pól poza planszą,
- znajdowanie ścieżki przez BFS,
- znajdowanie poprawnej ścieżki przez DFS,
- obsługę labiryntu bez rozwiązania,
- fakt, że BFS nie znajduje ścieżki dłuższej niż DFS w przykładowym labiryncie rozgałęzionym.

## 6. Wyniki eksperymentu

Po uruchomieniu programu komendą:

```bash
python -m maze_ai.main
```

program wypisuje porównanie algorytmów dla kilku labiryntów. Mierzone są:

- informacja, czy znaleziono ścieżkę,
- długość ścieżki,
- liczba odwiedzonych węzłów,
- czas działania w milisekundach.

Przykładowo BFS zazwyczaj znajduje krótszą lub równą ścieżkę w porównaniu z DFS. DFS może odwiedzić mniej pól w niektórych przypadkach, ale nie daje gwarancji optymalności trasy.

## 7. Wnioski

BFS jest lepszym wyborem, gdy zależy nam na znalezieniu najkrótszej ścieżki w labiryncie. Jego wadą może być większe zużycie pamięci, ponieważ przechowuje wiele pól na tym samym poziomie odległości.

DFS jest prosty i może szybko znaleźć jakąkolwiek ścieżkę, ale nie gwarantuje, że będzie ona najkrótsza. W labiryntach z wieloma rozgałęzieniami DFS może pójść bardzo długą drogą, zanim znajdzie cel.

Projekt pokazuje, że wybór algorytmu powinien zależeć od celu: jeśli najważniejsza jest najkrótsza ścieżka, lepszy jest BFS; jeśli wystarczy jakiekolwiek rozwiązanie i chcemy prostego przeszukiwania, można użyć DFS.
