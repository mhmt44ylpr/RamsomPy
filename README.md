
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

```
   ____                                      
  / __ \____  ___  ____  ____  ____  ____ _
 / / / / __ \/ _ \/ __ \/ __ \/ __ \/ __ `/
/ /_/ / /_/ /  __/ /_/ / /_/ / /_/ / /_/ / 
\____/ .___/\___/ .___/ .___/ .___/\__,_/  
    /_/        /_/   /_/   /_/             

[10:21:55] Şifreleme başlıyor....
[10:21:55] Key Oluşturuldu.
[10:21:55] Şifreleme bitti....
```

---

## ⚖️ Lisans

MIT Lisansı altında sunulmuştur. Ayrıntılar için `LICENSE` dosyasına bakabilirsiniz.

---

## ✍️ Geliştirici

- **Adınız / Takma Adınız**
- 📫 GitHub: [github.com/kullanıcı_adı](https://github.com/kullanıcı_adı)

---

## ❗ Uyarı

Bu araç, sadece kişisel kullanım ve öğrenim amacıyla geliştirilmiştir. Kötü niyetli veya izinsiz kullanımda geliştirici sorumluluk kabul etmez.
