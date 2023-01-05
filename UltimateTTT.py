# Ultimate Tic Tac Toe program with random moving computer
# 12/192022
__author__ = 'Tyler Slomianyj'

import random
import time
import os
import copy
import numpy as np

board = [[[['#','#','#'],['#','#','#'],['#','#','#']],
[['#','#','#'],['#','#','#'],['#','#','#']],
[['#','#','#'],['#','#','#'],['#','#','#']]],
[[['#','#','#'],['#','#','#'],['#','#','#']],
[['#','#','#'],['#','#','#'],['#','#','#']],
[['#','#','#'],['#','#','#'],['#','#','#']]],
[[['#','#','#'],['#','#','#'],['#','#','#']],
[['#','#','#'],['#','#','#'],['#','#','#']],
[['#','#','#'],['#','#','#'],['#','#','#']]]]

ultimateBoard = [['#', '#', '#'],['#', '#', '#'],['#', '#', '#']]
moveLocation = []
boxPick = []
checkMove = [0, 1, 2]
moveList = []
boxPickList = []
lenPickList = 0
lastMove = []


def resetBoard(): # resets board
  board = [[[['#','#','#'],['#','#','#'],['#','#','#']],
[['#','#','#'],['#','#','#'],['#','#','#']],
[['#','#','#'],['#','#','#'],['#','#','#']]],
[[['#','#','#'],['#','#','#'],['#','#','#']],
[['#','#','#'],['#','#','#'],['#','#','#']],
[['#','#','#'],['#','#','#'],['#','#','#']]],
[[['#','#','#'],['#','#','#'],['#','#','#']],
[['#','#','#'],['#','#','#'],['#','#','#']],
[['#','#','#'],['#','#','#'],['#','#','#']]]]


def printBoard(board): # prints the big board
  for ultRow in range(0, len(board)):
    for row in range(0, len(board[ultRow])):
      for ultCol in range(0, len(board[ultRow][row])):
        for col in range(0, len(board[ultRow][row][ultCol])):
          
          
          print(board[ultRow][ultCol][row][col], end = '')
          if col < len(board[ultRow][row][ultCol])-1:
            print(" | ", end = '')
          if col == 2 and ultCol != 2:
            print(' || ', end = '')
            
            
      if row < len(board[ultRow])-1:
        print()
        print('------------------------------------')
      if row == 2 and ultRow != 2:
        print()
        print('------------------------------------')
        print('------------------------------------')
  print()


def boardIsFull(board): # checks if every single box in the full board is full
  for ultRow in range(0, 3):
    for ultCol in range(0, 3):
      for row in range(0, 3):
        for col in range(0, 3):
          if board[0][0][row][col] == '#':
            return False
  return True


def gameWon(board): # checks if the game is won in a 3x3 array
  for row in range(0, len(board)):
    if board[row][0] != '#' and board[row][0] == board[row][1] == board[row][2]:
      return True
  for col in range(0, len(board[1])):
    if board[0][col] != '#' and board[0][col] == board[1][col] == board[2][col]:
      return True
  if board[0][0] != '#' and board[0][0] == board[1][1] == board[2][2]:
    return True
  if board[0][2] != '#' and board[0][2] == board[1][1] == board[2][0]:
    return True
  return False


def smallBoardPrint(board): # prints a small TTT board
  print()
  for row in range(0, len(board)):
    for col in range(0, len(board[row])):
      print(board[row][col], end = '')
      if col < len(board[row])-1:
          print(" | ", end = '')
    if row < len(board)-1:
      print('\n---------')
    else:
      print('') 


def isOpen(board, r, c): # checks if the spot in the board is open
  return '#' in board[r][c]


def playerMove(move, playerType): # does the move the player wants to and checks if the player won the game and changes boxPick in those circumstances
  global board, boxPick, ultimateBoard
  if board[boxPick[0]][boxPick[1]][move[0]][move[1]] == '#':
    board[boxPick[0]][boxPick[1]][move[0]][move[1]] = playerType
  else:
    print('help')
  if gameWon(board[boxPick[0]][boxPick[1]]):
    ultimateBoard[boxPick[0]][boxPick[1]] = playerType
    board[boxPick[0]][boxPick[1]] = [[playerType, playerType, playerType], [playerType, playerType, playerType], [playerType, playerType, playerType]]
  if ultimateBoard[move[0]][move[1]] == '#':
    boxPick = move
  else:
    boxPick = []


