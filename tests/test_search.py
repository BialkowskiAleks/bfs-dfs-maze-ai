from maze_ai.maze import Maze
from maze_ai.search import bfs, dfs


def test_bfs_finds_shortest_path_in_simple_maze() -> None:
    maze = Maze.from_text("""
S..
.#.
..G
""")

    result = bfs(maze)

    assert result.found is True
    assert result.path_length == 4
    assert result.path[0] == maze.start
    assert result.path[-1] == maze.goal


def test_dfs_finds_a_valid_path() -> None:
    maze = Maze.from_text("""
S..
.#.
..G
""")

    result = dfs(maze)

    assert result.found is True
    assert result.path is not None
    assert result.path[0] == maze.start
    assert result.path[-1] == maze.goal


def test_bfs_and_dfs_return_none_when_goal_is_unreachable() -> None:
    maze = Maze.from_text("""
S#.
###
.#G
""")

    assert bfs(maze).path is None
    assert dfs(maze).path is None


def test_bfs_is_not_longer_than_dfs_on_branching_maze() -> None:
    maze = Maze.from_text("""
S....
.#.#.
...#G
""")

    bfs_result = bfs(maze)
    dfs_result = dfs(maze)

    assert bfs_result.path_length is not None
    assert dfs_result.path_length is not None
    assert bfs_result.path_length <= dfs_result.path_length
