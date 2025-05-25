
# 🛡️ RamsomPy

**RamsomPy**, bir klasördeki dosyaları **şifrelemek** ve ardından istenildiğinde aynı anahtar ile **çözmek** için hazırlanmış basit ama etkili bir dosya şifreleme aracıdır. `cryptography`, `colorama`, `pyfiglet`, `rich` gibi kütüphaneleri kullanarak terminal çıktısını zenginleştirir.

> ⚠️ Bu araç sadece **eğitim amaçlı** geliştirilmiştir. İzinsiz kullanım yasal sonuçlara yol açabilir.

---

## 📦 Özellikler

- AES tabanlı güvenli dosya şifreleme (Fernet)
- Otomatik key üretimi ve kaydetme
- Renkli ve şık terminal çıktısı
- Belirli uzantılar yerine tüm dosyaları hedef alır
- Hatalı key kullanımı algılama

---

## 🔧 Kurulum

### Gerekli Python Sürümü:
```bash
Python 3.6+
```

### Gereksinimler:
```bash
pip install cryptography colorama pyfiglet rich
```

---

## 🚀 Kullanım

### 🔐 Şifreleme

```bash
python encrypgraph.py -p /hedef/klasor/yolu
```

- `-p` veya `--path` parametresi zorunludur.
- Şifreleme sonucunda `generated.key` dosyası otomatik olarak aynı dizine kaydedilir.

### 🔓 Şifre Çözme

```bash
python decrypgraph.py -p /hedef/klasor/yolu -k <şifreleme_key>
```

- `-p`: Şifreli dosyaların bulunduğu klasör
- `-k`: Daha önce oluşturulmuş olan `generated.key` içeriği

> Örnek:
```bash
python decrypgraph.py -p ./test_dosyalar -k "eCw4W...rest_of_key"
```

---

## 📁 Dosya Yapısı

```text
project-folder/
│
├── encrypgraph.py      # Şifreleme aracı
├── decrypgraph.py      # Şifre çözme aracı
├── generated.key       # (Oluşturulur) Fernet anahtarı
└── README.md           # Bu dosya
```

---

## 🧪 Örnek Ekran Çıktısı
![Ekran görüntüsü 2025-05-25 161939](https://github.com/user-attachments/assets/110c1361-f7bb-4764-8cb2-72aeb53760df)
-----------------------------------------------------------------
![Ekran görüntüsü 2025-05-25 161951](https://github.com/user-attachments/assets/e519cbdb-b1f7-4d33-8c5c-ce92671864b8)



## ⚖️ Lisans

MIT Lisansı altında sunulmuştur. Ayrıntılar için `LICENSE` dosyasına bakabilirsiniz.

---

## ✍️ Geliştirici

- **CHARON**
- 📫 GitHub: [github.com/mhmt44ylpr](https://github.com/mhmt44ylpr)

---

## ❗ Uyarı

Bu araç, sadece kişisel kullanım ve öğrenim amacıyla geliştirilmiştir. Kötü niyetli veya izinsiz kullanımda geliştirici sorumluluk kabul etmez.
