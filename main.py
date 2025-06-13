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
print("Registro de Reservas\n", "-"*20)
func_1.add_quarto(hotel, quarto_1)
func_1.add_quarto(hotel, quarto_2)
func_1.add_quarto(hotel, quarto_3)
print(hotel.quartos)

func_1.registrar_hospede(hotel, hospede=hosp_1)
print(hotel.hospedes)

reserva = Reserva(hosp_1, quarto_1)
func_1.registrar_reserva(hotel, reserva)
print(hotel.reservas[0])

# Consultas de Reservas
print("Registro de Reservas\n", "-"*20)


# Cancelamento de Reservas
print("Registro de Reservas\n", "-"*20)



# hotel = Hotel()

# quarto_1 = Quarto(1, "Single", True)
# quarto_2 = Quarto(2, "Cuple", True)
# print(quarto_1.numero)
# print(quarto_1.tipo)
# print(quarto_1.disponivel)

# funci_1 = Funcionario("Terry", "terryrogerps@gmail.com")
# print(funci_1)

# hosp_1 = Hospede("Millena", "mihlucia@gmail.com", [])
# print(hosp_1)

# print("-"*10)
# funci_1.add_quarto(hotel, quarto_1)
# funci_1.add_quarto(hotel, quarto_2)
# print(hotel.quartos[0],"\n",hotel.quartos[1])
