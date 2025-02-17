# Nomor 1

Diminta untuk memproses sebuah kalimat dengan mengganti beberapa kata dalam kalimat tersebut menggunakan kata akar (root words) yang diberikan. Kata-kata dalam kalimat yang memiliki awalan yang cocok dengan salah satu kata akar harus diganti dengan kata akar tersebut, dengan prioritas pada kata akar yang terpendek. Jika tidak ada kata akar yang cocok, kata tersebut tetap seperti semula. Disini saya menggunakan JavaScript untuk mengimplementasikan solusi dari soal ini. Pendekatan yang digunakan adalah dengan memecah kalimat menjadi kata-kata, kemudian memeriksa setiap kata satu per satu apakah ada kata akar yang cocok sebagai awalan. Jika ditemukan kata akar yang lebih pendek dari kata yang sedang diproses, maka kata tersebut akan diganti dengan kata akar tersebut. Jika tidak, kata tetap seperti semula.

## Code

```javascript
function replaceWords(kataAkar, kalimat) {
    // Memecah kalimat menjadi kata-kata
    const words = kalimat.split(" ");

    // Iterasi setiap kata dalam kalimat dan menggantinya dengan akar kata terpendek jika sesuai
    return words.map(word => {
        let replacement = word;
        for (const root of kataAkar) {
            // Jika kata diawali dengan kata akar dan kata akar lebih pendek, gantikan kata
            if (word.startsWith(root) && root.length < replacement.length) {
                replacement = root;
            }
        }
        return replacement;
    }).join(" "); // Gabungkan kata-kata yang telah diganti menjadi kalimat
}

// Soal 1
console.log(replaceWords(["cat", "bat", "rat"], "the cattle was rattled by the battery"));

// Soal 2
console.log(replaceWords(["dog", "car", "bike"], "the dogs were barking near the cars and bikers"));
```

## Output
```
the cat was rat by the bat
the dog were barking near the car and bike
```
# Nomor 2

Diberikan dataset yang berisi daftar kota dari berbagai negara dalam format CSV. Dataset ini berisi nama negara dan kota-kota yang ada dalam negara tersebut. Tugas nya adalah untuk memproses dataset tersebut dengan cara mengelompokkan kota berdasarkan negara yang tercantum di dalam kolom country_name dan menghitung jumlah kota di setiap negara. Hasilnya harus disajikan dalam urutan menurun berdasarkan jumlah kota di setiap negara. Untuk nomor 2 saya menggunakan python dan menggunakan library pandas yang digunakan untuk membaca dataset dalam format csv, Setelah data dimuat, saya menggunakan metode value_counts() dari pandas untuk menghitung jumlah kota di setiap negara, Selanjutnya, saya menggunakan sort_values() untuk mengurutkan hasil perhitungan jumlah kota berdasarkan nilai yang dihasilkan, dengan negara yang memiliki jumlah kota paling sedikit (ascending) muncul terlebih dahulu.
## Code

```python
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

print("Proses selesai! Hasil disimpan dalam output.csv dan output.json")

```

## Output
```
[
  {
    "country_name": "South Sudan",
    "city_count": 1
  },
  {
    "country_name": "Sao Tome and Principe",
    "city_count": 5
  },
  {
    "country_name": "Vanuatu",
    "city_count": 7
  },
  {
    "country_name": "Cayman Islands",
    "city_count": 7
  },
  {
    "country_name": "Grenada",
    "city_count": 7
  },
  {
    "country_name": "Solomon Islands",
    "city_count": 7
  },
  {
    "country_name": "Nauru",
    "city_count": 7
  },
  {
    "country_name": "Barbados",
    "city_count": 7
  },
  {
    "country_name": "Bonaire, Sint Eustatius and Saba",
    "city_count": 8
  }, .......
```
