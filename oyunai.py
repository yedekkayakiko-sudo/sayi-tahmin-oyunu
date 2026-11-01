import random

def sayi_tahmin_oyunu():
    tutulan_sayi = random.randint(1, 100)
    tahminler = []

    print("1 ile 100 arasında tuttuğum sayıyı tahmin et!")

    while True:
        giris = input("Tahminin: ").strip()

        try:
            tahmin = int(giris)
        except ValueError:
            print("Lütfen bir tam sayı gir.")
            continue

        if not 1 <= tahmin <= 100:
            print("Tahminin 1 ile 100 arasında olmalı.")
            continue

        tahminler.append(tahmin)

        if tahmin < tutulan_sayi:
            print("Daha büyük!")
        elif tahmin > tutulan_sayi:
            print("Daha küçük!")
        else:
            print(f"Bildin! Sayı {tutulan_sayi}.")
            print(f"{len(tahminler)} tahminde bildin.")
            print("Tahminlerin:", tahminler)
            break


if __name__ == "__main__":
    sayi_tahmin_oyunu()
