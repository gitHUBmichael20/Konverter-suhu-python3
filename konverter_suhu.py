import math

print("PROGRAM KONVERTER SUHU")
print("1. Kelvin")
print("2. Fahrenheit")
print("3. Reamur")
print("4. Celcius")

while True:
    pilih = input("Pilih satuan (1/2/3/4): ")
       
    if pilih in '1':
        print("Mengubah kelvin ke suhu lainnya")
        suhu_kelvin = float(input("Masukkan suhu (dalam kelvin) : "))
        
        print("hasil fahrenheit : ", ((1.8 * (suhu_kelvin - 273 )) + 32))
        print("Hasil reamur : ", (4/5 * (suhu_kelvin + 273)))
        print("Hasil celcius : ", (suhu_kelvin + 273))
    
    elif pilih in '2':
        print("Mengubah fahrenheit ke suhu lainnya")
        suhu_fahrenheit = float(input("Masukkan suhu (dalam fahrenheit) : "))
        
        print("hasil celcius : ", (5/9 * (suhu_fahrenheit - 32)))
        print("Hasil reamur : ", (4/9 * (suhu_fahrenheit - 32)))
    
    elif pilih in '3':
        print("Mengubah reamur ke suhu lainnya")
        suhu_reamur = float(input("Masukkan suhu (dalam reamur) : "))
        
        print("hasil celcius : ",(5/4 * suhu_reamur))
        print("Hasil Kelvin : ", (5/4 * (suhu_reamur + 273)))
        print("Hasil Fahrenheit : ", (9/4 * (suhu_reamur + 32)))
       
    elif pilih in '4':
        suhu_celcius = float(input("Masukkan suhu (dalam celcius) : "))

        print("Hasil fahrenheit : ", (9/5 * (suhu_celcius + 32)))
        print("Hasil kelvin : ", (suhu_celcius + 273))
        print("Hasil reamur : ", (4/5 * suhu_celcius))
        
    next_kalkulasi = input("Ulangi konversi ( Y / N ) : ")
    if next_kalkulasi == "N":
        break
    
else : 
    print("Invalid")
      
    
    