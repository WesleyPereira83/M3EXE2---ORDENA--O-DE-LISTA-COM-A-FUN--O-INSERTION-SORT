import random
vetor = list(range(0,30))
random.shuffle(vetor)
print("Números pares e ímpares desordenados => ", vetor)
print(' ')


def insertion_sort(vetor):
   
     
     for i in range(1, len(vetor)):
         j = i
         while vetor[j - 1] > vetor[j] and j > 0:
          vetor[j - 1] , vetor[j] = vetor[j], vetor[j - 1]
          j-=1


vetor = list(range(0,30))
random.shuffle(vetor)
insertion_sort(vetor)
print("Números pares e ímpares ordenados => ", vetor)
print(' ')


num = []
for number in vetor:
   if number % 2 == 1:
    num.append(number)

print("Números ímpares ordenados => ", num)