notaA = float(input('informe a primeira nota: '))
notaB = float(input('informe a segunda nota: '))

mediaFinal = (notaA + notaB) / 2

if mediaFinal >=7.0:
    print('A media: %.f - Aprovado ' % mediaFinal)
else:
    print('A media: %.1f - Reprovado ' % mediaFinal)
