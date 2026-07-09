import joblib

# Učitaj model
model = joblib.load('moj_model.pkl')

# Interaktivno testiranje
while True:
    naslov = input("\nUnesi naziv proizvoda (ili 'kraj' za izlaz): ")
    if naslov.lower() == 'kraj':
        break
    predikcija = model.predict([naslov])
    print(f"Model predviđa kategoriju: {predikcija[0]}")