class SequenciaNumerica:
    def __init__(self, lenght_list, list_num):
        self.lenght_list = lenght_list
        self.list_num = list_num

    def sequencia(self):
        return self.list_num

    def sequenciaCrescente(self):
        return sorted(self.list_num)


    