# Prompts for the Mate-in-Two task. All templates use {input} (FEN) and, where relevant, {answer} or partial move traces.

# 3-shot standard prompt: FEN to sequence of UCI moves (mate in 2)
standard_prompt = '''Here are some mate-in-two chess puzzles and their solutions (in UCI format).
Position (FEN): 4r3/1k6/pp3r2/1b2P2p/3R1p2/P1R2P2/1P4PP/6K1 w - - 0 35
Answer:
e5f6
e8e1
g1f2
e1f1

Position (FEN): r1bqk2r/pp1nbNp1/2p1p2p/8/2BP4/1PN3P1/P3QP1P/3R1RK1 b kq - 0 19
Answer:
e8f7
e2e6
f7f8
e6f7

Position (FEN): {input}
Answer:'''

# 3-shot Chain-of-Thought prompt: explain each move in UCI
cot_prompt = '''Solve each mate-in-two puzzle step by step. Use UCI format for moves.

Position (FEN): 4r3/1k6/pp3r2/1b2P2p/3R1p2/P1R2P2/1P4PP/6K1 w - - 0 35
Steps:
1. White plays e5f6, threatening mate and forcing a response.
2. Black responds with e8e1, checking the king.
3. White escapes with g1f2.
4. Black plays e1f1, but white is now ready to mate next turn.
Answer:
e5f6
e8e1
g1f2
e1f1

Position (FEN): {input}
Steps:'''

# 1-shot propose prompt: list possible next moves in UCI format
propose_prompt = '''Given the chess position (FEN): {input}
Propose strong candidate moves in UCI format that may lead to checkmate in two moves. Return only UCI moves, separated by newlines.'''

# Value prompt: evaluate current partial sequence
value_prompt = '''Evaluate the following move sequence in UCI format.
Position (FEN): {input}
Moves so far:
{answer}
How likely is this sequence to lead to a mate in two? (Answer with: impossible / likely / sure)'''

# Last-step value prompt (e.g. final judgment after full 3-ply sequence)
value_last_step_prompt = '''Final evaluation of a proposed mate-in-two.
Position (FEN): {input}
Answer:
{answer}
Judge the outcome (sure / impossible):'''
