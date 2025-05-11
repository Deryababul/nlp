# 🧠 Natural Language Processing (NLP) Projects

Bu depo, çeşitli Doğal Dil İşleme (NLP) tekniklerini uygulamalı olarak barındıran projeleri içermektedir. Amaç, farklı metin işleme ve makine öğrenmesi yöntemlerini kullanarak metinlerden anlam çıkarma, analiz etme ve üretme üzerine kapsamlı bir çalışma sunmaktır.

## 🔍 İçerik

Aşağıdaki uygulamalar bu repoda yer almaktadır:

### 1. 💬 Duygu Analizi (Sentiment Analysis)
- Türkçe/İngilizce metinlerde pozitif, negatif ve nötr duygu sınıflandırması yapılır.
- Scikit-learn ve/veya TensorFlow kullanılmıştır.
- Veri temizleme, lemmatization ve stopword kaldırma gibi ön işlemler uygulanmıştır.

### 2. 🔁 Markov Zinciri ile Metin Üretimi
- Verilen bir metin korpusu üzerinden Markov Zinciri kurulup yeni, anlamlı cümleler üretilmiştir.
- N-gram yapısı ile olasılık dağılımı oluşturulmuştur.
- Örnek kullanım: edebi metinlerden yeni cümle üretme.

### 3. 📊 Naive Bayes ile Metin Sınıflandırma
- Naive Bayes algoritması ile metinlerin ait olduğu sınıf tahmini yapılır.
- TF-IDF veya Bag of Words gibi özellik çıkarımı yöntemleriyle model eğitimi sağlanmıştır.
- Uygulama örneği: haber başlıkları veya yorumların kategori sınıflandırması.

### 4. 🧮 TF-IDF ile Kelime Ağırlığı Hesaplama
- Belgelerde geçen kelimelerin önem dereceleri hesaplanır.
- Scikit-learn TF-IDF vectorizer kullanılarak kelime matrisleri oluşturulmuştur.
- Veri görselleştirme ile birlikte anlamlı kelimelerin analizi yapılmıştır.

### 5. 🧠 Word2Vec ile Kelime Gösterimleri
- Gensim kütüphanesi ile Word2Vec modeli eğitildi.
- Kelimeler vektör uzayında temsil edilerek benzerlikler hesaplandı.
- “most_similar”, “odd_one_out” gibi fonksiyonlarla uygulama örnekleri sunulmuştur.

---

## ⚙️ Kullanılan Teknolojiler

- Python 3.x  
- Scikit-learn  
- NLTK & SpaCy  
- Gensim  
- Pandas, NumPy  
- Matplotlib / Seaborn  

---

## 🚀 Başlangıç

Projeyi klonlamak için:

```bash
git clone https://github.com/Deryababul/nlp.git
