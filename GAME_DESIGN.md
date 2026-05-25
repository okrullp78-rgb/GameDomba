# GameDomba - Game Design (Ringkas)

## Ringkasan
GameDomba adalah permainan simulasi dan kompetisi "adu domba" tradisional berbasis APK. Pemain memilih domba muda, merawat (pakan), melatih, dan mengikutsertakan domba ke kompetisi. Menang memberikan reward: pakan, rumput, dan kredit point. Ada toko untuk membeli pakan bergizi dan aksesori kosmetik.

## Flow Utama
1. Pemilihan domba (usia: anak/remaja/dewasa)
2. Perawatan: beri pakan (regenerasi stamina & buff mood)
3. Latihan: tingkatkan atribut (kekuatan, kecepatan) dengan biaya stamina + waktu
4. Matchmaking/kompetisi: lawan AI/ pemain lain (mode asynchronous)
5. Reward: pakan, rumput (item), kredit point
6. Toko: beli pakan premium, aksesoris kosmetik, tiket turnamen

## Atribut Domba
- usia (months) -> menentukan readiness
- stamina (0-100)
- strength (0-100)
- speed (0-100)
- mood (0-100)
- level / experience

## Mekanika Inti
- Pakan: mengisi stamina dan memberi buff sementara (+10–+30 stamina tergantung jenis)
- Latihan: konsumsi stamina, beri XP dan peningkatan atribut kecil per sesi
- Match: skema probabilistik berbasis weighted sum (strength*0.6 + speed*0.4 + random)
- Cooldown & waktu: latihan dan recovery butuh waktu; pakan mempercepat

## Ekonomi & Reward (contoh angka awal)
- Mata uang: `Credit` (utama)
- Reward kemenangan: 10–50 Credit, 1–3 pakan biasa, 0–1 pakan premium (probabilitas)
- Pakan biasa (Shop): 1 Credit / unit
- Pakan premium (buff): 20 Credit / unit (memberi +25% XP atau +20 stamina)
- Rumput (cosmetic resource): item gratis dari event atau reward
- Harga aksesori kosmetik: 50–500 Credit
- Entry Ticket turnamen: 20 Credit (hadiah lebih besar)

## Monetisasi
- Ads: Banner di menu, interstitial antar match, Rewarded ads untuk pakan gratis atau cooldown skip
- IAP Consumable: paket pakan premium, paket credit (mis. 10k IDR untuk 1000 Credits)
- IAP Cosmetic: aksesori unik non-pay-to-win
- Subscription VIP: bonus harian, tanpa iklan, exp booster

## Kepatuhan & Risiko
- Hindari mekanik judi (no real-money betting)
- Sertakan privacy policy; gunakan konsent untuk tracking
- Jika target anak, patuhi aturan iklan untuk anak

## Teknologi & Integrasi
- Engine: Unity (direkomendasikan) atau Godot/Android native
- Ads: AdMob/Unity Ads
- IAP: Google Play Billing
- Backend: Firebase (auth, Firestore, Remote Config, Analytics)
- Leaderboards: Google Play Services

## Next Steps
- Prototipe ekonomi & balancing (simulasi) — sudah dibuat
- Mockup UI flow toko & match
- Implementasi MVP: single-player local -> add ads/IAP -> add online features

