# Hosting Prototype GameDomba

Cara cepat menjalankan prototype lokal (Linux/macOS):

1. Pastikan Python 3 terinstall.
2. Jalankan script:

```bash
./run_server.sh
```

3. Buka browser ke `http://localhost:8000` dan pilih halaman prototype.

Catatan:
- Untuk deployment cepat ke publik, gunakan GitHub Pages (push folder `ui` ke gh-pages branch) atau layanan static host seperti Netlify / Vercel.
- Jika menggunakan GitHub Pages, pindahkan isi `ui` ke root branch `gh-pages` atau atur publikasi folder.

## Auto-deploy via GitHub Actions

Anda dapat mengaktifkan deployment otomatis untuk folder `ui/` ke branch `gh-pages` menggunakan workflow GitHub Actions yang sudah disertakan.

Langkah singkat:

1. Push repository ini ke GitHub (pastikan `main` adalah branch utama).
2. Workflow akan berjalan setiap kali ada push ke `main` dan menerbitkan isi `ui/` ke branch `gh-pages`.
3. Setelah workflow berjalan sukses, buka Settings -> Pages pada repo dan pilih `gh-pages` sebagai source.
4. Situs akan tersedia di `https://<username>.github.io/<repo-name>/`.

Catatan: workflow menggunakan `GITHUB_TOKEN` bawaan, sehingga tidak memerlukan secret tambahan.
