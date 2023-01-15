import random
kazanmasayisi=0
kaybetmesayisi=0

for j in range(10000):
    odullistesi=['bos1', 'bos2', 'bos3', 'bos4', 'bos5', 'araba']
    random.shuffle(odullistesi)
    
    kapilistesi=[1,2,3,4,5,6]
    random.shuffle(kapilistesi)

    sozluk={}
    for i in range(len(kapilistesi)):
        sozluk[kapilistesi[i]]=odullistesi[i]
        
        
    tahmin=random.randint(1,6)
    
    i=0
    while i<=3:
        cikarilacak=random.randint(1,len(kapilistesi))
        if cikarilacak in sozluk and (cikarilacak==tahmin or sozluk[cikarilacak]=='araba'):
            continue
        elif cikarilacak in sozluk:
            sozluk.pop(cikarilacak)
            i+=1
            
            
            
    if sozluk[tahmin]=='araba':
        kazanmasayisi+=1
        
    else:
        kaybetmesayisi+=1        
        
print(f" {kazanmasayisi} kere kazandiniz")
print(f" {kaybetmesayisi} kere kaybettiniz")        