from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__)

def load_gallery_data():
    """Load gallery data from JSON file"""
    try:
        with open('data/gallery.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

@app.route('/')
def index():
    """Main gallery page"""
    items = load_gallery_data()
    return render_template('index.html', items=items)

@app.route('/api/items')
def api_items():
    """API endpoint to get gallery items as JSON"""
    items = load_gallery_data()
    return jsonify(items)

@app.route('/test')
def test():
    """Test version without external dependencies"""
    items = load_gallery_data()
    return render_template('test.html', items=items)

@app.route('/ekle')
def add_item():
    """Placeholder route for adding new items"""
    return """
    <h1>Yeni Öğe Ekle</h1>
    <p>TODO: Bu sayfada yeni galeri öğeleri ekleme fonksiyonu geliştirilecek.</p>
    <a href="/">← Galeriye Dön</a>
    """

if __name__ == '__main__':
    app.run(debug=True)