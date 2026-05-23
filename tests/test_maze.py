import pytest

from maze_ai.maze import Maze


def test_maze_parses_start_and_goal() -> None:
    maze = Maze.from_text("""
S..
.#.
..G
""")

    assert maze.start == (0, 0)
    assert maze.goal == (2, 2)
    assert maze.width == 3
    assert maze.height == 3


def test_neighbors_skip_walls_and_out_of_bounds() -> None:
    maze = Maze.from_text("""
S#.
...
..G
""")

    assert maze.neighbors((0, 0)) == [(1, 0)]


def test_maze_requires_one_start_and_one_goal() -> None:
    with pytest.raises(ValueError):
        Maze.from_text("""
S.S
...
..G
""")
