class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 2
    
    def aumenta_canal(self):
        print('aumentar canal')
        self.canal += 1
        

    def diminui_canal(self):
        print('diminuir canal')
        self.canal -= 1
        