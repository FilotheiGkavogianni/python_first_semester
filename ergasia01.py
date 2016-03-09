#!/usr/bin/python
# -*- coding: utf-8 -*-

print '\t           ____               ___    _____         _____          '
print '\t   |      |    | |\   \   /  |   |     |    |\   |   |     |   |  '
print '\t   |      |____| |_\   \ /   |___|     |    | \  |   |     |___|   ' 
print '\t   |      |    | | /    |    |   \     |    |  \ |   |     |   |   '
print '\t   |____  |    | |/     |    |    \  __|__  |   \|   |     |   |   '


import math
import random
board = []

for row in range(10):
  board.append([])
  for column in range(10):
    board[row].append('x')
      
k=random.randint(0, 9)
l=random.randint(0, 9)
m=random.randint(0, 9)
n=random.randint(0, 9)   
board[k][l]='U'
board[m][n]='T'    
    
def print_board(board):
  for row in board:
    print " ".join(row)
    
print_board(board)

r=math.fabs(k-m)
t=math.fabs(l-n)
p=r+t
print 'exeis akoma',p,'bhmata'

count=0
move=raw_input("Πατήστε W(για πάνω)-S(για κάτω)-D(για δεξιά)-A(για αριστερά) για να κινηθείτε:")

while ((board[k][l])!=(board[m][n])):
 if move=='W' or move=='w':
  count+=1
  board[k][l]='x'	
  if k==0:
   board[k][l]='U'
   board[m][n]='T'
   print 'ε...τοιχος'
   move=raw_input("Πατήστε W(για πάνω)-S(για κάτω)-D(για δεξιά)-A(για αριστερά) για να κινηθείτε:")
   continue
  k=k-1	
  board[k][l]='U'
  board[m][n]='T'
  print_board(board)
  r=math.fabs(k-m)
  t=math.fabs(l-n)    
  p=r+t
  print 'exeis akoma',p,'bhmata'
  if (p==0):
	  break
  move=raw_input("Πατήστε W(για πάνω)-S(για κάτω)-D(για δεξιά)-A(για αριστερά) για να κινηθείτε:")
  if ((board[k][l])==(board[m][n])):
   break
 if move=='S' or move=='s':
  count+=1
  board[k][l]='x'
  if k==9:
	 board[k][l]='U'
	 board[m][n]='T'
	 print 'ε...τοιχος'
	 move=raw_input("Πατήστε W(για πάνω)-S(για κάτω)-D(για δεξιά)-A(για αριστερά) για να κινηθείτε:")
	 continue
  k=k+1
  board[k][l]='U'
  board[m][n]='T'
  print_board(board)
  r=math.fabs(k-m)
  t=math.fabs(l-n)    
  p=r+t
  print 'exeis akoma',p,'bhmata'
  if (p==0):
	  break
  move=raw_input("Πατήστε W(για πάνω)-S(για κάτω)-D(για δεξιά)-A(για αριστερά) για να κινηθείτε:")
  if ((board[k][l])==(board[m][n])):
	break
 if move=='A' or move=='a':
  count+=1
  board[k][l]='x'
  if l==0:
   board[k][l]='U'
   board[m][n]='T'
   print 'ε...τοιχος'
   move=raw_input("Πατήστε W(για πάνω)-S(για κάτω)-D(για δεξιά)-A(για αριστερά) για να κινηθείτε:")
   continue
  l=l-1
  board[k][l]='U'
  board[m][n]='T'
  print_board(board)
  r=math.fabs(k-m)
  t=math.fabs(l-n)    
  p=r+t
  print 'exeis akoma',p,'bhmata'
  if (p==0):
	  break
  move=raw_input("Πατήστε W(για πάνω)-S(για κάτω)-D(για δεξιά)-A(για αριστερά) για να κινηθείτε:")
  if ((board[k][l])==(board[m][n])):
   break
 if move=='D' or move=='d':
  count+=1
  board[k][l]='x'
  if l==9:
   board[k][l]='U'
   board[m][n]='T'
   print 'ε...τοιχος'
   move=raw_input("Πατήστε W(για πάνω)-S(για κάτω)-D(για δεξιά)-A(για αριστερά) για να κινηθείτε:")
   continue
  l=l+1
  board[k][l]='U'
  board[m][n]='T'
  print_board(board)
  r=math.fabs(k-m)
  t=math.fabs(l-n)    
  p=r+t
  print 'exeis akoma',p,'bhmata'
  if (p==0):
	  break
  move=raw_input("Πατήστε W(για πάνω)-S(για κάτω)-D(για δεξιά)-A(για αριστερά) για να κινηθείτε:")
  if ((board[k][l])==(board[m][n])):
   break
   
		
print '\t\t\tBRAVO!!!',count,'prospatheies'
print '\t\t\tYOU WIN A "HANDMADE" DIGITAL DOG!!!'
print        "\t\t\t^__^"
print        "\t\t\t(XX) \_________ /\/"
print		 "\t\t\t(__)  \         )" 
print		 "\t\t\t U    ||-----W- |"
print 		 "\t\t\t      ||       || "
 
