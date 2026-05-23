# Porównanie algorytmów BFS i DFS w labiryncie

Projekt zaliczeniowy z przedmiotu **Sztuczna Inteligencja**.

Autorzy:

- Jędrzej Chodkowski 30377
- Aleks Białkowski 3378

## Cel projektu

Celem projektu jest samodzielna implementacja oraz porównanie dwóch algorytmów przeszukiwania grafów: **Breadth-First Search (BFS)** i **Depth-First Search (DFS)**. Algorytmy rozwiązują problem znalezienia ścieżki w labiryncie reprezentowanym jako dwuwymiarowa siatka.

Porównywane są:

- długość znalezionej ścieżki,
- liczba odwiedzonych pól,
- czas działania algorytmu.

## Struktura projektu

```text
src/maze_ai/
  maze.py          # model labiryntu
  search.py        # implementacja BFS i DFS
  experiments.py   # przykładowe labirynty i porównanie wyników
  main.py          # uruchomienie programu

tests/
  test_maze.py     # testy modelu labiryntu
  test_search.py   # testy algorytmów
```

## Uruchomienie projektu

W repozytorium z projektem uruchom:

```bash
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
# .venv\Scripts\activate    # Windows
pip install -e .[dev]
python -m maze_ai.main
```

## Uruchomienie testów

```bash
pytest
```

## Sprawdzenie jakości kodu

```bash
ruff check .
```

## Podział pracy

- Jędrzej Chodkowski: przygotowanie opisu problemu, testów i analizy wyników.
- Aleks Białkowski: implementacja modelu labiryntu, algorytmów BFS/DFS oraz eksperymentu porównawczego.

## Najważniejszy wniosek

BFS gwarantuje znalezienie najkrótszej ścieżki w grafie nieważonym, dlatego w problemie labiryntu jest lepszy, gdy najważniejsza jest optymalna długość trasy. DFS również może znaleźć rozwiązanie, ale nie gwarantuje najkrótszej ścieżki, ponieważ eksploruje jedną gałąź grafu możliwie głęboko przed sprawdzeniem innych możliwości.
