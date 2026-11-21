# 1. random kütüphanesini içe aktar
import random

# 2. Makine: 1-100 arası rastgele bir sayı seçip geri veren "sayi_tut"
def sayi_tut():
    return random.randint(1, 100)

# 3. Makine: kullanıcıdan sayı isteyen "tahmin_al"
def tahmin_al():
    while True:
        tahmin = input("1 ile 100 arasında bir sayı tahmin edin: ")
        try:
            tahmin = int(tahmin)
            if 1 <= tahmin <= 100:
                return tahmin
            else:
                print("Lütfen 1 ile 100 arasında bir sayı girin.")
        except ValueError:
            print("Geçerli bir sayı girin.")

# 4. Makine: tahmin ile gizli sayıyı karşılaştırıp ipucu yazan "ipucu_ver"
def ipucu_ver(sonuc, tahmin_edilen):
    if tahmin_edilen < sonuc:
        print("Daha büyük bir sayı deneyin.")
    else:                                              # 🔸 elif yerine else, "Tebrikler" kalktı
        print("Daha küçük bir sayı deneyin.")

# 5. Oyun başlıyor                                     # 🔸 makinelerin ALTINA taşındı
sonuc = sayi_tut()
tahmin_edilen = tahmin_al()
tahminler = [tahmin_edilen]

# 6. Tahmin doğru olana kadar tekrarla
while tahmin_edilen != sonuc:
    ipucu_ver(sonuc, tahmin_edilen)
    tahmin_edilen = tahmin_al()                        # 🔸 EKSİK OLAN SATIR: yeni tahmin
    tahminler.append(tahmin_edilen)

# 7. Sonuçları yaz                                     # 🔸 yeni
print("Tebrikler! Doğru tahmin.")
print("Tahminlerin:", tahminler)
print(len(tahminler), "tahminde bildin.")