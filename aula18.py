from math import radians, sin, cos, tan

an = int(input('Digite o ângulo que você deseja '))
seno = sin(radians(an))
cosseno = cos(radians(an))
tg = tan(radians(an))

print('O ângulo de {} tem o SENO de {:.2f}, COSSENO {:.2f} e TANGENTE {:.2f}'.format(an, seno, cosseno, tg))
