"""Punkt startowy projektu."""

from __future__ import annotations

from maze_ai.experiments import MAZES, format_results, run_all_experiments, summarize
from maze_ai.maze import Maze
from maze_ai.search import bfs, dfs


def show_example_path() -> None:
    maze = Maze.from_text(MAZES["z_przeszkodami"])
    bfs_result = bfs(maze)
    dfs_result = dfs(maze)

    print("Przykladowy labirynt:")
    print(maze.render_with_path(None))
    print("\nSciezka BFS:")
    print(maze.render_with_path(bfs_result.path))
    print("\nSciezka DFS:")
    print(maze.render_with_path(dfs_result.path))


def main() -> None:
    results = run_all_experiments()
    show_example_path()
    print("\nWyniki eksperymentu:")
    print(format_results(results))
    print("\nPodsumowanie:")
    print(summarize(results))


if __name__ == "__main__":
    main()
