class Kafe:
    def __init__(self, ad, sehir):
        self.ad = ad
        self.sehir = sehir

        self.urunler = {
            "kahve": {
                "fiyat": 60,
                "stok": 10
            },
            "çay": {
                "fiyat": 25,
                "stok": 15
            },
            "sandviç": {
                "fiyat": 90,
                "stok": 8
            },
            "cheesecake": {
                "fiyat": 110,
                "stok": 5
            }
        }

        self.sepet = []
        self.satilan_urunler = set()
        self.gunluk_kazanc = 0

    def kafe_bilgilerini_goster(self):
        kafe_bilgileri = (
            self.ad,
            self.sehir,
            "09.00 - 22.00"
        )

        print("\n--- KAFE BİLGİLERİ ---")
        print("Kafe:", kafe_bilgileri[0])
        print("Şehir:", kafe_bilgileri[1])
        print("Çalışma saatleri:", kafe_bilgileri[2])

    def urunleri_goster(self):
        print("\n--- ÜRÜNLER ---")

        for urun_adi, bilgiler in self.urunler.items():
            print(
                f"{urun_adi.title()} - "
                f"{bilgiler['fiyat']} TL - "
                f"Stok: {bilgiler['stok']}"
            )

    def sepete_urun_ekle(self):
        self.urunleri_goster()

        urun_adi = input(
            "\nSepete eklemek istediğiniz ürün: "
        ).lower()

        if urun_adi not in self.urunler:
            print("Böyle bir ürün bulunamadı.")
            return

        adet = int(input("Kaç adet istiyorsunuz?: "))

        if adet <= 0:
            print("Adet sıfırdan büyük olmalıdır.")
            return

        mevcut_stok = self.urunler[urun_adi]["stok"]

        if adet > mevcut_stok:
            print("Yeterli stok bulunmuyor.")
            print("Mevcut stok:", mevcut_stok)
            return

        sepetteki_adet = 0

        for urun in self.sepet:
            if urun["urun"] == urun_adi:
                sepetteki_adet += urun["adet"]

        if sepetteki_adet + adet > mevcut_stok:
            print("Sepetteki ürünlerle birlikte stok aşılıyor.")
            print("Mevcut stok:", mevcut_stok)
            print("Sepette bulunan adet:", sepetteki_adet)
            return

        sepet_urunu = {
            "urun": urun_adi,
            "adet": adet,
            "birim_fiyat": self.urunler[urun_adi]["fiyat"]
        }

        self.sepet.append(sepet_urunu)

        print(f"{adet} adet {urun_adi} sepete eklendi.")

    def sepeti_goster(self):
        print("\n--- SEPET ---")

        if len(self.sepet) == 0:
            print("Sepetiniz boş.")
            return

        toplam_tutar = 0

        for urun in self.sepet:
            urun_adi = urun["urun"]
            adet = urun["adet"]
            birim_fiyat = urun["birim_fiyat"]

            urun_toplami = adet * birim_fiyat
            toplam_tutar += urun_toplami

            print(
                f"{urun_adi.title()} - "
                f"{adet} adet - "
                f"{urun_toplami} TL"
            )

        print("--------------------")
        print("Toplam tutar:", toplam_tutar, "TL")

    def siparisi_tamamla(self):
        if len(self.sepet) == 0:
            print("Sepet boş.")
            return

        siparis_toplami = 0

        for urun in self.sepet:
            urun_adi = urun["urun"]
            adet = urun["adet"]
            birim_fiyat = urun["birim_fiyat"]

            self.urunler[urun_adi]["stok"] -= adet
            siparis_toplami += adet * birim_fiyat

            self.satilan_urunler.add(urun_adi)

        self.gunluk_kazanc += siparis_toplami

        print("\nSipariş başarıyla tamamlandı.")
        print("Ödenen tutar:", siparis_toplami, "TL")

        self.sepet.clear()

    def satilan_urunleri_goster(self):
        print("\n--- SATILAN FARKLI ÜRÜNLER ---")

        if len(self.satilan_urunler) == 0:
            print("Henüz ürün satılmadı.")
            return

        for urun in self.satilan_urunler:
            print("-", urun.title())

    def kazanci_goster(self):
        print("\nGünlük toplam kazanç:", self.gunluk_kazanc, "TL")

    def menu(self):
        while True:
            print("\n==========================")
            print(self.ad.upper())
            print("==========================")
            print("1- Kafe bilgilerini göster")
            print("2- Ürünleri göster")
            print("3- Sepete ürün ekle")
            print("4- Sepeti göster")
            print("5- Siparişi tamamla")
            print("6- Satılan ürünleri göster")
            print("7- Günlük kazancı göster")
            print("0- Programdan çık")

            secim = input("\nSeçiminiz: ")

            if secim == "1":
                self.kafe_bilgilerini_goster()

            elif secim == "2":
                self.urunleri_goster()

            elif secim == "3":
                self.sepete_urun_ekle()

            elif secim == "4":
                self.sepeti_goster()

            elif secim == "5":
                self.siparisi_tamamla()

            elif secim == "6":
                self.satilan_urunleri_goster()

            elif secim == "7":
                self.kazanci_goster()

            elif secim == "0":
                print("Program kapatıldı.")
                break

            else:
                print("Geçersiz seçim yaptınız.")


kafe = Kafe("Python Kafe", "İstanbul")
kafe.menu()