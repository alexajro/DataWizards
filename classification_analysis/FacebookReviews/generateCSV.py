import csv

# Supongamos que word_counts es tu diccionario de conteo de palabras
with open('word_counts.csv', 'w', newline='', encoding = 'utf-8') as csvfile:
    with open('diff_words.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        writer = csv.writer(csvfile)
        for row in reader:
            word = row[1]
            count = int(row[0])
            for _ in range(count):
                writer.writerow([word])