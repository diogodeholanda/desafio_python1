from datetime import datetime

data_hora_atual = datetime.now()
data_hora_str = "2024-09-06 12:50"
mascara_ptbr = "%d/%m/%y - %H:%M - %A"
mascara_en = "%Y-%m-%d  %H:%M"

print(data_hora_atual.strftime(mascara_ptbr))

print(data_hora_atual.strftime("%d"))

print(data_hora_atual.strftime("%m"))

print(data_hora_atual.strftime("%Y"))


data_desconvertida = datetime.strptime(data_hora_str, mascara_en)
print(data_desconvertida)