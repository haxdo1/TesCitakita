# Nomor 1

diminta untuk memproses sebuah kalimat dengan mengganti beberapa kata dalam kalimat tersebut menggunakan kata akar (root words) yang diberikan. Kata-kata dalam kalimat yang memiliki awalan yang cocok dengan salah satu kata akar harus diganti dengan kata akar tersebut, dengan prioritas pada kata akar yang terpendek. Jika tidak ada kata akar yang cocok, kata tersebut tetap seperti semula.

## Usage

```python
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

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
