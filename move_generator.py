import chess

def apply_move(fen, move_uci):
    """
    Apply a move to a FEN position and return the new FEN.
    
    Parameters:
    - fen (str): The FEN string of the current position
    - move_uci (str): The move in UCI format (e.g., 'e2e4', 'g1f3')
    
    Returns:
    - str: The new FEN after applying the move
    - bool: True if the move was legal and applied, False otherwise
    """
    try:
        board = chess.Board(fen)
        move = chess.Move.from_uci(move_uci)
        if move in board.legal_moves:
            board.push(move)
            return board.fen(), True
        else:
            return fen, False  # Move is not legal
    except Exception as e:
        print(f"Error: {e}")
        return fen, False

def main():
    # Example inputs
    fen = "r1bqkbnr/pppppppp/n7/8/8/5N2/PPPPPPPP/RNBQKB1R w KQkq - 2 3"
    move = "g1f3"

    new_fen, success = apply_move(fen, move)
    if success:
        print("New FEN:", new_fen)
    else:
        print("Invalid move.")

if __name__ == "__main__":
    main()
