from datetime import date, datetime

data = date(2023, 1, 1)# se quiser exibir a data de hoje uso date.today()
mascara_ptbr = '%d/%m/%Y'

print(data.strftime(mascara_ptbr))

data_hora = datetime(2024, 9 , 5, 10, 30, 20)
print (data_hora)

data_hoje = date.today()#imprimi somente a data
print(data_hoje)

print(datetime.today())#imprimi data e hora