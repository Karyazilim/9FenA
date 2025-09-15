# 9 Fen A - Öğrenci Galerisi

Responsive "9 Fen A" öğrenci galerisi web uygulaması. Flask framework'ü kullanılarak geliştirilmiştir.

## Özellikler

- Responsive tasarım (mobil, tablet, masaüstü uyumlu)
- Türkçe arayüz
- JSON tabanlı veri yönetimi
- Material Design ikonları
- Tailwind CSS ile modern stil
- Masonry grid layout
- Hover efektleri

## Gereksinimler

- Python >= 3.10
- Flask 3.0.0
- Gunicorn (isteğe bağlı, production deployment için)

## Kurulum

1. **Sanal ortam oluşturun:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # veya
   venv\Scripts\activate     # Windows
   ```

2. **Bağımlılıkları yükleyin:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Uygulamayı çalıştırın:**
   ```bash
   flask --app app run --debug
   ```

4. **Tarayıcınızda açın:**
   http://127.0.0.1:5000

## API Endpoints

- `GET /` - Ana galeri sayfası
- `GET /api/items` - Galeri öğelerini JSON formatında döndürür
- `GET /ekle` - Yeni öğe ekleme sayfası (placeholder)

## Dosya Yapısı

```
9FenA/
├── app.py                 # Flask uygulaması
├── requirements.txt       # Python bağımlılıkları
├── data/
│   └── gallery.json      # Galeri verileri
├── templates/
│   └── index.html        # Ana sayfa şablonu
├── static/               # Statik dosyalar (isteğe bağlı)
├── README.md             # Bu dosya
└── .gitignore           # Git ignore kuralları
```

## Veri Modeli

`data/gallery.json` dosyası aşağıdaki formatta galeri öğelerini içerir:

```json
[
  {
    "title": "Öğe Başlığı",
    "author": "Yazar Adı",
    "image_url": "https://example.com/image.jpg"
  }
]
```

## Production Deployment

Gunicorn ile production ortamında çalıştırmak için:

```bash
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

## Geliştirme

Yeni galeri öğeleri eklemek için `data/gallery.json` dosyasını düzenleyin. Uygulama otomatik olarak yeni verileri yükleyecektir.

## Lisans

MIT License - Detaylar için `LICENSE` dosyasına bakın.