
# 📦 Deskripsi Proyek: 3D Robot Visualization dengan Plotly

Proyek ini merupakan visualisasi robot 3D yang dibuat menggunakan **Plotly**, sebuah pustaka visualisasi interaktif berbasis JavaScript dan Python. Model robot dirancang dengan memanfaatkan bentuk dasar seperti **balok (cuboid)**, **silinder (cylinder)**, dan **bola (sphere)**.

Visualisasi ini dirancang agar dapat ditampilkan langsung di browser melalui file HTML yang telah diekspor dari kode Python. Dengan bantuan `plotly.graph_objects`, setiap bagian tubuh robot seperti kepala, badan, tangan, dan kaki dibangun secara modular dan kemudian dirakit menjadi satu kesatuan model 3D.

## Tujuan Proyek

- Menampilkan model robot 3D secara interaktif di browser.
- Melatih penggunaan geometri 3D sederhana dengan `Mesh3d` dan `Surface`.
- Mengekspor visualisasi dari Python ke HTML agar bisa dibuka tanpa membutuhkan Python interpreter.

## Fitur Utama

- 📦 **Bagian tubuh lengkap**: torso, kepala, mata, tangan, dan kaki.
- 🎨 **Warna berbeda** untuk tiap bagian agar mudah dibedakan.
- 🖱️ **Interaktif**: model dapat diputar, diperbesar, dan dipindahkan dengan mouse.
- 🌌 **Tampilan latar belakang gelap** untuk kesan futuristik.

## Tools & Teknologi

- Python + NumPy
- Plotly (`plotly.graph_objects`)
- HTML5 untuk visualisasi akhir

## Cara Menjalankan

1. Jalankan script Python untuk menghasilkan visualisasi robot.
2. Visualisasi akan tampil dalam jendela browser.
3. Simpan output menjadi file HTML menggunakan `fig.write_html("robot.html")` agar bisa dibuka kembali kapan saja.

## Contoh Output

Visualisasi akhir akan menampilkan robot berdiri tegak dengan dimensi dan proporsi yang realistis secara sederhana. Setiap bagian terlihat seperti model 3D, dengan sudut pandang bebas yang bisa diputar sesuai keinginan pengguna.

---

> Proyek ini cocok untuk pembelajaran dasar visualisasi 3D, pengenalan geometris sederhana dalam dunia pemrograman, atau sekadar eksperimen membuat model 3D dari kode.

