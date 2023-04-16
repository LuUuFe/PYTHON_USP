segundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))
dias = segundos // 86400
segundos_restantes = segundos % 86400
horas = segundos_restantes // 3600
segundos_restantes = segundos % 3600
minutos = segundos_restantes // 60
segundos_restantes = segundos % 60
print(dias,"dias,",horas,"horas,",minutos,"minutos e",segundos_restantes,"segundos.")