import re

def verificar_email(email):

    patron= r"\w+\@\w+(\.com|\.br)"
    busqueda=re.search(patron,email)
    
    if busqueda :
        print("ok")
    else:
        print("La direccion de email es incorrecta")




nuevo_correo=verificar_email("ofarredondo@gmail.com") 



