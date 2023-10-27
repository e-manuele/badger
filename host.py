import serial.tools.list_ports as port_list
import serial
import time
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s  %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename='example.log')
card_db=['2236835850','3111483307','2798319075']
com = ""
target = ":x.0"
name_1 ="COM3"
name ="COM20"
ports = list(port_list.comports())
for port in ports:
    print(port)
    print(port.name)
print("Inizio...")
# Aggiungi una variabile globale per memorizzare l'ultimo timestamp di lettura di una carta
last_card_read_time = 0
# Definisci un intervallo di debounce in millisecondi (ad esempio, 1000 ms = 1 secondo)
DEBOUNCE_INTERVAL_MS = 2000
for port in ports:
    #print(str(port.location).__contains__(target))
    #print(port.location)
    if str(port.name) == name:
    #if str(port.location).__contains__(target):
        com = port.name
        print("...connessione...")
        while True:
            time.sleep(3)
            s = serial.Serial(com, baudrate=115200,
                              parity=serial.PARITY_NONE,
                              stopbits=serial.STOPBITS_ONE,
                              bytesize=serial.EIGHTBITS,
                              timeout=1
                              )
            
            s.write(b"on\n")
            while True:
                print(".")
                s.write(b".\n")
                card = s.readline().decode("utf-8") .strip()
                current_time = int(time.time() * 1000)
                if len(card)>0:
                    if card.__contains__("..."):
                        continue
                    if current_time - last_card_read_time >= DEBOUNCE_INTERVAL_MS:
                        print(f"Confronto nel database {card}")
                        if card in card_db:
                            s.write(b"ok\n")
                            print(f"Match found with {card}")
                            logging.debug('This message was written from pico: ')
                            logging.info(card)
                        else:
                            s.write(b"no\n")
                            print("Match not found")
                        last_card_read_time = current_time

