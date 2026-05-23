"""Samodzielna implementacja BFS i DFS dla problemu szukania sciezki."""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from time import perf_counter

from maze_ai.maze import Maze, Position


@dataclass(frozen=True)
class SearchResult:
    algorithm: str
    path: list[Position] | None
    visited_nodes: int
    elapsed_ms: float

    @property
    def path_length(self) -> int | None:
        """Liczba krokow od startu do celu."""
        if self.path is None:
            return None
        return len(self.path) - 1

    @property
    def found(self) -> bool:
        return self.path is not None


def reconstruct_path(parent: dict[Position, Position | None], goal: Position) -> list[Position]:
    path: list[Position] = []
    current: Position | None = goal
    while current is not None:
        path.append(current)
        current = parent[current]
    path.reverse()
    return path


def bfs(maze: Maze) -> SearchResult:
    """Breadth-First Search: przeszukuje graf poziomami i znajduje najkrotsza sciezke."""
    start_time = perf_counter()
    queue: deque[Position] = deque([maze.start])
    parent: dict[Position, Position | None] = {maze.start: None}
    visited_nodes = 0

    while queue:
        current = queue.popleft()
        visited_nodes += 1

        if current == maze.goal:
            elapsed_ms = (perf_counter() - start_time) * 1000
            return SearchResult(
                "BFS", 
                reconstruct_path(parent, maze.goal), 
                visited_nodes, 
                elapsed_ms,
            )

        for neighbor in maze.neighbors(current):
            if neighbor not in parent:
                parent[neighbor] = current
                queue.append(neighbor)

    elapsed_ms = (perf_counter() - start_time) * 1000
    return SearchResult("BFS", None, visited_nodes, elapsed_ms)


def dfs(maze: Maze) -> SearchResult:
    """Depth-First Search: idzie mozliwie gleboko, a dopiero potem sie cofa."""
    start_time = perf_counter()
    stack: list[Position] = [maze.start]
    parent: dict[Position, Position | None] = {maze.start: None}
    visited_nodes = 0

    while stack:
        current = stack.pop()
        visited_nodes += 1

        if current == maze.goal:
            elapsed_ms = (perf_counter() - start_time) * 1000
            return SearchResult(
                "DFS", 
                reconstruct_path(parent, maze.goal), 
                visited_nodes, 
                elapsed_ms,
            )

        # Odwracamy kolejnosc, aby DFS przy stosie zachowywal podobny priorytet sasiadow
        # jak BFS: gora, prawo, dol, lewo.
        for neighbor in reversed(maze.neighbors(current)):
            if neighbor not in parent:
                parent[neighbor] = current
                stack.append(neighbor)

    elapsed_ms = (perf_counter() - start_time) * 1000
    return SearchResult("DFS", None, visited_nodes, elapsed_ms)
