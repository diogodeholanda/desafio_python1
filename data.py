from datetime import datetime

data_hora_atual = datetime.now()
#data_hora_str = "2024-09-03 14:00"

mascara_ptbr = '%d/%m/%Y %a'

print(data_hora_atual.strftime(mascara_ptbr))