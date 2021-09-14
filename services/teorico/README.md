- Un caso en el que usarías procesos para resolver un problema y por qué.
    Lo usaria para una tarea relativamente simple, que no implique consumo de recursos excesivos.

- Un caso en el que usarías threads para resolver un problema y por qué.
    Se usan los thread cuando se desarrollan web-scrapers, En este caso, varios hilos pueden encargarse de la búsqueda de varias páginas web en paralelo, lo que hace que no existan cuello de botella por ejemplo al descargar los datos.

- Un caso en el que usarías corrutinas para resolver un problema y por qué.
    Se podria usar una corrutina en el ejercicio propuesto, enviando la consulta a la primera API y esperando que respondiese para luego con los resultados obtenidos, ir a las APIS siguientes.
    "Coroutines make our asynchronous code look sequential." (Coroutines: Suspending State Machines, June 2020)

- Si tuvieras 1.000.000 de elementos y tuvieras que consultar para cada uno de ellos
información en una API HTTP. ¿Cómo lo harías? Explicar.

Usaria request en paralelo usando colas e hilos. 
Supongamos que esta tarea se compara con un restaurante, entonces el camarero responsable de llevar la comida a la mesa es el hilo, y cada mesa representa un elemento para consultar.

Cuando usamos varios hilos para completar tareas, entonces
"Por cada comensal que se acerca a una mesa, se coloca un mesero en esa mesa, es decir, tantos comensales tienen que corresponder a tantos meseros"
Cuando un mesero termina de servir la mesa, toma el siguiente pedido en la cola (FIFO puede funcionar).

