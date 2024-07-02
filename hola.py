import re

def solicitar_numero_celular():
    while True:
        numero_celular = input("Ingrese su número de celular: ")
        if re.match(r"^\d{10}$", numero_celular):
            return numero_celular
        else:
            print("Número de celular inválido. Debe contener 10 dígitos.")

def solicitar_correo_electronico():
    while True:
        correo_electronico = input("Ingrese su correo electrónico: ")
        if re.match(r"^[a-zA-Z0-9._%+-]+@(gmail|hotmail)\.com$", correo_electronico):
            return correo_electronico
        else:
            print("Correo electrónico inválido. Debe ser @gmail.com o @hotmail.com.")

def main():
    numero_celular = solicitar_numero_celular()
    correo_electronico = solicitar_correo_electronico()

    print(f"Número de celular: {numero_celular}")
    print(f"Correo electrónico: {correo_electronico}")

if __name__ == "__main__":
    main()