def clean(): # cleans the display
  time.sleep(0.1)
  os.system('clear')


def main(): # main function of the program
  global board, ultimateBoard, boxPick, moveLocation, boxPickList, moveList, lenPickList, lastMove
  
  print('* Welcome to ULTIMATE Tic-Tac-Toe *')
  player = ''
  computer = ''
  printBoard(board)
  print('Main board ^^^^^^^^^^^^^^^^^^^^^^^^^')
  smallBoardPrint(ultimateBoard)
  print('^^^^^^^^^ (3x3 representation of ultimate board)')
  
  xturn = (random.randint(1,2) == 2)
  movelocation = []
  while player != 'X' and player != 'O':
    player = input('Would you like to be X or O? ').upper()
  computer = 'O' if player == 'X' else 'X'
  print('X moves first' if xturn else 'O moves first')
  time.sleep(1.5)
  
  while not(gameWon(ultimateBoard) and boardIsFull(board)):
    if xturn and player == 'X' or not xturn and player == 'O': # player move
      if not boxPick:
        clean()
        printBoard(board)
        smallBoardPrint(ultimateBoard)
        
        while True:
          try:
            boxPick = input('Which box in the ultimate TTT board do you want to pick? Ex: ' + str(random.randint(0, 2)) + ' ' + str(random.randint(0, 2)) + '\n-').split()
            boxPick = [eval(i) for i in boxPick]
            if (boxPick[0] in checkMove) and (boxPick[1] in checkMove) and (ultimateBoard[boxPick[0]][boxPick[1]] == '#'):
              break
            else:
              clean()
              printBoard(board)
              smallBoardPrint(ultimateBoard)
              print('Invalid move or invalid input. Try again.')
          except:
            clean()
            printBoard(board)
            smallBoardPrint(ultimateBoard)
            print('Invalid move or invalid input. Try again.')
      
      clean()
      printBoard(board)
      print('Main board ^^^^^^^^^^^^^^^^^^^^^^^^^')
      smallBoardPrint(board[boxPick[0]][boxPick[1]])
      print('^^^^^^^^^ this is the mini TTT box that you chose.')
      
      while True:
        try:
          if len(lastMove) == 4:
            print('The computer last moved in position ', lastMove[2], ', ', lastMove[3], ' in ultimate box ', lastMove[0], ', ', lastMove[1], '.', sep='')
          moveLocation = input('What box in the mini TTT board do you want to move in? (You are moving in ultimate box ' + str(boxPick[0]) + ', ' + str(boxPick[1]) + '.)' + ' Ex: ' + str(random.randint(0, 2)) + ' ' + str(random.randint(0, 2)) + '\n-').split()
          moveLocation = [eval(i) for i in moveLocation]
          if (moveLocation[0] in checkMove) and (moveLocation[1] in checkMove) and (board[boxPick[0]][boxPick[1]][moveLocation[0]][moveLocation[1]] == '#') and (ultimateBoard[boxPick[0]][boxPick[1]] == '#'):
            playerMove(moveLocation, player)
            xturn = not xturn
            break
          else:
            clean()
            printBoard(board)
            smallBoardPrint(board[boxPick[0]][boxPick[1]])
            print('^^^^^^^^^ this is the mini TTT box that you have chosen.')
            print(boxPick, moveLocation)
            print('Invalid move or invalid input. Try again.')
        except Exception as e:
          clean()
          printBoard(board)
          smallBoardPrint(board[boxPick[0]][boxPick[1]])
          print('^^^^^^^^^ this is the mini TTT box that you have chosen.')
          print('Invalid move or invalid input. Try again.')
    else: # random computer move
      lastMove = []
      if not boxPick:
        boxPickList = []
        for ultRow in range(3):
          for ultCol in range(3):
            if ultimateBoard[ultRow][ultCol] == '#':
              boxPickList.append([ultRow, ultCol])
        boxPick = random.choice(boxPickList)
      moveList = []
      for ultRow in range(3):
        for ultCol in range(3):
          if isOpen(board[boxPick[0]][boxPick[1]], ultRow, ultCol):
            moveList.append([ultRow, ultCol])
      moveLocation = random.choice(moveList)
      lastMove = [boxPick[0], boxPick[1], moveLocation[0], moveLocation[1]]
      playerMove(moveLocation, computer)
      xturn = not xturn
  print('good game')

if __name__ == '__main__': #main entry point of the program
  main()