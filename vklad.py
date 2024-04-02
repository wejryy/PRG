vklad = 1000
roky = 10
urok = 0.05

hodnota = vklad
for rok in range(roky):
    hodnota *= urok + 1

print("Hodnota vašeho vkladu po {roky} letech při {urok * 100: .0f}% úrokové sazbě je {hodnota} Kč.")