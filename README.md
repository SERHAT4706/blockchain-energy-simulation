# Blockchain Tabanlı P2P Enerji Ticareti Simülasyonu 

Bu proje, yerel bir enerji ağında (Microgrid) üretici ve tüketici arasındaki enerji alışverişini simüle eder. İşlemler, Python kullanılarak oluşturulan basit bir **Blockchain (Blokzincir)** yapısı üzerinde şifreli olarak saklanır.

##  Özellikler
* **Enerji Üretim Simülasyonu:** Güneş paneli verimi saate göre (gündüz/gece) değişir.
* **Akıllı Kontrat Mantığı:** Fazla enerji varsa ve komşunun ihtiyacı varsa otomatik satış gerçekleşir.
* **Blockchain Kaydı:** Her enerji satışı, SHA-256 şifreleme algoritması ile bir blok olarak zincire eklenir.
* **Dinamik Fiyatlandırma:** Şebekeden daha ucuz, satıştan daha karlı bir orta yol fiyatı belirlenir.

##  Kullanılan Teknolojiler
* **Dil:** Python 3
* **Kütüphaneler:** Hashlib (Şifreleme için), Random (Veri üretimi için), Datetime.

##  Nasıl Çalıştırılır?
Bilgisayarınızda Python yüklüyse terminalden şu komutu girin:
`python main.py`
