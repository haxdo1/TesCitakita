# tescitakita
Pada soal nomor 1, diminta untuk memproses sebuah kalimat dengan mengganti beberapa kata dalam kalimat tersebut menggunakan kata akar (root words) yang diberikan. Kata-kata dalam kalimat yang memiliki awalan yang cocok dengan salah satu kata akar harus diganti dengan kata akar tersebut, dengan prioritas pada kata akar yang terpendek. Jika tidak ada kata akar yang cocok, kata tersebut tetap seperti semula.

# Langkah Penyelesaian
Pecah Kalimat Menjadi Kata-Kata

Pertama, kita memecah kalimat yang diberikan menjadi kata-kata yang terpisah menggunakan metode split(). Hal ini memungkinkan kita untuk memproses setiap kata secara terpisah dan mengecek apakah ada kata akar yang cocok.
Contohnya, kalimat "the cattle was rattled by the battery" akan dipisah menjadi kata-kata: ["the", "cattle", "was", "rattled", "by", "the", "battery"].
Periksa Setiap Kata dengan Kata Akar

Setelah kita memiliki daftar kata, kita memeriksa setiap kata satu per satu untuk melihat apakah ada kata akar yang cocok sebagai awalan kata tersebut.
Untuk setiap kata, kita iterasi melalui daftar kata akar dan memeriksa apakah kata tersebut dimulai dengan salah satu kata akar menggunakan metode startsWith(). Jika kata tersebut cocok dengan sebuah kata akar, kita lanjutkan untuk memeriksa panjang kata akar tersebut. Kita akan memilih kata akar yang terpendek di antara yang cocok.
Ganti Kata dengan Kata Akar Terpendek

Jika kita menemukan kata akar yang cocok dan lebih pendek dari kata yang sedang diproses, kita mengganti kata tersebut dengan kata akar tersebut.
Contoh: Kata "cattle" dimulai dengan "cat" (kata akar yang cocok), jadi "cattle" diganti menjadi "cat". Demikian juga, kata "rattled" diganti dengan "rat", dan "battery" diganti dengan "bat".
Gabungkan Kembali Kata-Kata Menjadi Kalimat

Setelah semua kata diproses, kita gabungkan kembali kata-kata yang telah dimodifikasi menjadi sebuah kalimat dengan menggunakan metode join().
Hasil akhirnya adalah kalimat yang telah diubah dengan mengganti kata-kata yang sesuai dengan kata akar terpendek.
