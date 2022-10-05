from PIL import Image  # Python Imaging Library
import numpy as np

inicjaly = Image.open("inicjaly.bmp")

print("tryb:", inicjaly.mode)
print("format:", inicjaly.format)
print("rozmiar:", inicjaly.size)

dane_inicjaly = np.asarray(inicjaly)
dane_inicjaly = dane_inicjaly * 1

np.savetxt("inicjaly.txt", dane_inicjaly)

inicjaly_info = np.loadtxt("inicjaly.txt", dtype=np.int_, converters=float)

print("***************************************")
print("typ danych tablicy inicjaly_info:", inicjaly_info.dtype)  # 
print("rozmiar tablicy inicjaly_info :", inicjaly_info.shape) 
print("elementow w tablicy inicjaly_info jest:", inicjaly_info.size)
print("wymiar tablicy inicjaly_info :", inicjaly_info.ndim)


print("(50,30) wartosc:", inicjaly_info[30][50])
print("(90,40) wartosc:", inicjaly_info[40][90])
print("(99,0) wartosc:", inicjaly_info[0][99])
