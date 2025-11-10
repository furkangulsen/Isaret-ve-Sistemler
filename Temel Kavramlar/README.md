# 📘 İŞARET VE SİSTEMLER  
> "Sinyalleri anlamak, sistemleri kontrol etmenin ilk adımıdır."  

Bu doküman, **İşaret ve Sistemler** dersinin temel konularını **kısa, öz ve akılda kalıcı** biçimde açıklar.  
Her bölüm, konunun mantığını kavramanı ve sınavlarda hızlı hatırlamanı kolaylaştıracak şekilde tasarlanmıştır.  

---

## 🔹 1. İşaret (Sinyal) Temelleri  

### 🔸 Tanım  
Bir **işaret (sinyal)**; zaman, uzay veya başka bağımsız değişkenlere göre değişen **fiziksel niceliktir.**  
Matematiksel olarak bir fonksiyon şeklindedir:  

![formula](https://latex.codecogs.com/svg.image?x(t)\text{%20veya%20}x(n))

- Matematiksel fonksiyon olmasının yanı sıra **gerçek sistemlerde ölçülebilen büyüklük** olarak değerlendirilir.

---

### 🔸 Boyut Kavramı  
| Sinyal Türü | Bağımsız Değişken(ler) | Boyut | Örnek |
|--------------|------------------------|--------|--------|
| Konuşma Sinyali | Zaman (t) | 1D | Mikrofonla ölçülen ses dalgası |
| Görüntü Sinyali | Uzay (x, y) | 2D | Gri seviye resim |
| Video | Uzay (x, y) + Zaman (t) | 3D | Renkli hareketli görüntü |

💡 **Trick:** Boyut = Bağımsız değişken sayısı  

#### Örnekler:
- **Konuşma** → zamana bağlı, 1 boyutlu  
- **Görüntü** → x-y koordinatlı, 2 boyutlu  
- **Renkli video** → x-y-z (zaman) koordinatlı, 3 boyutlu  

---

### 🔸 Bağımsız ve Bağımlı Değişkenler

#### Bağımsız Değişken (Independent Variable)
- Sinyalin değiştiği değişken: **zaman (t)** veya **uzay (x, y)**.  
- Sinyalin boyutunu belirler:  
  - Konuşma sinyali → 1 boyut (zaman)  
  - Görüntü sinyali → 2 boyut (x, y)  

#### Bağımlı Değişken (Dependent Variable)
- Bağımsız değişkene bağlı olarak değişen **sinyal genliği**.  
- Örnek: Konuşma sinyalinde ses şiddeti, zamana bağlı olarak değişir.  

---

### 🔸 Frekans (Frequency)
- Sinyalin bileşenlerinin tekrar hızını gösterir.  
- Periyodik sinyallerde temel frekans:
  
  ![formula](https://latex.codecogs.com/svg.image?f_0=\frac{1}{T_0})  
  **f₀**: Temel frekans (Hz - Hertz cinsinden)
  
  ![formula](https://latex.codecogs.com/svg.image?\omega_0=\frac{2\pi}{T_0})  
  **ω₀**: Açısal frekans (rad/s - radyan/saniye cinsinden)
  
- Fourier serisi ile sinyal, frekans bileşenlerine ayrılabilir.

---

### 🔸 Faz (Phase)
- Sinyalin frekans bileşenlerinin zaman eksenindeki **başlangıç konumu**.  
- Fourier spektrumunda genlik ve faz birlikte değerlendirilir.  
- Örnek: Aynı frekansta iki sinyal, farklı fazlarda başlayabilir; bu, senkronizasyon farkını gösterir.  

---

### 🎵 Analoji: Sinyal = Melodi
| Kavram                 | Melodi Analojisi                            |
|------------------------|--------------------------------------------|
| Bağımsız Değişken      | Melodiyi dinlediğin süre                    |
| Bağımlı Değişken       | Nota şiddeti (yükseklik)                   |
| Frekans                | Hangi nota çalıyor (tını, perde)          |
| Faz                    | Notanın melodide ne zaman başladığı        |

---

### 🔸 Enerji ve Güç Sınıflandırması  
| Tür | Tanım | Özellik | Örnek |
|-----|--------|----------|--------|
| **Enerji Sinyali** | Enerjisi sonlu, gücü sıfır | ![formula](https://latex.codecogs.com/svg.image?0<E<\infty,\quad%20P=0) | Düşen darbeler |
| **Güç Sinyali** | Gücü sonlu, enerjisi sonsuz | ![formula](https://latex.codecogs.com/svg.image?E=\infty,\quad%200<P<\infty) | Periyodik sinyaller |
| **Diğer** | Ne enerji ne güç sinyali | – | ![formula](https://latex.codecogs.com/svg.image?x(t)=t) |

📌 **Trick:** Enerji sinyalleri *bitip tükenir*, güç sinyalleri *sürekli devam eder.*  

---

### 🔸 Temel İşaretler
- **Birim Basamak (u(t))** → Sinyalin başlangıcını temsil eder.  
- **Birim Dürtü (δ(t))** → Bir sistemin karakteristiğini belirlemek için kullanılır (dürtü yanıtı).  
- **Rampa (r(t))**, **sinüs**, **üstel** gibi fonksiyonlar analizde sıkça kullanılır.  

---

## 🔹 2. Sistem Temelleri  

### 🔸 Tanım  
Bir **sistem**, bir girdi işaretini alıp bir **çıktı işaretine dönüştüren fiziksel veya matematiksel yapı**dır.  

![formula](https://latex.codecogs.com/svg.image?y(t)=T\{x(t)\})

---

### 🔸 Sistem İle İlişkisi
- Sinyaller **sistemler üzerinden üretilir ve işlenir**.  
- Örnekler:  
  - **Ses telleri** → konuşma sinyali  
  - **Fotoğraf filmi** → görüntü sinyali  
  - **Mikrofon** → ses sinyalini elektrik sinyaline dönüştürür  
  - **Hoparlör** → elektrik sinyalini tekrar sese dönüştürür  
- Sistem, sinyale işlem uygulayabilir (filtreleme, modülasyon vb.)  

---

### 🔸 Sistem Sınıflandırmaları  
| Özellik | Tür | Açıklama |
|----------|-----|-----------|
| **Doğrusal / Doğrusal Olmayan** | ![formula](https://latex.codecogs.com/svg.image?T(a_1x_1+a_2x_2)=a_1T(x_1)+a_2T(x_2)) | Doğrusal sistemler süperpozisyon ilkesine uyar |
| **Zamanla Değişmeyen / Değişen** | ![formula](https://latex.codecogs.com/svg.image?T\{x(t-t_0)\}=y(t-t_0)) | Girdi ötelenince, çıktı da aynı miktarda öteleniyorsa zamanla değişmeyen |
| **Nedensel / Nedensel Olmayan** | Çıktı yalnızca geçmiş ve şimdiki girdilere bağlıysa nedensel | Gerçek sistemler nedenseldir |
| **Kararlı / Kararsız** | Girdi sınırlıysa çıktı da sınırlıysa kararlı | **BIBO Kararlılığı** koşulu |

---

### 🔸 Dürtü Yanıtı (h(t))
- Bir sistemin karakteristiğini **tam olarak tanımlar.**  
- Herhangi bir girdi ![formula](https://latex.codecogs.com/svg.image?x(t)), **konvolüsyon** ile sistemden geçer:  

![formula](https://latex.codecogs.com/svg.image?y(t)=x(t)*h(t))

- Bu ifade, **Lineer Zamanla Değişmeyen (LTI)** sistemlerin temelidir.  

---

## 🔹 3. Dirac Delta (Dürtü) Fonksiyonu  

### 🔸 Tanım  
**Dirac delta** fonksiyonu, sıfır dışında her yerde **0**, sıfırda ise **sonsuz** değer alır.  
Ancak bu sonsuz değer öyle ayarlanmıştır ki **alanı (integrali)** **1**'e eşittir:  

![formula](https://latex.codecogs.com/svg.image?\delta(t)=\begin{cases}0,&t\neq%200\\\infty,&t=0\end{cases}\quad\text{ve}\quad\int_{-\infty}^{\infty}\delta(t)dt=1)

💡 **Trick:** δ(t) = "sonsuz küçük zamanda 1 birimlik enerji."  

---

### 🔸 Temel Özellikler  

| Özellik | Matematiksel Gösterim | Açıklama |
|----------|------------------------|-----------|
| **Örnekleme Özelliği** | ![formula](https://latex.codecogs.com/svg.image?\int_{-\infty}^{\infty}x(t)\delta(t-t_0)dt=x(t_0)) | δ(t), x(t)'yi t₀ noktasında örnekler |
| **Kaydırma (Öteleme)** | ![formula](https://latex.codecogs.com/svg.image?\delta(t-t_0)) | δ sinyali t₀ anına taşınır |
| **Türev Özelliği** | ![formula](https://latex.codecogs.com/svg.image?\frac{d}{dt}u(t)=\delta(t)) | Birim basamak fonksiyonunun türevi δ(t)'dir |
| **Çarpanlı Delta** | ![formula](https://latex.codecogs.com/svg.image?\delta(at)=\frac{1}{\lvert%20a\rvert}\delta(t)) | Ölçekleme yapılırken genlik değişir |

---

### 🔸 Birim Basamak ile İlişkisi  
- **Birim basamak (u(t))**, δ(t)'nin **integralidir**:  
  
  ![formula](https://latex.codecogs.com/svg.image?u(t)=\int_{-\infty}^{t}\delta(\tau)d\tau)
  
- **δ(t)** ise u(t)'nin **türevidir**:  
  
  ![formula](https://latex.codecogs.com/svg.image?\frac{du(t)}{dt}=\delta(t))

📌 **Trick:**  
"**δ(t)** → anlık tepki,  
**u(t)** → birikimli tepki."  

---

### 🔸 Fiziksel Yorum  
Dirac delta, bir sisteme **anlık enerji darbesi** verir.  
Sistemin bu darbeye verdiği yanıt = **dürtü yanıtı (h(t))** olur.  
Bu yanıt, sistemin **tüm davranışını temsil eder.**

---

### 🔸 Zaman ve Frekans Düzleminde Görünümü  

| Alan | Gösterim | Özellik |
|------|------------|----------|
| **Zaman Düzlemi** | ![formula](https://latex.codecogs.com/svg.image?\delta(t)) | t=0 noktasında anlık tepki |
| **Frekans Düzlemi** | ![formula](https://latex.codecogs.com/svg.image?\delta(t)\leftrightarrow%201) | Tüm frekanslarda eşit genlik (sonsuz bant genişliği) |

💡 **Trick:**  
δ(t) → zaman alanında *noktadır*,  
ama frekansta *her şeydir!*  

---

### 🔸 Uygulama: Konvolüsyon Basitleştirmesi  
Bir sinyalin δ(t) ile konvolüsyonu, sinyalin kendisini verir:  

![formula](https://latex.codecogs.com/svg.image?x(t)*\delta(t)=x(t))

Bu nedenle δ(t), konvolüsyonda **"birim eleman"** gibi davranır.

---

### 🔸 Ayrık-Zaman (Discrete-Time) Dirac  
Sürekli zamanda δ(t)'nin ayrık karşılığı:  

![formula](https://latex.codecogs.com/svg.image?\delta[n]=\begin{cases}1,&n=0\\0,&n\neq%200\end{cases}\quad\text{ve}\quad\sum_{n=-\infty}^{\infty}\delta[n]=1)

📌 **Trick:** δ[n] → dizinin "başlangıç noktasını" temsil eder.  

---

## 🔹 4. Zaman Düzlemi İşlemleri  

| İşlem | Matematiksel Tanım | Açıklama |
|--------|--------------------|-----------|
| **Zamanda Öteleme** | ![formula](https://latex.codecogs.com/svg.image?x(t-t_0)) | Sinyalin sağa veya sola kaydırılması |
| **Zamanda Ters Çevirme** | ![formula](https://latex.codecogs.com/svg.image?x(-t)) | Sinyalin aynalanması |
| **Zamanda Ölçekleme** | ![formula](https://latex.codecogs.com/svg.image?x(at)) | Zamanın sıkıştırılması veya genişletilmesi |

💡 **Trick:**  
- a > 1 → zaman sıkışır (frekans artar)  
- 0 < a < 1 → zaman genişler (frekans azalır)  

---

## 🔹 5. Frekans Düzlemi Analizi (Fourier)

### 🔸 Fourier Serileri (FS)
- **Periyodik sinyalleri** temel sinüs ve kosinüs bileşenlerine ayırır.  
- Her periyodik sinyal → sonsuz sayıda harmonik içerir.  

![formula](https://latex.codecogs.com/svg.image?x(t)=\sum_{k=-\infty}^{\infty}a_ke^{jk\omega_0t})

#### Özellikler:
- Doğrusallık  
- Zamanda Öteleme  
- Zaman Ölçekleme  
- **Parseval Teoremi:** Enerji = Frekans bileşenleri toplamı  

💡 **Trick:** Fourier serisi = "sinyali notalara ayırmak" gibidir.  

---

### 🔸 Sürekli-Zaman Fourier Dönüşümü (SZFD)
- **Aperiyodik sinyalleri** analiz etmek için kullanılır.  

![formula](https://latex.codecogs.com/svg.image?X(j\omega)=\int_{-\infty}^{\infty}x(t)e^{-j\omega%20t}dt)

#### Temel Özellikler:
- **Konvolüsyon Teoremi:**  
  
  ![formula](https://latex.codecogs.com/svg.image?x(t)*h(t)\leftrightarrow%20X(j\omega)\cdot%20H(j\omega))
  
- **Zaman/Frekans Öteleme**  
- **İkilik (Duality)**  
- **Dirichlet Koşulları:** Fourier dönüşümünün var olması için sağlanmalıdır.  

---

## 🔹 6. Kompleks Frekans Düzlemi Analizi (Laplace)

### 🔸 Tanım
- Fourier dönüşümünün **genelleştirilmiş hâlidir.**  

![formula](https://latex.codecogs.com/svg.image?X(s)=\int_{-\infty}^{\infty}x(t)e^{-st}dt)

**s = σ + jω** (kompleks frekans)

---

### 🔸 Yakınsaklık Bölgesi (ROC)
- Dönüşümün var olabilmesi için **integralin yakınsadığı bölge.**  
- ROC, sistemin **nedensellik** ve **kararlılık** özelliklerini belirler.

---

### 🔸 Kutup ve Sıfırlar
- **Kutup (Pole):** Paydanın kökü → sistem kararlılığıyla ilişkilidir.  
- **Sıfır (Zero):** Payın kökü → frekans cevabını şekillendirir.  

💡 **Trick:** Kutup sol yarı düzlemdeyse sistem **kararlıdır.**

---

### 🔸 Dönüşüm Özellikleri
- Lineerlik  
- Zamanda Öteleme  
- Türev/İntegral ilişkileri  
- Konvolüsyon  

---

### 🔸 LTI Sistemlerde Kullanımı
- Laplace, sistem analizi için **evrensel bir araçtır.**  
- **Transfer fonksiyonu:**  

![formula](https://latex.codecogs.com/svg.image?H(s)=\frac{Y(s)}{X(s)})

Bu ifade, sistemin tüm dinamik davranışını özetler.  

---

## 🧠 Özet Tablo

| Konu | Alan | Temel Araç | Ana Amaç |
|-------|------|-------------|-----------|
| Zaman Düzlemi | t | Konvolüsyon | Sinyalin sistemden geçişini bulmak |
| Frekans Düzlemi | ω | Fourier | Frekans bileşenlerini analiz etmek |
| Kompleks Frekans | s = σ + jω | Laplace | Kararlılık ve nedenselliği incelemek |

---

## 💬 Son Söz  
> "Bir sistemi anlamak istiyorsan, önce onun sinyaliyle konuşmayı öğrenmelisin."  

Bu bölüm, **İşaret ve Sistemler** dersindeki temel kavramları hızlıca özetlemek ve hangi konuların öğrenileceğini göstermek amacıyla hazırlanmıştır.