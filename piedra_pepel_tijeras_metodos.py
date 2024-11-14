import random
from objetos import *

def jugar():
    final_usuario=usuario()
    final_pc=pc()
    mecanismo(final_usuario,final_pc)
    pass


def pc():
    opcion_pc=random.choice(options)
    print(opcion_pc.name)
    return opcion_pc
        
def usuario():
        eleccion=True
        while eleccion:
            opcion_user=input("Elige piedra, papel o tijera: 1,2,3:")
            if opcion_user == "1":
                opcion_final=piedra
                eleccion=False
            elif opcion_user == "2":
                opcion_final=papel
                eleccion=False
            elif opcion_user == "3":
                opcion_final=tijeras
                eleccion=False
            else:
                print("Ingresa una opcion que sea Valida")
                eleccion=True
        
        return opcion_final


def mecanismo(final,finalpc):
                if final.name == finalpc.name :
                    print(f"Empate!! usted a elegido{final.name} y la computadora a elegido {finalpc.name}")
                elif final.name == finalpc.strong_a:
                    print(f"Perdiste!! Elegiste {final.name} y la computadora eligio {finalpc.name}")
                elif final.name == finalpc.weak_a:
                    print(f"Ganaste!! Elegiste {final.name} y la computadora eligio {finalpc.name}")
                return volver()

        
             
def volver():
        volver_r=input(f"Quieres volver a jugar?").lower()

        if volver_r=="si":
             jugar()
        else:
             print("ok")
            


jugar()