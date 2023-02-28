import pytest
from unittest import mock

from Tictactoe import TicTacToe

def test_create_tic_tac_toe_board():
    board = TicTacToe(3, 3)
    assert board.board == [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
    assert board.winning is None

def test_create_tic_tac_toe_board_with_winning_length():
    board = TicTacToe(3, 3, 3)
    assert board.board == [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
    assert board.winning == 3

def test_create_tic_tac_toe_board_with_invalid_winning_length():
    with pytest.raises(ValueError):
        board = TicTacToe(3, 3, 4)

def test_update_tic_tac_toe_board():
    board = TicTacToe(3, 3)
    board.update_board('X', 1, 1)
    assert board.board == [['-', '-', '-'], ['-', 'X', '-'], ['-', '-', '-']]
    board.update_board('O', 2, 2)
    assert board.board == [['-', '-', '-'], ['-', 'X', '-'], ['-', '-', 'O']]

def test_check_horizontal_win():
    board = TicTacToe(3, 3)
    board.board = [['-', '-', '-'], ['X', 'X', 'X'], ['-', '-', '-']]
    assert board.check_win('X') == True

def test_check_vertical_win():
    board = TicTacToe(3, 3)
    board.board = [['-', 'X', '-'], ['-', 'X', '-'], ['-', 'X', '-']]
    assert board.check_win('X') == True

def test_check_diagonal_win_():
    board = TicTacToe(3, 3)
    board.board = [['X', '-', '-'], ['-', 'X', '-'], ['-', '-', 'X']]
    assert board.check_win('X') == True

def test_show_current_board(capsys):
    board = TicTacToe(3, 3)
    expected_output = "['-', '-', '-']\n['-', '-', '-']\n['-', '-', '-']"
    board.show_current_board()
    captured_output = capsys.readouterr()
    assert captured_output.out.rstrip('\n') == expected_output

def test_diagonals():
    board = TicTacToe(3, 3)
    board.board = [['-', 'X', '-'], ['-', 'X', '-'], ['-', 'X', 'X']]
    assert board.get_diagonal(True) == ['-', 'X', '-']

def test_get_user_input_valid():
    user_input = "1\n2\n"
    board = TicTacToe(3, 3)
    board.occupied = dict()
    with mock.patch('builtins.input', side_effect=user_input.split()):
        result = board.get_user_input()
    assert result == (1, 2)

def test_get_user_input_invalid():
    user_input = "4\n2\n2\n2\n0\n1\n"
    board = TicTacToe(3, 3)
    with mock.patch('builtins.input', side_effect=user_input.split()):
        result = board.get_user_input()
    with pytest.raises(AssertionError):
        assert result == (0, 1)


def test_check_vertical_win_with_defined_lenght():
    board = TicTacToe(3, 3, 2)
    board.board = [['-', 'X', '-'], ['-', 'X', '-'], ['-', '-', 'X']]
    print(board.check_win('X'))
    assert board.check_win('X') == True

def test_check_diagonal_win_with_defined_lenght():
    board = TicTacToe(3, 3, 2)
    board.board = [['-', '-', 'X'], ['-', 'O', '-'], ['-', '-', 'O']]
    assert board.check_win('O') == True

def test_check_horizontal_win_with_defined_lenght():
    board = TicTacToe(4, 3, 2)
    board.board = [['X', 'X', 'O', 'X'], ['O', 'X', 'O', 'O'], ['-', 'X', 'X', 'X']]
    assert board.check_win('X') == True

def test_check_win_failure():
    board = TicTacToe(3, 3, 2)
    board.board = [['-', 'O', '-'], ['-', 'O', '-'], ['-', '-', 'O']]
    with pytest.raises(AssertionError):
        assert board.check_win('X') == True

def test_play_game_X_win():
    tic_tac_toe = TicTacToe(3,3)
    mock_input = mock.Mock(side_effect=["0", "0", "1", "0", "1", "1", "2", "0", "2", "2"])
    with mock.patch('builtins.input', mock_input):
        tic_tac_toe.play_game()
    # Assert that 'X' has won
    assert tic_tac_toe.check_win('X') == True                                                        

def test_play_game_O_win():
    tic_tac_toe = TicTacToe(4,4,3)
    mock_input = mock.Mock(side_effect=["0", "0", "1", "0", "1", "1", "2", "0", "2", "3", "3", "0"])
    with mock.patch('builtins.input', mock_input):
        tic_tac_toe.play_game()
    # Assert that 'O' has won
    assert tic_tac_toe.check_win('O') == True

def test_play_game_draw():
    tic_tac_toe = TicTacToe(4, 4)
    mock_input = mock.Mock(side_effect=["0", "0", "0", "1", "0", "2", "0", "3", "1", "0", "2", "0", "3", "0", "3" ,"1", 
                                        "2", "1", "1", "1", "1", "2", "1", "3", "2", "3", "3", "3", "3", "2", "2", "2"])
    with mock.patch('builtins.input', mock_input):
        tic_tac_toe.play_game()
    # Assert that the game ended in a tie
    assert tic_tac_toe.check_win('X') == False
    assert tic_tac_toe.check_win('O') == False

def test_invalid_overwriting_of_existing_box(capsys):
    tic_tac_toe = TicTacToe(2, 2)
    tic_tac_toe.occupied = {(0, 0): True}
    mock_input = mock.Mock(side_effect=['0', '0', '0', '1'])
    expected_output = "You cannot mark an already selected box\n['-', '-']\n['-', '-']"
    with mock.patch('builtins.input', mock_input):
        tic_tac_toe.get_user_input()
        captured_output = capsys.readouterr()
        assert captured_output.out.rstrip('\n') == expected_output


def test_main():
    with mock.patch('builtins.input', side_effect=['3', '3', '3']):
        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of columns: "))
        winning = input("Enter length of winning row or column: (optional)")
    assert rows == 3
    assert cols == 3
    assert winning == '3'
    mock_play_game = mock.Mock()
    with mock.patch.object(TicTacToe, 'play_game', mock_play_game):
        board = TicTacToe(rows, cols, int(winning))
        board.play_game()
        mock_play_game.assert_called_once()

