import time

print("Yamyamlar ve Misyonerler!")
print("3 adet Yamyam ve 3 adet Misyoner var amacımız nehrin sol tarafında olan herkesi yamyamlara yem etmeden sağ tarafa geçirmek bir adet sandalımız var ve bu sandal maksimum 2 kişi alabilir.bir taraftaki yamyam sayısı misyoner sayısından fazla olursa oyun biter!")

time.sleep(10)
#listenin sol tarafı misyonerleri sağ tarafı yamyamları temsil eder!
#Kullanıcı Mye basarsa 

#Listeler

#Başlangıç
nehrinSolu=[3,3]
nehrinSagi=[0,0]
sandal=[0,0]


def oyun():
    while True:
       
        print("Nehrin sol tarafı:", nehrinSolu)
        print("Nehrin sağ tarafı:", nehrinSagi)
       
       
       
        if nehrinSagi[0] != 0 and nehrinSolu[0] != 0 :
            if nehrinSolu[1] > nehrinSolu[0] or nehrinSagi[1] > nehrinSagi[0]:
                print("Yamyamlar misyonerleri yedi!")
                break

        

        taraf = int(input(" Sandalı nehrin sol tarafına göndermek için 1'e sağ tarafına göndermek için için 2'ye bas:"))
        cevap = input("M veya Y giriniz: ")
        if cevap == "m" and taraf == 1 :
            nehrinSolu[0] += 1
            nehrinSagi[0] -= 1
           
        
        elif cevap == "y" and taraf == 1:
            nehrinSolu[1] += 1
            nehrinSagi[1] -= 1


        if cevap == "m" and taraf == 2 :
            nehrinSolu[0] -= 1
            nehrinSagi[0] += 1
           
        
        elif cevap == "y" and taraf == 2:
            nehrinSolu[1] -= 1
            nehrinSagi[1] += 1

        
        cevap1 = input("M veya Y giriniz: ")
        
        if cevap1 == "m" and taraf == 1 :
            nehrinSolu[0] += 1
            nehrinSagi[0] -= 1
           
        
        elif cevap1 == "y" and taraf == 1:
            nehrinSolu[1] += 1
            nehrinSagi[1] -= 1


        if cevap1 == "m" and taraf == 2 :
            nehrinSolu[0] -= 1
            nehrinSagi[0] += 1
           
        
        elif cevap1 == "y" and taraf == 2:
            nehrinSolu[1] -= 1
            nehrinSagi[1] += 1


        
        

if __name__ == "__main__":
    oyun()
    



