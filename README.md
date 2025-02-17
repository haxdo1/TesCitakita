# Nomor 1

diminta untuk memproses sebuah kalimat dengan mengganti beberapa kata dalam kalimat tersebut menggunakan kata akar (root words) yang diberikan. Kata-kata dalam kalimat yang memiliki awalan yang cocok dengan salah satu kata akar harus diganti dengan kata akar tersebut, dengan prioritas pada kata akar yang terpendek. Jika tidak ada kata akar yang cocok, kata tersebut tetap seperti semula.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install foobar
```

## Usage

```python
import foobar

# returns 'words'
foobar.pluralize('word')

# returns 'geese'
foobar.pluralize('goose')

# returns 'phenomenon'
foobar.singularize('phenomena')
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
