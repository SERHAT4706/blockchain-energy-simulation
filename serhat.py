import hashlib
import datetime
import random
import time

# --- BÖLÜM 1: BLOCKCHAIN YAPISI (Buraya dokunmana gerek yok) ---
# Bu kısım yapılan her alışverişi şifreli bir deftere kaydeder.

class Blok:
    def __init__(self, index, zaman, islem_detayi, onceki_sifre):
        self.index = index
        self.zaman = zaman
        self.islem_detayi = islem_detayi
        self.onceki_sifre = onceki_sifre # Bir önceki bloğun şifresi (Zincir mantığı)
        self.kendi_sifresi = self.sifre_olustur()

    def sifre_olustur(self):
        # Verileri karıştırıp karmaşık bir şifre (Hash) oluşturur
        veri_birlestir = str(self.index) + str(self.zaman) + str(self.islem_detayi) + str(self.onceki_sifre)
        return hashlib.sha256(veri_birlestir.encode()).hexdigest()

# --- BÖLÜM 2: SENARYO VE SİMÜLASYON ---

print("--- MAHALLE ENERJİ BORSASI SİMÜLASYONU BAŞLATILIYOR ---\n")

# Blockchain defterimizi oluşturuyoruz (İlk sayfa boş)
blockchain = [Blok(0, datetime.datetime.now(), "Başlangıç Bloğu", "0")]

# İki karakterimiz var:
# Ahmet: Çatısında Güneş Paneli var (Üretici)
# Ayşe: Evden çalışıyor, elektriğe ihtiyacı var (Tüketici)

toplam_kar = 0 # Ahmet'in kazancı

# Simülasyon: Günün 24 Saati dönüyor
for saat in range(0, 24):
    
    print(f"\nSaat: {saat}:00")
    
    # 1. Enerji Üretim/Tüketim Durumu (Basit Mantık)
    # Güneş sabah 06:00 ile 18:00 arası vardır.
    if 7 <= saat <= 18:
        ahmet_uretim = random.randint(5, 10) # Ahmet panelden 5-10 kW üretiyor
    else:
        ahmet_uretim = 0 # Gece üretim yok

    ahmet_kullanim = 2 # Ahmet'in evi sabit 2 kW harcıyor
    ayse_ihtiyac = random.randint(3, 6) # Ayşe'nin 3-6 kW ihtiyacı var

    # Ahmet'in satabileceği fazlası var mı?
    ahmet_fazla_enerji = ahmet_uretim - ahmet_kullanim

    # 2. ALIM - SATIM KARARI (YAPAY ZEKA KISMI BURASI)
    if ahmet_fazla_enerji > 0:
        # Ahmet'in satacak malı var!
        satis_miktari = min(ahmet_fazla_enerji, ayse_ihtiyac) # Ayşe'nin ihtiyacı kadar sat
        fiyat = 3.5 # Şebekeden ucuz, Ahmet'ten pahalı (Fiyat: 3.5 TL)
        kazanc = satis_miktari * fiyat
        toplam_kar += kazanc

        # 3. İŞLEMİ BLOCKCHAIN'E KAYDETME
        islem_mesaji = f"Ahmet -> Ayşe'ye {satis_miktari} kW elektrik sattı. Tutar: {kazanc} TL"
        
        # Yeni blok oluştur ve zincire ekle
        onceki_blok = blockchain[-1]
        yeni_blok = Blok(len(blockchain), datetime.datetime.now(), islem_mesaji, onceki_blok.kendi_sifresi)
        blockchain.append(yeni_blok)

        print(f"✅ İŞLEM BAŞARILI: {islem_mesaji}")
        print(f"   🔒 Blok Şifresi (Hash): {yeni_blok.kendi_sifresi[0:15]}...") # Şifrenin ilk 15 harfi

    else:
        print("❌ Satış Yok: Ahmet'in fazladan enerjisi yok, Ayşe şebekeden alıyor.")

    # Küçük bir bekleme efekti (gerçekçi olsun diye)
    # time.sleep(0.1) 

print("\n------------------------------------------------")
print(f"GÜN SONU RAPORU: Ahmet komşusuna satıştan toplam {toplam_kar} TL kazandı!")
print(f"Toplam Blok Sayısı: {len(blockchain)}")
print("------------------------------------------------")