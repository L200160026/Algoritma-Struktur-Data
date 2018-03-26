#Python 3.6

#[NO_1]
print ("==[No_1]==")
def Hercules():
    Odin = []
    bolu = 0
    for x in range(20):
        if x%2 == 0:
            bolu += x
            Odin.append(bolu)
        else:
            pass
    return Odin

print (Hercules())


#[NO_2]
print ("\n==[No_2]==")
def palingkecilPalingBesar(data):
    rid1 = [data[0],data[0]]
    for x in data:
        if x < rid1[0]:
            rid1[0] = x
        if x > rid1[1]:
            rid1[1] = x
    return rid1
            
print (palingkecilPalingBesar([45,23,17,2,54,87,32,132,38,8,96,32,22,16,5,17]))


#[NO_3]
print ("\n==[No_3]==")
class bungaKu():
    def __init__(self, nama, jumlah, harga):
        self.nama = nama
        self.jumlah = jumlah
        self.harga = harga
    def __str__(self):
        return "Nama Bunga\t: "+self.nama+"\nJumlah Bunga\t: "+str(self.jumlah)+"\nHarga Bunga\t: "+str(self.harga)

    def setNama(self, nama):
        self.nama = str(nama)
    def setJumlah(self, jumlah):
        self.jumlah = jumlah
    def setHarga(self, harga):
        self.harga = harga

    def getNama(self):
        print ("Nama Bunga\t:",self.nama)
    def getJumlah(self):
        print ("Jumlah Bunga\t:",self.jumlah)
    def getHarga(self):
        print ("Harga Bunga\t:",self.harga)


Aku = bungaKu("Bangkai", 75, 345700)
print("=Before=")
print (Aku)
Aku.setNama("Begonia")
Aku.setJumlah(85)
Aku.setHarga(886300)
print ("=After=")
Aku.getNama()
Aku.getJumlah()
Aku.getHarga()

print ("\n\n")
Dia = bungaKu("Bakung", 87, 786740)
print("=Before=")
print (Dia)
Dia.setNama("Aster")
Dia.setJumlah(26)
Dia.setHarga(485000)
print("=After=")
Dia.getNama()
Dia.getJumlah()
Dia.getHarga()

print ("\n\n")
Kamu = bungaKu("Asoka", 48, 654700)
print("=Before=")
print (Kamu)
Kamu.setNama("Allamanda")
Kamu.setJumlah(76)
Kamu.setHarga(764895)
print("=After=")
Kamu.getNama()
Kamu.getJumlah()
Kamu.getHarga()


#====
import collections
import numpy as numpang

class Vector:
  def __init__(self, d):
    if isinstance(d, int):
      self._coords = [0] * d
    else:
      try:                                     
        self._coords = [val for val in d]
      except TypeError:
        raise TypeError('invalid parameter type')

  def __len__(self):
    return len(self._coords)

  def __getitem__(self, j):
    return self._coords[j]

  def __setitem__(self, j, val):
    self._coords[j] = val

  def __add__(self, other):
    if len(self) != len(other):          
      raise ValueError('dimensions must agree')
    result = Vector(len(self))           
    for j in range(len(self)):
      result[j] = self[j] + other[j]
    return result

  def __str__(self):
    return '<' + str(self._coords)[1:-1] + '>'  


#[NO_4]
  def __sub__(self, other):
    if len(self) != len(other):          
      print('dimensi harus benar')
    else:
      geng = []
      for i in range(len(self)):
        adalah = self[i] - other[i]
        geng.append(adalah)
      return geng

    
#[NO_5]
  def __mul__(self, other):
    if len(self) != len(other):          
      print('dimensi harus benar')
    else:
      vulcan = 0
      for i in range(len(self)):
        vulcan += self[i] * other[i]
    return vulcan

#NO4
print ("\n==[No_4]==")
ddr3 = Vector([5,6,7,1,2])
ddr4 = Vector([3,2,5,4,5])
skaar = ddr3 - ddr4
print ("Output Penjumlahan :",skaar)

#NO5
print ("\n==[No_5]==")
durian = Vector([4,5,6])
nangka = Vector([8,5,2])
R026 = durian * nangka
print ("Output Perkalian :",R026)


#[NO_6]
print ("\n==[No_6]==")
def Galactus(u,v):
    if len(u) == len(v) and len(u[0]) == len(v[0]) and len(u[0][0]) == len(v[0][0]):
        rid1 = numpang.array(u) + numpang.array(v)
        kali = numpang.array(u) * numpang.array(v)
        print ("=====[Penambahan]===== \n",rid1)
        print ("=====[Perkalian]===== \n",kali)
    else:
        print ('dimensi harus benar')

pensil = [[[2,4,6],[8,9,10]],[[1,3,5],[7,9,11]],[[1,2,3],[4,5,6]]]
bolpen = [[[2,4,6],[8,9,10]],[[1,3,5],[7,9,11]],[[1,2,3],[4,5,6]]]
Galactus(pensil,bolpen)


#[NO_7]
print ("\n==[No_7]==")
def thanos(n):
    if len(n) == 3 and len(n[0]) == 3:
        d1 = n[0][0]*((n[1][1]*n[2][2])-(n[1][2]*n[2][1]))
        d2 = n[0][1]*((n[1][0]*n[2][2])-(n[1][2]*n[2][0]))
        d3 = n[0][2]*((n[1][0]*n[2][1])-(n[1][1]*n[2][0]))
        R026 = d1 - d2 + d3
        return R026
    elif len(n) == 2 and len(n[0]) == 2:
        R026 = (n[0][0] * n[1][1]) - (n[0][1]*n[1][0])
        return R026
    else:
        print ("Matrix harus ordo 2x2 atau 3x3")


avenger = [[2,-5,3],[-7,2,1],[0,4,9]]
print ("det :",thanos(avenger))



class Node:
    def __init__(self, data, nextNode=None):
        self.data = data
        self.nextNode = nextNode

    def getData(self):
        return self.data

    def setData(self, val):
        self.data = val

    def getNextNode(self):
        return self.nextNode

    def setNextNode(self, val):
        self.nextNode = val


class LinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.size = 0


    #===[No_8]===
    def addNode(self, peter):
        if self.head == None:
            newNode = Node(peter)
            self.head = newNode
            self.size += 1
        else:
            loki = self.head
            while loki is not None:
                if loki.nextNode == None:
                    loki.nextNode = Node(peter)
                    self.size += 1
                    break
                else:
                    loki = loki.nextNode
        return True

    
    #===[No_9]===
    def getSize(self):
        return self.size

    def printNode(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.getNextNode()


myList = LinkedList()
myList.addNode(100)
myList.addNode(200)
myList.addNode(300)
myList.addNode(400)
myList.addNode(500)
myList.addNode(600)
myList.addNode(700)
print ("\n==[No_8]==")
myList.printNode()

print ("\n==[No_9]==")
print("Byk node :",myList.getSize())
