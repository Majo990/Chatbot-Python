#Libreria pyttsx3: convierte un texto a voz
import pyttsx3
voz=pyttsx3.init()
voz.setProperty("rate",150)
listavoces=voz.getProperty("voices")
voz.setProperty("voice",listavoces[0].id)

voz.say("calculadora")
voz.runAndWait()
voz.say("ingrese su nombre y apellido:")
voz.runAndWait()
nombre=input("ingrese su nombre y apellido: ")
voz.runAndWait()
voz.say(nombre)

voz.say("Bienvenido")
voz.runAndWait()
voz.say("ingrese el valor 1 por favor ")
voz.runAndWait()
n1=int(input("ingrese el valor 1: "))
voz.runAndWait()
voz.say(n1)
voz.runAndWait()
voz.say("ingrese el valor 2 porfavor")
voz.runAndWait()
n2=int(input("ingrese el valor 2: "))
voz.runAndWait()
voz.say(n2)
voz.runAndWait()

suma=n1+n2
resta=n1-n2
multiplicar=n1*n2
dividir=n1/n2

voz.say("La suma es")
print("La suma es ",suma)
voz.say(suma)
voz.runAndWait()

voz.say("La Resta es")
print("La resta es ",resta)
voz.say(resta)
voz.runAndWait()

voz.say("La Multiplicacion es")
print("La multiplicacion es ",multiplicar)
voz.say(multiplicar)
voz.runAndWait()

voz.say("La division es")
print(" la division es ",dividir)
voz.say(dividir) 
voz.say("Gracias")
voz.runAndWait()
