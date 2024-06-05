import random

pieceScore = {"K": 0, "Q": 10, "R": 5,
              "B": 3, "N": 3, "p": 1}
CHECKMATE = 1000
STALEMATE = 0
DEPTH = 5


def findRandomMove(validMoves):
    return validMoves[random.randint(0, len(validMoves)-1)]

# Recursive Minimax
def findBestMove(gs, validMoves):
    turnMultiplier = 1 if gs.whiteToMove else -1
    oppMinMaxScore = CHECKMATE
    bestPlayerMove = None
    for playerMove in validMoves:
        gs.makeMove(playerMove)
        oppMoves = gs.getValidMoves()
        random.shuffle(validMoves)
        oppMaxScore = -CHECKMATE
        for oppMove in oppMoves:
            gs.makeMove(oppMove)
            if gs.checkMate:
                score = -turnMultiplier * CHECKMATE
            elif gs.staleMate:
                score = STALEMATE
            else:
                score = -turnMultiplier * scoreMaterial(gs.board)
            if score > oppMaxScore:
                oppMaxScore = score
            gs.undoMove()
        if oppMaxScore < oppMinMaxScore:
            oppMinMaxScore = oppMaxScore
            bestPlayerMove = playerMove
        gs.undoMove()
    return bestPlayerMove


# Helper method to makefirst recursive call
def findBestMoveMinMax(gs, validMoves, depth, whiteToMove):
    global nextMove
    nextMove = None
    findMoveMinMax(gs, validMoves, DEPTH, gs.whiteToMove)
    return nextMove

# Recursive Minimax
def findMoveMinMax(gs, validMoves, depth, whiteToMove):
    global nextMove
    if depth == 0:
        return scoreMaterial(gs.board)

    if whiteToMove:
        maxScore = -CHECKMATE
        for move in validMoves:
            gs.makeMove()
            nextMove = gs.getValidMoves()
            score = findMoveMinMax(gs, nextMove, depth-1, False)
            if score > maxScore:
                maxScore = score
                if depth == DEPTH:
                    nextMove = move
            gs.undoMove()
        return maxScore
    else:
        minScore = CHECKMATE
        for move in validMoves:
            gs.makeMove()
            nextMove = gs.getValidMoves()
            score = findMoveMinMax(gs, nextMove, depth-1, True)
            if score < maxScore:
                minScore = score
                if depth == DEPTH:
                    nextMove = move
            gs.undoMove()
        return minScore


def scoreBoard(gs, ):
    if gs.checkMate:
        if gs.whiteToMove:
            return -CHECKMATE
        else:
            return CHECKMATE
    elif gs.staleMate:
        return STALEMATE

    score = 0
    for row in gs.board:
        for square in row:
            if square[0] == 'w':
                score += pieceScore[square[1]]
            elif square[0] == 'b':
                score -= pieceScore[square[1]]

    return score



def scoreMaterial(board):
    score = 0
    for row in board:
        for square in row:
            if square[0] == 'w':
                score += pieceScore[square[1]]
            elif square[0] == 'b':
                score -= pieceScore[square[1]]

    return score