class Kume():
    def __init__(self,isim,elemanlar = []):
        list1 =[]
        self.isim = isim
        self.uzay = type(elemanlar[0])
        for i in elemanlar:
            if i not in list1:
                list1.append(i)
        self.elemanlar = list1
        self.elemansayisi = len(self.elemanlar)
        self.alt_kume_sayisi = pow(2,self.elemansayisi)
        self.oz_alt_kume_sayisi = self.alt_kume_sayisi-1

    def birlesim(self,kume=[]):
        birlesim = Kume("birlesim kumesi","None",self.elemanlar)
        for i in kume:
            if i not in self.elemanlar:
                birlesim.elemanlar.append(i)
        return birlesim

    def kesisim(self,kume=[]):
        kesisim =Kume("Kesisim kumesi",self.uzay,kume)
        for i in kume:
            if i not in self.elemanlar:
                kesisim.elemanlar.remove(i)
        return kesisim
