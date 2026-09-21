#1. Escribe qué resultado crees que mostrará.
#DBCA devido y el otro una lista del recorrido que seguira el metodo, 

#2. Explica por qué.
# llama a D, que llama a B, que llama a C, que llama a A. y mro es el mapa que siguie el metodo para recorrer la herencia

#3. Ejecútalo y comprueba la respuesta.
class A:
    def metodo(self):
        return "A"
class B(A):
    def metodo(self):
        return "B" + super().metodo()
class C(A):
    def metodo(self):
        return "C" + super().metodo()
class D(B, C): 
    def metodo(self):
        return "D" + super().metodo()
obj = D()
print(obj.metodo())
print(D.mro())

#4. Modifica únicamente el orden de herencia de D y explica cómo cambia el resultado.
class D(C, B):  # Cambiamos el orden de herencia
    def metodo(self):
        return "D" + super().metodo()
#Sera DCBA porque llamo primero a C y no a B.

#5. Explica qué está haciendo realmente super() en este ejemplo.
#El método super() está llamando al siguiente método en la herencia.