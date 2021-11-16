API Rest para app principal:

Nombre integrantes:
-Sebastián Martínez - 201873519-1
-Iñaki Oyarzun (subordinado) - 201873620-1

Instrucciones de funcionamiento:
-La siguiente API esta encargada de registrar el historial de jugadas realizadas dentro del sistema para generar métricas en cuanto a uso del juego, e igualmente
calcula y entrega el resultado de las jugadas.

El juego es el siguiente:
- Dos jugadores tienen cartas a elegir, estas cartas tienen tipos:Fuego, Agua y Nieve
y a la vez estas cartas tienen numeros.
- Fuego vence a nieve, Nieve vence a Agua y Agua vence a Fuego.
- Y en caso de ser iguales los tipos entre el jugador 1 (usuario) y jugador 2 (bot), gana aquel que tenga un valor mayor
es decir, las jugadas son: <tipo_de_la_carta><numero> (Fuego20,Nieve3,Agua10)

La api recibe los siguientes datos:
jugada1 y jugada2, donde ambas jugadas son un string que indica el tipo de la carta y el numero. ("Fuego20" es "F20")
la API las toma por GET, luego calcula el ganador, añade esos datos al modelo de datos y finalmente retorna ese valor ingresado
para que la API informe de quien gano con esas jugadas (1 si ganó jugador1 y 2 si gano jugador2(CPU))

el formato de ingreso es:

"localhost:8000/?jugada1=F20&jugada2=F30" Donde deberia ganar el jugador2 (CPU).