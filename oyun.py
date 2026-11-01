import random

gizlisayi = random.randint(1, 100)
tahmin = int(input("1 ile 100 arasında bir sayı giriniz: "))
tahminler = [tahmin]


while tahmin != gizlisayi:
    if tahmin < gizlisayi:
        print("Daha büyük bir sayı dene")
    elif tahmin > gizlisayi:
        print("Daha küçük bir sayı dene")
    tahmin = int(input("1 ile 100 arasında bir sayı giriniz: "))
    tahminler.append(tahmin)
print("Tebrikler, bildin!")
print("Tahminlerin:", tahminler)
print(len(tahminler), "tahminde bildin.")



