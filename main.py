from Funcionario import Funcionario
from Hospede import Hospede
from Quarto import Quarto
from Hotel import Hotel
from Reserva import Reserva


# Intanciação das classes.
print("Instanciando os objetos\n", "-"*20)
hotel = Hotel()
func_1 = Funcionario("Terry", "terry@terry.com")
hosp_1 = Hospede("Millena", "millena@millena.com")
quarto_1 = Quarto(1, "Single", True)
quarto_2 = Quarto(2, "Two Single", True)
quarto_3 = Quarto(3, "Cuple", True)



# Registro de reserva
print("\nRegistro de Reservas\n", "-"*20)
func_1.add_quarto(hotel, quarto_1)
func_1.add_quarto(hotel, quarto_2)
func_1.add_quarto(hotel, quarto_3)


func_1.registrar_hospede(hotel, hospede=hosp_1)
print(hotel.hospedes)

func_1.ver_disponibilidade(quarto_1)

reserva = Reserva(hosp_1, quarto_1)
hosp_1.fazer_reserva(reserva)
func_1.registrar_reserva(hotel, reserva)
# print(hotel.reservas[0])
func_1.ver_disponibilidade(quarto_1)

# Consultas de Reservas
print("\nRegistro de Reservas\n", "-"*20)


# Cancelamento de Reservas
print("\nRegistro de Reservas\n", "-"*20)