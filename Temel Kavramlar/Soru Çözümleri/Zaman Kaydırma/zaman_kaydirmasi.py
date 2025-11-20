"""
x(t) ve x(t+4) sinyallerini ayrı çerçevelerde gösteren script.
x(t+4), x(t) sinyalinin 4 birim sola kaydırılmış halidir.
"""

import numpy as np
import matplotlib.pyplot as plt
import os


def x_t(t: np.ndarray) -> np.ndarray:
    """
    x(t) sinyalini tanımlar:
      t < -2        : 0
      -2 <= t < -1  : 0'dan 1'e lineer artış (slope = 1)
      -1 <= t < 0   : 1 seviyesinde sabit
      t = 0         : 1'den 2'ye sıçrama
      0 <= t < 1    : 2 seviyesinde sabit
      1 <= t <= 2   : 2'den 0'a lineer azalış (slope = -2)
      t > 2         : 0
    """
    x = np.zeros_like(t)
    
    # Segment 1: t = -2'den -1'e: 0'dan 1'e lineer artış
    mask1 = (-2 <= t) & (t < -1)
    x[mask1] = t[mask1] + 2  # t = -2'de 0, t = -1'de 1
    
    # Segment 2: t = -1'den 0'a: sabit 1
    mask2 = (-1 <= t) & (t < 0)
    x[mask2] = 1.0
    
    # Segment 3: t = 0'da: 2 (sıçrama noktası - sağdan limit)
    mask3 = (np.abs(t) < 1e-10)  # t ≈ 0 için yaklaşık kontrol
    x[mask3] = 2.0
    
    # Segment 4: t = 0'dan 1'e: sabit 2
    mask4 = (t > 0) & (t < 1)
    x[mask4] = 2.0
    
    # Segment 5: t = 1'den 2'ye: 2'den 0'a lineer azalış
    mask5 = (1 <= t) & (t <= 2)
    x[mask5] = 2.0 - 2.0 * (t[mask5] - 1)  # t = 1'de 2, t = 2'de 0
    
    return x


def plot_x_t_and_x_t_plus_4():
    """
    x(t) ve x(t+4) sinyallerini ayrı çerçevelerde (subplot) çizer.
    """
    # Zaman aralığını belirle
    t_original = np.linspace(-3, 3, 2000)  # x(t) için
    t_shifted = np.linspace(-7, -1, 2000)  # x(t+4) için
    
    # x(t) sinyalini hesapla
    x_original = x_t(t_original)
    
    # x(t+4) sinyalini hesapla (4 birim sola kaydırma)
    x_shifted = x_t(t_shifted + 4)
    
    # İki ayrı subplot oluştur
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
    
    # ========== ÜST ÇERÇEVE: x(t) ==========
    ax1.plot(t_original, x_original, label=r'$x(t)$', color='blue', linewidth=2.5)
    ax1.set_title(r'$x(t)$ Sinyali', fontsize=14, fontweight='bold')
    ax1.set_xlabel('Zaman (t)', fontsize=12)
    ax1.set_ylabel('Genlik', fontsize=12)
    ax1.grid(True, linestyle='--', alpha=0.6, linewidth=0.8)
    ax1.axhline(0, color='black', linewidth=1)
    ax1.axvline(0, color='black', linewidth=1)
    ax1.legend(fontsize=11, loc='upper right')
    ax1.set_xlim(-3, 3)
    ax1.set_ylim(-0.5, 2.5)
    
    # x(t) için önemli noktaları işaretle
    ax1.plot(-2, 0, 'bo', markersize=8)
    ax1.plot(-1, 1, 'bo', markersize=8)
    ax1.plot(0, 1, 'bo', markersize=8)
    ax1.plot(0, 2, 'bo', markersize=8)
    ax1.plot(1, 2, 'bo', markersize=8)
    ax1.plot(2, 0, 'bo', markersize=8)
    
    # ========== ALT ÇERÇEVE: x(t+4) ==========
    ax2.plot(t_shifted, x_shifted, label=r'$x(t+4)$', color='red', linewidth=2.5)
    ax2.set_title(r'$x(t+4)$ Sinyali (4 birim sola kaydırılmış)', fontsize=14, fontweight='bold')
    ax2.set_xlabel('Zaman (t)', fontsize=12)
    ax2.set_ylabel('Genlik', fontsize=12)
    ax2.grid(True, linestyle='--', alpha=0.6, linewidth=0.8)
    ax2.axhline(0, color='black', linewidth=1)
    ax2.axvline(0, color='black', linewidth=1)
    ax2.legend(fontsize=11, loc='upper right')
    ax2.set_xlim(-7, -1)
    ax2.set_ylim(-0.5, 2.5)
    
    # x(t+4) için önemli noktaları işaretle
    ax2.plot(-6, 0, 'ro', markersize=8)
    ax2.plot(-5, 1, 'ro', markersize=8)
    ax2.plot(-4, 1, 'ro', markersize=8)
    ax2.plot(-4, 2, 'ro', markersize=8)
    ax2.plot(-3, 2, 'ro', markersize=8)
    ax2.plot(-2, 0, 'ro', markersize=8)
    
    # Genel başlık
    fig.suptitle('x(t) ve x(t+4) Sinyalleri', fontsize=16, fontweight='bold', y=0.995)
    
    plt.tight_layout()
    
    # PNG olarak kaydet (dosya adıyla aynı isimde)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    png_filename = os.path.join(script_dir, 'zaman_kaydirmasi.png')
    plt.savefig(png_filename, dpi=300, bbox_inches='tight')
    print(f"Grafik kaydedildi: {png_filename}")
    
    plt.show()


if __name__ == "__main__":
    plot_x_t_and_x_t_plus_4()

