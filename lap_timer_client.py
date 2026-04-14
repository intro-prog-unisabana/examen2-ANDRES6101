# lap_timer_client.py
# Programa cliente que lee tiempos de vuelta de un archivo
# e imprime la racha decreciente mas larga.

import lap_timer


def main():
   
    # TODO: Pedir el nombre del archivo al usuario usando input()
    filename = input("Nombre del archivo: ")
    
    # TODO: Abrir el archivo y leer el numero de vueltas n
    with open(filename,'r') as f:
        n = int(f.readline())
    
    # TODO: Crear el cronometro usando lap_timer.init(n)
    timer = lap_timer.init(n)
    
    # TODO: Leer los n tiempos de vuelta y agregarlos con lap_timer.add_lap()
    with open(filename, 'r') as f:
        for _ in range(n):
            time = float(f.readline().strip())
            timer = lap_timer.add_lap(timer, time)

    # TODO: Imprimir la racha decreciente mas larga
    #       usando lap_timer.longest_decreasing_streak()
    print( lap_timer.longest_decreasing_streak(timer))

    pass


if __name__ == "__main__":
    main()


