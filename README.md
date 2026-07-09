# Klasifikacija proizvoda - ML Projekat

Ovaj projekat implementira model mašinskog učenja za automatsku kategorizaciju proizvoda na osnovu njihovog naziva.

## Sadržaj projekta
- `model_razvoj.ipynb`: Jupyter radna sveska sa celokupnom analizom, pripremom podataka i procesom treniranja modela.
- `moj_model.pkl`: Istrenirani model sačuvan u .pkl formatu spreman za produkciju.
- `predict_category.py`: Python skripta za interaktivno testiranje modela (unos naziva -> predikcija kategorije).
- `IMLP6_TASK_03-products (2).csv`: Skup podataka korišćen za treniranje.

## Kako pokrenuti
1. Kloniraj repozitorijum.
2. Instaliraj potrebne biblioteke: 
   `pip install pandas scikit-learn joblib`
3. Pokreni testiranje:
   `python predict_category.py`
