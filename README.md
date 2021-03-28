<div align='center'>
    <h1>purple-utils</h1><br>
</div>

A simple script for testing bitboards, pseudo-legal, and legal move generation using python-chess.

## Usage

```
usage: board.py [-h] [-b] [-p] [-l] [-t T] fen

Testing utility for purple chess engine.

positional arguments:
  fen         FEN representation for board

optional arguments:
  -h, --help  show this help message and exit
  -b          Print all bitboards for given board
  -p          Print pseudolegal moves for position
  -l          Print legal moves for position
  -t T        Filter based on piece type
```
