import pandas as pd

# URL dataset
url = "https://raw.githubusercontent.com/dr5hn/countries-states-cities-database/refs/heads/master/csv/cities.csv"

# Membaca dataset dari URL
df = pd.read_csv(url)

# Mengelompokkan kota berdasarkan negara dan menghitung jumlah kota per negara
city_counts = df['country_name'].value_counts(ascending=True).reset_index()
city_counts.columns = ['country_name', 'city_count']

# Mengurutkan hasil berdasarkan jumlah kota (ascending)
city_counts = city_counts.sort_values(by='city_count', ascending=True)

# Menyimpan hasil dalam format CSV
city_counts.to_csv("output.csv", index=False)

# Menyimpan hasil dalam format JSON
city_counts.to_json("output.json", orient="records", indent=4)

print("Proses selesai, Hasil disimpan dalam output.csv dan output.json")
