from Funcionario import Funcionario
from Hospede import Hospede
from Quarto import Quarto
from Hotel import Hotel
from Reserva import Reserva
from Pessoa import Pessoa

# Intanciação das classes.
print("Etapa 1: Instanciando os objetos\n", "-"*20)
hotel = Hotel()
func_1 = Funcionario("Terry", "terry@terry.com")
hosp_1 = Hospede("Millena", "millena@millena.com")
quarto_1 = Quarto(1, "Single", True)
quarto_2 = Quarto(2, "Two Single", True)
quarto_3 = Quarto(3, "Cuple", True)

# Registro de reserva
print("\nEstapa 2: Registro de Reservas\n", "-"*20)
print("Adicionando os quartos ao Hotel.")
func_1.add_quarto(hotel, quarto_1)
func_1.add_quarto(hotel, quarto_2)
func_1.add_quarto(hotel, quarto_3)

print("Registrando Hospedes")
func_1.registrar_hospede(hotel, hospede=hosp_1)

print("Consultando a disponibilidade dos quartos")
func_1.ver_disponibilidade(quarto_1)

print("Efetuando a reserva")
reserva = Reserva(hosp_1, quarto_1)
hosp_1.fazer_reserva(reserva)
func_1.registrar_reserva(hotel, reserva)
func_1.ver_disponibilidade(quarto_1)

# Consultas de Quartos, Hóspedes e Reservas
print("\nEtapa 3: Consultas de Quartos, Hóspedes e Reservas\n", "-"*20)
#Reservasdo Hospede 1
print(hosp_1.reservas)

#Reservas registradas no Hotel:
print(hotel.reservas)

#Quartos Registrados no hotel
print(hotel.quartos)

#Hospedes Registrados o Hotel
print(hotel.hospedes)

# Cancelamento de Reservas
print("\nEtapa 4: Cancelamento de Reservas\n", "-"*20)
# Consultando a primeira reserva do Hospede 1
print(hosp_1.reservas[0])
func_1.ver_disponibilidade(quarto_1)
hosp_1.cancelar_reserva(reserva)
#Consulta as reservas de hospede
print(hosp_1.reservas)

func_1.cancelar_reserva(hotel, reserva)
func_1.ver_disponibilidade(quarto_1)

#Consultando Reservas, Hospedes e Quartos do Hotel
print(hotel.reservas)
print(hotel.hospedes)
print(hotel.quartos)

