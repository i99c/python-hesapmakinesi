s1 = int(input("Birinci sayıyı girin: "))
islem = input("İşlemi girin (+, -, *, /): ")
s2 = int(input("İkinci sayıyı girin: "))

if islem == "+":
    sonuc = s1 + s2
elif islem == "-":
    sonuc = s1 - s2
elif islem == "*":
    sonuc = s1 * s2
elif islem == "/":
    sonuc = s1 / s2
else:
    print("Yanlış işlem girdiniz")

print(f"{s1} {islem} {s2} = {sonuc}")
