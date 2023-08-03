class Board:

    def __init__(self):
        self.data = [[0 for i in range(3)] for i in range(3)]
        print(self.data)

    def get(self,x,y):
        return self.data[x][y]

    def set(self,x,y,val):
        if (self.data[x][y] == 0):
            self.data[x][y] = val
            return True
        else:
            return False

    def get_row(self,x):
        return self.data[x]

    def set_row(self,x,val):
        assert type(val) == list
        self.data[x] = val

    def get_col(self,y):
        return [self.data[i][y] for i in range(3)]

    def set_col(self,y,val):
        assert type(val) == list
        for i in range(3):
            self.data[i][y] = val[i]

    def get_diagonal(self,x):
        assert x in range(2)
        return [self.get(i,i) for i in range(3)] if x == 0 else [self.get(2-i,i) for i in range(3)]

    def set_diagonal(self,x, val):
        assert type(val) == list
        assert x in range(2)

        for i in range(3):
            x_index = i if x == 0 else 2-i
            self.set(x_index,i,val[i])

    def check_tie(self):
        full_board = []
        for i in range(3):
            full_board += self.get_row(i)

        return True if 0 not in full_board else False

    def find_winner(self):
        #checks the totals for the rows and columns and diagonals, and returns true if a 1 or an 8 is in the list

        winner = "None"


        def product(mylist):
            total = 1
            for x in mylist:
                total *= x

            return total

        row_totals = [product(self.get_row(i)) for i in range(3)]
        col_totals = [product(self.get_col(i)) for i in range(3)]
        diagonal_totals = [product(self.get_diagonal(i)) for i in range(2)]

        totals = row_totals + col_totals + diagonal_totals
        
        if 1 in totals:
            winner = "Player"
            return winner
        elif 8 in totals:
            winner = "Computer"
            return winner
        elif (self.check_tie()):
            return "Tie"
        else:
            return "None"


    def render(self):

        render_dic = {0: "  ~  " , 1: "  X  ", 2: "  O  "}

        for i in range(len(self.data)):
            row_render = "  "
            for j in range(len(self.data[i])):
               row_render += render_dic[self.data[i][j]]

            print(row_render)

