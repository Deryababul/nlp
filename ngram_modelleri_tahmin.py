# Import necessary libraries
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.util import ngrams
from nltk.probability import FreqDist

# Download NLTK resources if not already downloaded
nltk.download('punkt')

# Metin örneği
text = "Merhaba dünya. Bu bir örnek metindir. Doğal dil işleme eğlencelidir."

# Küçük harfe çevirme ve noktalama kaldırma
text = text.lower()
text = re.sub(r'[^\w\s]', '', text)

# Kelimelere ayırma (tokenizasyon)
tokens = word_tokenize(text)

# Unigram (Tek kelimeler)
unigrams = list(tokens)

# Bigram (İkili kelime grupları)
bigrams = list(ngrams(tokens, 2))

# Trigram (Üçlü kelime grupları)
trigrams = list(ngrams(tokens, 3))

# Frekans dağılımlarını oluşturma
unigram_freq = FreqDist(unigrams)
bigram_freq = FreqDist(bigrams)
trigram_freq = FreqDist(trigrams)

# Örnek çıktı: En sık geçen ilk 5 unigram
print("Unigram en sık geçenler:", unigram_freq.most_common(5))
print("Bigram en sık geçenler:", bigram_freq.most_common(5))
print("Trigram en sık geçenler:", trigram_freq.most_common(5))

# Bigram tahmini için
prev_word = "doğal"
next_word_options = [b[1] for b in bigram_freq.keys() if b[0] == prev_word]

print(f'"{prev_word}" kelimesinden sonra gelebilecek kelimeler: {next_word_options}')

# Kullanıcının girdiği kelimeyle tahmin yapalım
input_text = "doğal dil"
input_tokens = input_text.split()

# Eğer bigram modelindeysek
if len(input_tokens) == 1:
    next_word = [b[1] for b in bigram_freq.keys() if b[0] == input_tokens[0]]

# Eğer trigram modelindeysek
elif len(input_tokens) == 2:
    next_word = [t[2] for t in trigram_freq.keys() if t[0] == input_tokens[0] and t[1] == input_tokens[1]]

print(f'"{input_text}" ifadesinden sonra en olası kelime(ler): {next_word}')