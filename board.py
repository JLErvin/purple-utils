#!/bin/python3

import chess
import argparse
import sys

def print_moves(moves, board, f_piece):
    for move in moves:
        square = move.from_square
        piece = board.piece_at(square)
        if f_piece == None or f_piece == str(piece):
            to_name = chess.SQUARE_NAMES[move.to_square]
            from_name = chess.SQUARE_NAMES[move.from_square]
            print("Piece:", piece, "From:", from_name, "To:", to_name)


def print_pseudolegal(fen, f_piece=None):
    board = chess.Board(fen)
    moves = board.pseudo_legal_moves
    print("Number of Pseudo-Legal moves:", moves.count())
    print_moves(moves, board, f_piece)

def print_legal(fen, f_piece=None):
    board = chess.Board(fen)
    moves = board.legal_moves
    print("Number of Legal moves:", moves.count())
    print_moves(moves, board, f_piece)

def print_bitboards(fen):
    board = chess.Board(fen)
    WP = board.pieces(chess.PAWN, chess.WHITE)
    WR = board.pieces(chess.ROOK, chess.WHITE)
    WN = board.pieces(chess.KNIGHT, chess.WHITE)
    WB = board.pieces(chess.BISHOP, chess.WHITE)
    WK = board.pieces(chess.KING, chess.WHITE)
    WQ = board.pieces(chess.QUEEN, chess.WHITE)

    BP = board.pieces(chess.PAWN, chess.BLACK)
    BR = board.pieces(chess.ROOK, chess.BLACK)
    BN = board.pieces(chess.KNIGHT, chess.BLACK)
    BB = board.pieces(chess.BISHOP, chess.BLACK)
    BK = board.pieces(chess.KING, chess.BLACK)
    BQ = board.pieces(chess.QUEEN, chess.BLACK)

    white=WP|WR|WN|WB|WK|WQ
    black=BP|BR|BN|BB|BK|BQ
    all=white|black

    print("White Pawn:", int(WP))
    print("White Rooks:", int(WR))
    print("White Knights:", int(WN))
    print("White Bishops:", int(WB))
    print("White King:", int(WK))
    print("White Queen:", int(WQ))
    print()

    print("Black Pawn:", int(BP))
    print("Black Rooks:", int(BR))
    print("Black Knights:", int(BN))
    print("Black Bishops:", int(BB))
    print("Black King:", int(BK))
    print("Black Queen:", int(BQ))
    print()

    print("All Pieces:", int(all))

def main():
    parser = argparse.ArgumentParser(description='Testing utility for purple chess engine.')
    parser.add_argument('fen', help='FEN representation for board')
    parser.add_argument('-b', required=False, help='Print all bitboards for given board', action='store_true')
    parser.add_argument('-p', required=False, help='Print pseudolegal moves for position', action='store_true')
    parser.add_argument('-l', required=False, help='Print legal moves for position', action='store_true')
    parser.add_argument('-t', required=False, help='Filter based on piece type')
    p = parser.parse_args()

    print("Analyzing for FEN:", p.fen)

    if p.b:
        print_bitboards(p.fen)

    if p.p:
        print_pseudolegal(p.fen, p.t)

    if p.l:
        print_legal(p.fen, p.t)


if __name__ == "__main__":
    main()
