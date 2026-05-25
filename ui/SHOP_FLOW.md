# Shop Flow — GameDomba

Tujuan: sketsa UI & alur toko yang mudah dipahami, mendukung monetisasi via IAP dan rewarded ads.

1. Screen: Toko (default)
   - Menampilkan grid item: pakan, premium food, tiket, kosmetik
   - HUD: kredit, tombol VIP
   - Tombol "Detail" pada tiap item

2. Screen: Detail Item
   - Nama, deskripsi, efek (stamina/xp), harga
   - Tombol `Beli` (IAP/credit) dan `Tonton Iklan` (jika item tersedia via rewarded)
   - Tombol kembali

3. Purchase Flow
   - Jika kredit mencukupi: konfirmasi sederhana -> update credit + inventory
   - Jika tidak mencukupi: tawarkan paket credit (IAP) atau tonton rewarded ad untuk item gratis

4. Rewarded Ad Flow
   - Pemain memilih tombol tonton ad -> panggil SDK rewarded -> beri reward (basic food atau credit kecil)
   - Batasi frekuensi per jam/daily

5. VIP / Subscription
   - VIP membuka "no ads", bonus harian, discount di toko

6. Notes untuk implementasi
   - Integrasi: Google Play Billing untuk IAP; AdMob/Unity Ads untuk rewarded
   - Gunakan Remote Config untuk A/B testing harga dan drop rate
   - Analitik: track purchases, ad impressions, revenue per user

