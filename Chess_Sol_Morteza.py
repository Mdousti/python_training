# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 17:47:00 2018

@author: M.Dousti
"""
chess_board_size = 8
chess_board = [0] * chess_board_size

solution_found = False
index = 0
while not solution_found:
    treat_check = False
    for index_check in range( index ):
        if chess_board[index] == chess_board[index_check]:
            chess_board[index] = chess_board[index] + 1
            treat_check = True

        elif chess_board[index] == ( chess_board[index_check]+(index-index_check) ):
            chess_board[index] = chess_board[index] + 1
            treat_check = True
            
        elif chess_board[index] == ( chess_board[index_check]-(index-index_check) ):
            chess_board[index] = chess_board[index] + 1
            treat_check = True
        
    if not treat_check:
        if chess_board[index] > 7:
            chess_board[index] = 0        
            index = index - 1
            chess_board[index] = chess_board[index] + 1
        else:
            index = index + 1
        
    if index > 7:
        solution_found = True
        
print( 'chess_board..:', chess_board)