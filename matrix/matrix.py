class Matrix:
    def __init__(self, matrix_string):
        self.matrix_list = []
        for x in matrix_string.split("\n"):
            self.matrix_list.append(list(map(int, x.split(" "))))

    def row(self, index):
        return self.matrix_list[index-1]

    def column(self, index):
        col_list = []
        for row in self.matrix_list:
            col_list.append(row[index-1])
        return col_list
