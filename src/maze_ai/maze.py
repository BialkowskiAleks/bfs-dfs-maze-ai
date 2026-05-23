"""Model labiryntu uzywany przez algorytmy BFS i DFS."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TypeAlias

Position: TypeAlias = tuple[int, int]


@dataclass(frozen=True)
class Maze:
    """Labirynt reprezentowany jako dwuwymiarowa siatka znakow.

    Dozwolone znaki:
    - S: start
    - G: cel
    - #: sciana
    - . lub spacja: wolne pole
    """

    grid: tuple[str, ...]
    start: Position
    goal: Position

    @classmethod
    def from_text(cls, text: str) -> Maze:
        """Tworzy labirynt z tekstu wielolinijkowego."""
        rows = tuple(line.rstrip("\n") for line in text.strip("\n").splitlines())
        if not rows:
            raise ValueError("Labirynt nie moze byc pusty.")

        width = len(rows[0])
        if any(len(row) != width for row in rows):
            raise ValueError("Wszystkie wiersze labiryntu musza miec taka sama dlugosc.")

        start_positions = cls._find_all(rows, "S")
        goal_positions = cls._find_all(rows, "G")

        if len(start_positions) != 1:
            raise ValueError("Labirynt musi zawierac dokladnie jeden punkt startowy S.")
        if len(goal_positions) != 1:
            raise ValueError("Labirynt musi zawierac dokladnie jeden cel G.")

        return cls(grid=rows, start=start_positions[0], goal=goal_positions[0])

    @staticmethod
    def _find_all(rows: tuple[str, ...], char: str) -> list[Position]:
        return [
            (r, c) 
            for r, row in enumerate(rows) 
            for c, value in enumerate(row) 
            if value == char
        ]

    @property
    def height(self) -> int:
        return len(self.grid)

    @property
    def width(self) -> int:
        return len(self.grid[0])

    def in_bounds(self, position: Position) -> bool:
        row, col = position
        return 0 <= row < self.height and 0 <= col < self.width

    def is_walkable(self, position: Position) -> bool:
        row, col = position
        return self.grid[row][col] != "#"

    def neighbors(self, position: Position) -> list[Position]:
        """Zwraca sasiadow w stalej kolejnosci: gora, prawo, dol, lewo."""
        row, col = position
        candidates = [(row - 1, col), (row, col + 1), (row + 1, col), (row, col - 1)]
        return [pos for pos in candidates if self.in_bounds(pos) and self.is_walkable(pos)]

    def render_with_path(self, path: list[Position] | None) -> str:
        """Zwraca tekstowa wizualizacje labiryntu ze sciezka oznaczona gwiazdkami."""
        if path is None:
            return "\n".join(self.grid)

        path_set = set(path) - {self.start, self.goal}
        rows = [list(row) for row in self.grid]
        for row, col in path_set:
            rows[row][col] = "*"
        return "\n".join("".join(row) for row in rows)
