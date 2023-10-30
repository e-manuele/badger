import logging
import csv
import io
import serial.tools.list_ports as port_list
import serial
import time
from datetime import datetime
import logging
class CsvFormatter(logging.Formatter):
    def __init__(self):
        super().__init__()
        self.output = io.StringIO()
        self.writer = csv.writer(self.output, quoting=csv.QUOTE_ALL)

    def format(self, record):
        #record.timestamp = datetime.now().
        self.writer.writerow([record.levelname, record.msg[0], record.msg[1], record.msg[2]])
        data = self.output.getvalue()
        self.output.truncate(0)
        self.output.seek(0)
        return data.strip()
    
logging.basicConfig(level=logging.DEBUG,  filename='example1.log')

logger = logging.getLogger(__name__)
logging.root.handlers[0].setFormatter(CsvFormatter())

card_db=['2236835850','3111483307','2798319075']
card_dict={'2236835850':"Marco",'3111483307':"Matteo",'2798319075':"Gianluca"}
com = ""
target = ":x.0"
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
            
            s = serial.Serial(com, baudrate=115200,
                              parity=serial.PARITY_NONE,
                              stopbits=serial.STOPBITS_ONE,
                              bytesize=serial.EIGHTBITS,
                              timeout=1
                              )
            
            s.write(b"on\n")
            while True:
                time.sleep(1)
                print(".")
                s.write(b".\n")
                card = s.readline().decode("utf-8") .strip()
                current_time = int(time.time() * 1000)
                if len(card)>0:
                    if card.__contains__("..."):
                        continue
                    if current_time - last_card_read_time >= DEBOUNCE_INTERVAL_MS:
                        print(f"Cerco nel database {card}")
                        date = datetime.now().strftime("%d/%m/%Y-%H:%M")
                        if card in card_db:
                            #s.write(b"a\n")
                            print(f"Match found with {card}")
                            logging.info([date , card, card_dict[card]])
                        else:
                            logging.warning([date ,card, "None"])
                            print("Match not found")
                        last_card_read_time = current_time
