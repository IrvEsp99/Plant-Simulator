import time
import sys
import random

proceso = random.randint(1, 5)

def cuenta_atras(proceso):
    for queda in range(proceso, 0, -1):
        progreso = int((proceso - queda) / proceso * 30)
        sys.stdout.write(f"\r{queda} restantes...")
        sys.stdout.flush()
        time.sleep(1)

cuenta_atras(proceso)