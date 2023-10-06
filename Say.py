import random

yatma = random.randint(2, 11)
yatislar = []
for i in range(7):
    yatma = random.randint(3, 4)
    yatislar.append(yatma)

for i in range(80):
    yatma = random.randint(0, 3)
    yatislar.append(yatma)

random.shuffle(yatislar)
with open("mahsuni.txt", "w") as dosya:
    for yatis in yatislar:
        for sifirsay in range(yatis):
            dosya.write(str(0)+"\n")
        dosya.write(str(random.uniform(1.49, 1.8))[:4].replace(".",",")+"\n")

print("Metin dosyası güncellendi.")