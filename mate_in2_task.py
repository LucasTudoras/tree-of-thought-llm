import os
import pandas as pd
import chess
from tot.tasks.base import Task, DATA_PATH

class MateIn2Task(Task):
    """
    Input (x): A FEN string.
    Output (y): A sequence of up to 3 UCI moves.
    Reward (r): 1 if sequence leads to checkmate, else 0.
    """
    def __init__(self, file='mate2_filtered.csv'):
        super().__init__()
        path = os.path.join(DATA_PATH, 'mate2', file)
        df = pd.read_csv(path)
        self.data = list(zip(df['FEN'], df['Moves']))
        self.steps = 3
        self.stops = ['\n'] * self.steps

    def __len__(self):
        return len(self.data)

    def get_input(self, idx: int) -> str:
        fen, _ = self.data[idx]
        return fen

    def test_output(self, idx: int, output: str) -> dict:
        fen, _ = self.data[idx]
        board = chess.Board(fen)
        try:
            for line in output.strip().split('\n'):
                move = line.strip()
                if move:
                    board.push_uci(move)
            return {'r': int(board.is_checkmate())}
        except Exception:
            return {'r': 0}

    @staticmethod
    def standard_prompt_wrap(x: str, y: str = '') -> str:
        return f"FEN: {x}\nFind a sequence of moves that mates in 2:\n{y}"

    @staticmethod
    def cot_prompt_wrap(x: str, y: str = '') -> str:
        return f"FEN: {x}\nLet’s reason through a mate-in-2 sequence step by step:\n{y}"

    @staticmethod
    def propose_prompt_wrap(x: str, y: str = '') -> str:
        return f"FEN: {x}\nPropose the next move (UCI format):\n{y}"

    @staticmethod
    def value_prompt_wrap(x: str, y: str) -> str:
        return f"FEN: {x}\nMoves so far:\n{y}\nIs this likely to result in mate in 2? (impossible / likely / sure)"

    @staticmethod
    def value_outputs_unwrap(x: str, y: str, value_outputs: list) -> float:
        value_names = [_.strip().lower() for _ in value_outputs]
        value_map = {'impossible': 0.01, 'likely': 1, 'sure': 20}
        return sum(value_map.get(name, 0) for name in value_names)
