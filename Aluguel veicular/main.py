import fn_diaria

fn_diaria.mostralinha()
aluguel = int(input('Informe a quantidade de diarias: '))
fn_diaria.mostralinha()
kmi = int(input('Informe a quilometragem inicial: '))
fn_diaria.mostralinha()
kmf = int(input('Informe a quilometragem final: '))

diaria = 60.00
kmr = 0.18

calcd = fn_diaria.calcular_diaria(diaria, aluguel)
calck = fn_diaria.calcular_km(kmi, kmf, kmr)

fn_diaria.mostralinha()
print('RESULTADO')


fn_diaria.mostralinha()
print('A quantidade de diarias: ', aluguel)

fn_diaria.mostralinha()
print('Quilometros Rodados', calck/aluguel)

fn_diaria.mostralinha()
print('O valor a ser pago pelo cliente: ', calcd + calck)
fn_diaria.mostralinha()
