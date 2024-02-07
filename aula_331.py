from collections import deque

#Bom
lista = [0,1,2,3,4,5,6,7,8,9]
lista.append(10)
lista.append(11)

ultimo_removido = lista.pop()

print('último:', ultimo_removido)
print('Lista:', lista)
print()


#Ruim (vai repassar por todos os elementos, vai ficar lento)
lista = [0,1,2,3,4,5,6,7,8,9]

lista.insert(0,10)
lista.insert(0,11)

primeiro_removido = lista.pop(0)

print('Primeiro: ', primeiro_removido)
print('Lista: ', lista)
print()

#Fifo com deque
fila_correta: deque[int] = deque()
fila_correta.append(3)
fila_correta.append(4)
fila_correta.append(5)
fila_correta.appendleft(0)
fila_correta.appendleft(1)
fila_correta.appendleft(2)
print(fila_correta)
fila_correta.pop()
fila_correta.popleft()
print(fila_correta)
