# Sistem za automatsku kategorizaciju proizvoda

Ovaj projekat omogućava automatsku klasifikaciju proizvoda u odgovarajuće kategorije na osnovu njihovog naziva (Product Title), koristeći mašinsko učenje.

## Kako pokrenuti projekat
1. Instaliraj potrebne biblioteke:
   pip install pandas scikit-learn joblib
2. Pokreni skriptu za testiranje:
   python predict_category.py
3. Unesi naziv proizvoda kada te sistem pita.

## Tehnologija
- Model: Naivni Bajes (MultinomialNB)
- Vektorizacija: TF-IDF
- Preciznost: Visoka (proveriti u Jupyter svesci)

## Struktura
- `IMLP6_TASK_03-products (2).csv` - Ulazni podaci
- `moj_model.pkl` - Trenirani model spreman za upotrebu
- `predict_category.py` - Interaktivni skript za testiranje