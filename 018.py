from math import cos, tan, sin, radians
ang = float(input('Digite o ângulo que deseja: '))
coss = cos(radians(ang))
tang = tan(radians(ang))
seno = sin(radians(ang))
print('O ângulo de {}° tem o SENO de {:.2f}'.format(ang, seno))
print('O ângulo de {}° tem a TANGENTE de {:.2f}'.format(ang, tang))
print('O ângulo de {}° tem o COSSENO de {:.2f}'.format(ang, coss))
