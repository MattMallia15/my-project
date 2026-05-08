from flask import Flask, jsonify, send_from_directory, request
import json
import os
from datetime import datetime
from werkzeug.utils import secure_filename

app = Flask(__name__, static_folder='.')
ARTICLES_FILE = 'articles.json'
BIO_FILE = 'bio.json'

def load_articles():
    with open(ARTICLES_FILE, 'r') as f:
        return json.load(f)

def save_articles(articles):
    with open(ARTICLES_FILE, 'w') as f:
        json.dump(articles, f, indent=2)

def load_bio():
    with open(BIO_FILE, 'r') as f:
        return json.load(f)

def save_bio(bio):
    with open(BIO_FILE, 'w') as f:
        json.dump(bio, f, indent=2)

@app.route('/')
def index():
    return send_from_directory('.', 'bio.html')

@app.route('/articles')
def articles_page():
    return send_from_directory('.', 'index.html')

@app.route('/article.html')
def article_page():
    return send_from_directory('.', 'article.html')

@app.route('/admin.html')
def admin_page():
    return send_from_directory('.', 'admin.html')

@app.route('/bio.html')
def bio_page():
    return send_from_directory('.', 'bio.html')

@app.route('/api/bio', methods=['GET'])
def get_bio():
    return jsonify(load_bio())

@app.route('/api/bio', methods=['PUT'])
def update_bio():
    save_bio(request.json)
    return jsonify({'success': True})

@app.route('/api/bio/cv', methods=['POST'])
def upload_cv():
    if 'cv' not in request.files:
        return jsonify({'error': 'No file'}), 400
    file = request.files['cv']
    if not file.filename.lower().endswith('.pdf'):
        return jsonify({'error': 'PDF only'}), 400
    file.save(os.path.join('.', 'cv.pdf'))
    bio = load_bio()
    bio['has_cv'] = True
    save_bio(bio)
    return jsonify({'success': True})

@app.route('/cv')
def download_cv():
    if not os.path.exists('cv.pdf'):
        return jsonify({'error': 'No CV uploaded'}), 404
    return send_from_directory('.', 'cv.pdf', as_attachment=True,
                               download_name='Matthew_Mallia_CV.pdf')

@app.route('/api/articles', methods=['GET'])
def get_articles():
    category = request.args.get('category')
    articles = load_articles()
    if category:
        articles = [a for a in articles if a['category'] == category]
    articles.sort(key=lambda x: x['date'], reverse=True)
    return jsonify(articles)

@app.route('/api/articles/<int:article_id>', methods=['GET'])
def get_article(article_id):
    articles = load_articles()
    article = next((a for a in articles if a['id'] == article_id), None)
    if not article:
        return jsonify({'error': 'Not found'}), 404
    return jsonify(article)

@app.route('/api/articles', methods=['POST'])
def add_article():
    data = request.json
    articles = load_articles()
    new_id = max((a['id'] for a in articles), default=0) + 1
    article = {
        'id': new_id,
        'title': data['title'],
        'category': data['category'],
        'summary': data['summary'],
        'content': data['content'],
        'date': datetime.now().strftime('%Y-%m-%d')
    }
    articles.append(article)
    save_articles(articles)
    return jsonify(article), 201

@app.route('/api/articles/<int:article_id>', methods=['DELETE'])
def delete_article(article_id):
    articles = load_articles()
    articles = [a for a in articles if a['id'] != article_id]
    save_articles(articles)
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
