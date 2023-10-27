import pyb

# Definizione del LED
led = pyb.LED(1)

# Inizializzazione della libreria USB_VCP
usb = pyb.USB_VCP()

# Ciclo infinito
while True:
    # Controllo dello stato della connessione
    if usb.connected():
        # Accensione del LED
        led.on()
    else:
        # Spegnimento del LED
        led.off()

    # Pausa di 1 secondo
    pyb.delay(1000)
