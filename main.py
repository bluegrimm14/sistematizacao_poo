from Funcionario import Funcionario
from Hospede import Hospede
from Quarto import Quarto
from Hotel import Hotel
from Reserva import Reserva

# Intanciação das classes.
hotel = Hotel()
func_1 = Funcionario("Fulano", "fulano@fulano.com")
hosp_1 = Hospede("Ciclano", "ciclano@ciclano.com")
quarto_1 = Quarto(1, "Single", True)
quarto_2 = Quarto(2, "Two Single", True)
quarto_3 = Quarto(3, "Cuple", True)

# Registro de reserva
func_1.add_quarto(hotel, quarto_1)
func_1.add_quarto(hotel, quarto_2)
func_1.add_quarto(hotel, quarto_3)

# Registrando Hospedes
func_1.registrar_hospede(hotel, hospede=hosp_1)

# Consultando a disponibilidade dos quartos
func_1.ver_disponibilidade(quarto_1)

# Efetuando a reserva"
reserva = Reserva(hosp_1, quarto_1)
hosp_1.fazer_reserva(reserva)
func_1.registrar_reserva(hotel, reserva)
func_1.ver_disponibilidade(quarto_1)

# Consultas de Quartos, Hóspedes e Reservas
#Reservasdo Hospede 1
print(hosp_1.reservas)

#Reservas registradas no Hotel:
print(hotel.reservas)

#Quartos Registrados no hotel
print(hotel.quartos)

#Hospedes Registrados o Hotel
print(hotel.hospedes)

# Cancelamento de Reservas e Remoção de Quartos
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

func_1.remover_quarto(hotel, quarto_3)

print(hotel.quartos)