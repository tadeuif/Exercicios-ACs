from Ex1_AC3_televisao import Televisao
tv = Televisao()
print(tv.ligada)
print(tv.canal)

tv_sala = Televisao()
tv_sala.ligada = True
tv_sala.canal = 5
print(tv.ligada)
print(tv.canal)
print(tv_sala.ligada)
print(tv_sala.canal)