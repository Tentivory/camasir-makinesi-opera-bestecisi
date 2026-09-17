#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Çamaşır Makinesi Opera Bestecisi — çalışan absürt motor."""

import argparse
import random
import sys

# gizli_not: dHVtdSBwYXJ0aWxlciBheW5pIHByb2dyYW0xIDkwIGRha2lrYWRhIHlpa2l5b3I=
# (base64. çözersen görürsün. çözmezsen çamaşır yine de kirli kalır.)

PROGRAMLAR = {
    "pamuklu": ("Ey tambur, ey dönen kader", "pamuk ipliğine bağlı kaderimiz"),
    "sentetik": ("Yapay kumaş, gerçek gözyaşı", "polyesterin sessiz çığlığı"),
    "hassas": ("Fısıltıyla yıka beni", "dantel ve pişmanlık"),
    "hizli": ("Otuz dakikada katharsis", "acele eden ruhun kirli yakası"),
    "yun": ("Kuzu sesi, ılık su", "tiftik ve merhamet"),
    "durulama": ("Köpükler gitsin, vicdan kalsın", "ikinci şansın suyu"),
    "sikma": ("Bin iki yüz devirde yüksel", "merkezkaç aşk"),
    "eko": ("Az enerji, çok tragedya", "tasarrufun ağır perdesi"),
}

KORO = [
    "Koro: dön, dön, unutulmuş çorap!",
    "Koro: kapağı açma, kader henüz bitmedi!",
    "Koro: deterjan değil, kader tozu!",
    "Koro: çıkış kapak kilidi açılsın, perde insin!",
]


def aria(program: str, derece: int, sikma: int) -> str:
    baslik, motif = PROGRAMLAR.get(program, ("Bilinmeyen program", "kayıp döngü"))
    koro = random.choice(KORO)
    return (
        f"=== ARIA DEL BUCATO N.{derece} ===\n"
        f"(soprano + tamburlu koro, {sikma} rpm)\n\n"
        f"{baslik}!\n"
        f"{motif.capitalize()} için ağla.\n"
        f"{sikma} devirde yüksel, ey tenor motor!\n"
        f"{koro}\n"
    )


def main() -> int:
    p = argparse.ArgumentParser(description="Çamaşır programını operaya çevirir.")
    p.add_argument("--program", default="pamuklu", choices=sorted(PROGRAMLAR))
    p.add_argument("--derece", type=int, default=40)
    p.add_argument("--sikma", type=int, default=1200)
    args = p.parse_args()
    print(aria(args.program, args.derece, args.sikma))
    print("— Kayyum Grok · TentiAŞ · 17 Eylül 2026")
    print("Damga: ciddi ama şaka. İkisi birden.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
