import numpy as np
from random import randint, choice

from PIL import Image, ImageDraw, ImageFont


class game2048():
  def __init__(self):
    '''
    Initializes the board with numbers in the board as follows
        [2, 0, 0, 0]
        [0, 2, 0, 2]
        [4, 0, 0, 0]
        [8, 0, 8, 2]

    '''
    self._board = np.array([
        [2, 0, 0, 0],
        [0, 2, 0, 2],
        [4, 0, 0, 0],
        [8, 0, 8, 2]
    ])
    self._length = 3

  def __str__(self):
    return str(self._board)

  def flatten(self, arr):
    '''
    taking a 2d array's row as an argument
      flattening it as
                                        [8,0,8,2]
                                if flatted to the right
    becomes                             [0,0,16,2]
      as a 2048 rule
      and then returning the row

    '''
    # flatten a single row
    for _ in range(3):
        # the code below is for flattening but to make sure doing it 4 times as th loop above says
        for i in range(1, self._length + 1):
            # stating to check from 1th element rather than 0th
            if arr[i] == 0 and i != 0:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
            if arr[i] == arr[i - 1]:
                arr[i] = arr[i] * 2
                arr[i - 1] = 0
        # print(arr)
    return arr

  def right(self):
    for row_index in range(self._length + 1):
        self._board[row_index] = self.flatten(self._board[row_index])
    # print('Righted--> \n', self._board)

  def left(self):
    # print(self._board)
    '''
    So basically [::-1] flip each row of board and   ////////
    do a self.right() and flip it back and walla !!! //left//
                                                      ////////
    '''
    new = []
    for row in self._board:
        new.append(row[::-1])
    self._board = np.array(new)

    self.right()

    new = []
    for row in self._board:
        new.append(row[::-1])
    self._board = np.array(new)

  def up(self):
    '''
    transpose the board and left = up (if right = down)
    '''
    self._board = self._board.transpose()
    self.left()
    self._board = self._board.transpose()

  def down(self):
    '''
    transpose the board and right = down
    '''
    self._board = self._board.transpose()
    self.right()
    self._board = self._board.transpose()

  def add_random_nos(self):
    '''
    adds a random number [2,4,8]
    as a choice from the list above
    to a random 2d location in the board where the number is 0
    OR empty in case of the GUI if i ever made one
    '''
    x, y = randint(0, 3), randint(0, 3)
    if self._board[x, y] == 0:
        self._board[x, y] = choice([2, 4, 8])
    else:
        self.add_random_nos()

  # def show_slice(self):
  #   '''
  #   writing should start from 16px, 16px
  #   dimension of each no is 108 by 108
  #   maybe need additional 16px for next no will see
  #   '''
  #   # draw.text((30, 90), f'{self._board[i,j]}', fill='white', font=arial)
  #   board = Image.open('board.jpg')
  #   draw = ImageDraw.Draw(board)
  #   arial = ImageFont.truetype('arial.ttf', size=100)
  #   for i in range(4):
  #       for j in range(4):
  #           draw_coord = ((i * 108) + 16, (j * 108) + 16)
  #           draw.text(draw_coord,  # co-ord of where to draw the number
  #                     # value of no to write on the coord
  #                     f'{self._board[i,j]}   ',
  #                     fill='white',  # writing the no as a white no for now
  #                     font=arial)  # obviuos

  #   board.save('new_board.jpg')


# x = game2048()
# x.down()
# print(x)
# x.show_slice()

# print(x)
# x.up()
# print(x)
# x.left()
# print(x)
# x.add_random_nos()
# print(x)

# x.flatten(x._board[3])
# x.flatten(arr)

# print(arr)


# def flatten(arr):
#     for i in range(1, 4):
#         print(i)
#         if arr[i] == 0 and i != 0:
#             print('.')
#             arr[i], arr[i - 1] = arr[i - 1], arr[i]
#         if arr[i] == arr[i - 1]:
#             print('*')
#             arr[i] = arr[i] * 2
#             arr[i - 1] = 0
#     print(arr)


# arr = [0, 0, 4, 0]

# for i in range(4):
#     flatten(arr)
# flatten(arr)
