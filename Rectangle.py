def draw_rectangle(symbol, row, column):
    if row >= 3 and column >= 3:
        for i in range(column):
            for j in range(row):
                if i == 0 or i == (column - 1) or j == 0 or j == (row - 1):
                    print(symbol, end='  ')
                else:
                    print(' ', end='  ')
            print('')
    else:
        print('Cannot create a hollow box! Row and Column values can\'t be less than 3.')


print('Hollow box program')
column = int(input('What is your Rectangle height?: '))
row = int(input('What is your Rectangle width?: '))
draw_rectangle('*', row, column)