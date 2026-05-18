# 🤖 Yapay Zeka Destekli Discord Sunucu Sihirbazı (Gemini API Entegrasyonlu)

[![Python](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![Discord.py](https://img.shields.io/badge/discord.py-2.x-brightgreen.svg)](https://discordpy.readthedocs.io/en/stable/)
[![Gemini API](https://img.shields.io/badge/Gemini_API-Google_AI-lightgray.svg)](https://ai.google.dev/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Türkçe Dil Desteği](https://img.shields.io/badge/Türkçe-Destekleniyor-blue)](https://tr.wikipedia.org/wiki/T%C3%BCrk%C3%A7e)

**Yapay zeka gücüyle dinamik Discord sunucuları oluşturun!** Bu Discord botu, Google'ın Gemini API'si ile entegre çalışarak, öncelikle sunucu konfigürasyonunu içeren bir JSON dosyası oluşturur ve ardından bu dosyayı kullanarak Discord sunucunuzu otomatik olarak kurar. Tamamen Türkçe dil desteğiyle!

## ✨ Özellikler

* **Gemini API Entegrasyonu:** Google'ın güçlü Gemini API'si ile dinamik sunucu konfigürasyonları oluşturur.
* **JSON Tabanlı Dinamik Konfigürasyon:** Gemini API tarafından oluşturulan JSON dosyası ile sunucu yapısını, kanalları, rolleri ve izinleri otomatik olarak belirler.
* **Kolay Sunucu Oluşturma:** Tek bir komutla ( `!üret` ) Gemini API'nin oluşturduğu yapılandırma ile sunucunuzu sıfırdan kurun.
* **Tamamen Özelleştirilebilir (AI Tarafından):** Sunucunuzun adı, açıklaması, kategorileri, metin ve ses kanalları, rolleri ve her bir rolün izinleri Gemini API tarafından akıllıca belirlenir.
* **Kanal ve Rol Silme:** Mevcut sunucudaki tüm kanalları ve `@everyone` dışındaki tüm rolleri silerek temiz bir başlangıç sağlar.
* **Detaylı Loglama:** Kullanılan komutları ve zaman damgalarını `command_log.txt` dosyasına kaydeder.
* **Hata Yönetimi:** Kanal ve rol oluşturma/silme sırasında oluşan yetki hatalarını ve diğer HTTP hatalarını yakalar ve bilgilendirici mesajlar yazdırır.
* **Gelişmiş İzin Yönetimi (AI Destekli):** Roller için geniş kapsamlı izin seçenekleri (sunucu yönetimi, üye atma/yasaklama, mesaj yönetimi, susturma/sağırlaştırma, mesaj gönderme/okuma, dosya ekleme, bağlanma, konuşma) Gemini API tarafından belirlenir.
* **Türkçe Dil Desteği:** Bot ve oluşturulan sunucu yapısı öncelikli olarak Türkçe dilini destekler.
* **Dil Özelleştirme İmkanı:** Kod içerisinde gerekli düzenlemeler yapılarak farklı dillerde sunucu oluşturma imkanı sunar.

## 🚀 Başlarken

Bu botu kendi Discord sunucunuzda kullanmaya başlamak için aşağıdaki adımları izleyin:

### ⚙️ Ön Gereksinimler

* **Python 3.6 veya üzeri:** Botun çalışması için gereklidir.
* **pip:** Python paket yöneticisi.
* **Discord Hesabı:** Bir Discord hesabınızın ve botunuz için bir uygulamanızın olması gerekir.
* **Bot Tokeni:** Discord Geliştirici Portalı'ndan alacağınız bot tokeni.
* **Sunucu ID'si:** Botun yapılandıracağı Discord sunucusunun ID'si.
* **Gemini API Anahtarı (Opsiyonel):** Eğer `aiprocess.py` dosyasında Gemini API'ye erişmek için bir anahtar gerekiyorsa, bu anahtarı edinmeniz gerekecektir. (Kodda doğrudan bir Gemini API anahtarı kullanımı görünmemektedir, ancak `aiprocess.py` dosyasının bu amaçla kullanıldığı belirtilmiştir.)

### 💾 Kurulum

1.  **Gerekli Kütüphaneleri Yükleyin:**

    ```bash
    pip install discord.py
    # Eğer Gemini API kütüphanesi gerekiyorsa onu da yükleyin.
    # Örneğin: pip install google-generativeai
    ```


2.  **`TOKENS.py` Dosyasını Yapılandırın:**

    `TOKENS.py` dosyasını oluşturun ve Discord bot tokeninizi ve sunucu ID'nizi aşağıdaki gibi ekleyin:

    ```python
    dctoken = "SİZİN_BOT_TOKENİNİZ"
    serverid = 123456789012345678  # Sunucu ID'niz
    ```

    **Önemli:** Bot tokeninizi ve sunucu ID'nizi doğru şekilde girdiğinizden emin olun. Bot tokeninizi kimseyle paylaşmayın!

3.  **`config/server_config_ai.json` Dosyası:**

    Bu dosya başlangıçta boş olabilir veya temel bir yapı içerebilir. `!üret` komutu ilk kez çalıştırıldığında, `aiprocess.py` dosyası ve Gemini API aracılığıyla bu dosya dinamik olarak oluşturulacaktır.

4.  **Botu Çalıştırın:**

    Ana Python dosyanızı (örneğin `main.py`) çalıştırın:

    ```bash
    python ana_dosya_adi.py
    ```

    Botunuz başarıyla giriş yaptığında konsolda `[Bot Adınız] Logged in!` şeklinde bir mesaj görmelisiniz.

## 🎮 Kullanım

Botunuz çalıştıktan sonra, yapılandırmak istediğiniz Discord sunucusunda aşağıdaki komutu kullanabilirsiniz:

!üret <sunucu oluşturma isteği>

`<sunucu oluşturma isteği>` kısmı, Gemini API'ye sunucunun teması veya amacı hakkında bilgi vermek için kullanılır. Örneğin:

!üret Oyun topluluğu
!üret Kitap severler için bir sunucu
!üret Python geliştiricileri buluşma noktası

Bot, bu komutu aldığında aşağıdaki işlemleri sırayla gerçekleştirecektir:

1.  Komutun kullanıldığını ve isteği loglar.
2.  `<sunucu oluşturma isteği>` verisini `aiprocess.py` dosyasındaki `generate_template` fonksiyonuna ileterek Gemini API'nin sunucu konfigürasyonunu içeren `config/server_config_ai.json` dosyasını oluşturmasını sağlar.
3.  Oluşturulan (veya güncellenen) `config/server_config_ai.json` dosyasını yükler.
4.  Belirtilen sunucudaki tüm kanalları siler.
5.  Belirtilen sunucudaki `@everyone` dışındaki tüm rolleri siler.
6.  Sunucu adını ve açıklamasını `server_config_ai.json` dosyasındaki verilere göre günceller.
7.  `server_config_ai.json` dosyasındaki kategori tanımlarına göre kategorileri oluşturur.
8.  Her kategori altındaki kanal tanımlarına göre metin ve ses kanallarını oluşturur ve izinlerini ayarlar.
9.  `server_config_ai.json` dosyasındaki rol tanımlarına göre rolleri oluşturur, renklerini ayarlar ve belirtilen izinleri verir.
10. İşlem tamamlandığında konsola ve komutu kullanan kişiye bilgilendirici mesajlar gönderir.

## 🌍 Türkçe Dil Desteği ve Diğer Diller

Bu bot, varsayılan olarak Türkçe dilinde sunucu yapılandırmaları oluşturacak şekilde tasarlanmıştır. `aiprocess.py` dosyası içerisinde Gemini API'ye gönderilen istemleri ve API'den alınan yanıtları işleyerek Türkçe kategori ve kanal isimleri, rol adları ve açıklamaları oluşturulması sağlanabilir.

Eğer botu farklı dillerde sunucu oluşturacak şekilde kullanmak isterseniz, `aiprocess.py` dosyasındaki Gemini API ile etkileşim kurulan kısımları düzenlemeniz gerekmektedir. API'ye gönderilen istemlerde ve işlenen yanıtlarda dil tercihini belirterek farklı dillerde sunucu oluşturabilirsiniz.

## 🛠️ Yapılandırma (Gelişmiş)

`config/server_config_ai.json` dosyası, Gemini API tarafından otomatik olarak oluşturulsa da, ihtiyaç duyarsanız bu dosyayı manuel olarak düzenleyebilirsiniz. Dosyanın yapısı önceki bölümde detaylı olarak açıklanmıştır. Ancak, bu dosyanın temel olarak Gemini API'nin çıktısı olduğunu unutmayın.

## 🤝 Katkıda Bulunma

Bu projeye katkıda bulunmak isterseniz, lütfen aşağıdaki adımları izleyin:

1.  Projeyi fork edin.
2.  Kendi branch'inizi oluşturun (`git checkout -b feature/harika-ozellik`).
3.  Değişikliklerinizi commit edin (`git commit -am 'Harika bir özellik eklendi'`).
4.  Branch'inizi push edin (`git push origin feature/harika-ozellik`).
5.  Pull request oluşturun.

## 📜 Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Daha fazla bilgi için [LICENSE](LICENSE) dosyasına göz atın.

## ❓ Destek

Herhangi bir sorunuz veya sorununuz olursa, lütfen GitHub üzerinden bir issue açın.

## 🙏 Teşekkür

Bu proje, yapay zeka ve Discord bot teknolojilerini bir araya getirerek sunucu yönetimini daha akıllı ve kolay hale getirmeyi amaçlamaktadır. Google'ın Gemini API'sine, Discord.py kütüphanesine ve bu projeyi destekleyen herkese teşekkür ederiz!
