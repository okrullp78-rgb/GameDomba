# Integrasi AdMob & Google Play Billing di Unity (Ringkas)

Panduan singkat untuk menyiapkan AdMob (rewarded/banners) dan Google Play Billing di Unity.

## Prasyarat
- Unity 2020.3 LTS atau lebih baru (disarankan 2021/2022+ untuk plugin terbaru)
- Android Build Support terinstall
- Akun Google Play Console aktif

## AdMob (Unity)
1. Daftar ke AdMob dan buat App + Ad Units (Banner, Interstitial, Rewarded).
2. Di Unity, buka Package Manager -> Add package from git URL -> `https://github.com/googleads/googleads-mobile-unity` (atau download SDK dari repo resmi).
3. Import Unity package SDK AdMob.
4. Configure Android manifest: SDK akan menambahkan dependensi Gradle; periksa `Assets/Plugins/Android`.
5. Implementasi rewarded ad flow:
   - Init SDK: `MobileAds.Initialize(initStatus => { ... });`
   - Load rewarded: `RewardedAd.CreateAdRequest()` dan handler untuk `OnUserEarnedReward` untuk memberikan pakan/credit.
6. Test dengan test ad unit IDs sebelum publish.

## Google Play Billing (IAP)
1. Tambahkan `com.android.billingclient:billing` gradle dependency via Play Billing Library (plugin Unity IAP recommended).
2. Di Unity, import Unity IAP via Services > In-App Purchasing atau Package Manager (`com.unity.purchasing`).
3. Setup produk di Google Play Console (consumable untuk pakan, non-consumable untuk kosmetik, subscription untuk VIP).
4. Implement purchase flow menggunakan Unity IAP sample and callbacks; verifikasi receipt server-side bila perlu.

## Best Practices
- Gunakan remote config (Firebase Remote Config) untuk tuning harga dan drop rate tanpa update APK.
- Gunakan Firebase Analytics untuk memantau events: `purchase`, `ad_impression`, `ad_reward`, `tutorial_complete`.
- Test on-device selalu sebelum publish; gunakan internal testing track di Google Play Console.
- Pastikan Privacy Policy + user consent (GDPR) saat menargetkan EEA.

## Resources
- AdMob Unity plugin: https://github.com/googleads/googleads-mobile-unity
- Unity IAP docs: https://docs.unity3d.com/Manual/UnityIAP.html
- Google Play Billing docs: https://developer.android.com/google/play/billing

