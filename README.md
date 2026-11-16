# TinyForge — a tiny UCI chess engine

A complete chess engine in a single `main.py` (4,078 bytes, under the
4,096-byte contest limit), written in pure Python 3 standard library.
Built for the make.fun "tiny-chess-01" contest.

## Run

```sh
python3 main.py
```

Then speak UCI to it on stdin/stdout, e.g. `uci`, `isready`,
`position startpos`, `go wtime 10000 btime 10000 winc 100 binc 100`, `quit`.

## Features

- Full rules: legal move generation with castling, en passant and promotions
  (validated by perft against known node counts).
- Negamax search with alpha-beta pruning and iterative deepening; the best
  root move is tracked across iterations and a timeout abort always leaves
  the board state intact, so the returned move is legal for the position
  that was actually searched.
- Quiescence search over captures and promotions, so the engine does not
  walk into simple tactical shots at the horizon.
- Capture-first move ordering (most valuable victim), promotions next.
- Material evaluation plus a pawn-advancement bonus that rewards pushed
  and near-promotion pawns.
- Conservative time management for the 10s + 0.1s/move contest clock:
  roughly 1/25 of the remaining time per move plus half the increment,
  never more than half the remaining time, with a hard internal deadline
  checked at every search node.
