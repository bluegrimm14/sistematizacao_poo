from Funcionario import Funcionario
from Hospede import Hospede
from Quarto import Quarto
from Hotel import Hotel

hotel = Hotel()

quarto_1 = Quarto(1, "Single", True)
quarto_2 = Quarto(2, "Cuple", True)
print(quarto_1.numero)
print(quarto_1.tipo)
print(quarto_1.disponivel)

funci_1 = Funcionario("Terry", "terryrogerps@gmail.com")
print(funci_1)

hosp_1 = Hospede("Millena", "mihlucia@gmail.com", [])
print(hosp_1)

print("-"*10)
funci_1.add_quarto(hotel, quarto_1)
funci_1.add_quarto(hotel, quarto_2)
print(hotel.quartos[0],"\n",hotel.quartos[1])
