from datetime import datetime, timedelta

def munkanapok_szama(kezdet, veg):
    munkanapok = 0
    nap = kezdet
    while nap.date() <= veg.date():
        if nap.weekday() < 5:  # hétfő=0, péntek=4
            munkanapok += 1
        nap += timedelta(days=1)
    return munkanapok

def main():
    # Cél dátum: 2025.12.31. 23:59:59
    cel = datetime(2025, 12, 31, 23, 59, 59)

    # Jelenlegi idő
    most = datetime.now()

    if most > cel:
        print("A megadott dátum már elmúlt.")
        return

    # Különbség kiszámítása
    kulonbseg = cel - most

    napok = kulonbseg.days
    orak = kulonbseg.seconds // 3600
    percek = (kulonbseg.seconds % 3600) // 60

    # Munkanapok száma
    munkanapok = munkanapok_szama(most, cel)

    print(f"Hátralévő napok száma: {napok}")
    print(f"Hátralévő idő: {napok} nap, {orak} óra, {percek} perc")
    print(f"Hátralévő munkanapok: {munkanapok}")

if __name__ == "__main__":
    main()
