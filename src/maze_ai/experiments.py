"""Eksperyment porownujacy BFS i DFS na kilku labiryntach testowych."""

from __future__ import annotations

from statistics import mean

from maze_ai.maze import Maze
from maze_ai.search import SearchResult, bfs, dfs

MAZES: dict[str, str] = {
    "prosty": """
S....
###.#
....G
""",
    "z_przeszkodami": """
S..#.....
.#.#.###.
.#...#...
.#####.#.
.......#G
""",
    "dluzszy_korytarz": """
S........#....
.######..#.##.
......#..#..#.
.####.#.###.#.
....#........G
""",
    "bez_rozwiazania": """
S.#
###
#.G
""",
}


def run_single_experiment(name: str, maze_text: str) -> list[SearchResult]:
    maze = Maze.from_text(maze_text)
    return [bfs(maze), dfs(maze)]


def run_all_experiments() -> dict[str, list[SearchResult]]:
    return {name: run_single_experiment(name, text) for name, text in MAZES.items()}


def format_results(results: dict[str, list[SearchResult]]) -> str:
    lines = [
        "Labirynt | Algorytm | Znaleziono | Dlugosc sciezki | Odwiedzone wezly | Czas [ms]",
        "--- | --- | --- | ---: | ---: | ---:",
    ]
    for maze_name, maze_results in results.items():
        for result in maze_results:
            lines.append(
                f"{maze_name} | {result.algorithm} | {'tak' if result.found else 'nie'} | "
                f"{result.path_length if result.path_length is not None else '-'} | "
                f"{result.visited_nodes} | {result.elapsed_ms:.4f}"
            )
    return "\n".join(lines)


def summarize(results: dict[str, list[SearchResult]]) -> str:
    bfs_lengths = [
        r.path_length 
        for values in results.values() 
        for r in values 
        if r.algorithm == "BFS" and r.found]
    
    dfs_lengths = [
        r.path_length 
        for values in results.values() 
        for r in values 
        if r.algorithm == "DFS" and r.found]
    bfs_visited = [
        r.visited_nodes 
        for values in results.values() 
        for r in values 
        if r.algorithm == "BFS"]
    dfs_visited = [
        r.visited_nodes 
        for values in results.values() 
        for r in values 
        if r.algorithm == "DFS"]

    return (
        "Srednie wyniki dla labiryntow, w ktorych znaleziono sciezke:\n"
        f"- BFS: srednia dlugosc sciezki = {mean(bfs_lengths):.2f}, "
        f"srednio odwiedzone wezly = {mean(bfs_visited):.2f}\n"
        f"- DFS: srednia dlugosc sciezki = {mean(dfs_lengths):.2f}, "
        f"srednio odwiedzone wezly = {mean(dfs_visited):.2f}"
    )
