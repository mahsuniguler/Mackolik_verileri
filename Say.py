import random

yatma = []
for i in range(20):
    Sayi = random.randint(4, 5)
    yatma.append(Sayi)

for i in range(1000):
    Sayi = random.randint(0, 3)
    yatma.append(Sayi)

for i in range(20000):
    Sayi = random.randint(0, 2)
    yatma.append(Sayi)

toplm = 0
say = 0

random.shuffle(yatma)
sira = 1
with open("YükselenOranlar.txt", "w") as yaz:
    for yatis in yatma:
        for sifirsay in range(yatis):
            if sira == 380:
                break
            yaz.write(str(0) + "\n")
            sira += 1
        if sira == 380:
            break
        oran = round(random.uniform(1.65, 1.77), 2)
        toplm += oran
        yaz.write(str(oran).replace(".", ",") + "\n")
        sira += 1
        say += 1
        continue
    say += 1
    toplm += oran
    yaz.write(str(oran).replace(".", ",") + "\n")
    yaz.close()

oranlist = []

with open("YükselenOranlar.txt", "r") as oku:
    for line in oku:
        oran = line.strip().replace(",", ".")
        oranlist.append(float(oran))

with open("SabitOranlar.txt", "w") as S_Oran:
    for a in oranlist:
        if int(a) == 0:
            oran = round(random.uniform(1.6, 1.67), 2)
            S_Oran.write(str(oran).replace(".", ",") + "\n")

        else:
            S_Oran.write(str(0) + "\n")
            continue
S_Oran.close()

print(say)
print(toplm)
print(f"Ortalama {toplm / say}")
print("Metin dosyası güncellendi.")
