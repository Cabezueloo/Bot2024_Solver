# 2048 Bot

Este repositorio contiene un bot diseñado para resolver el juego **2048**. El bot utiliza el patrón de diseño **MVC** (Modelo-Vista-Controlador).

## Estructura del Programa

### Modelo
El **Modelo** contiene el **Tablero** (`Board`), que está compuesto por objetos **Caja** (`Box`). El tablero se maneja utilizando la librería **Numpy** para facilitar las operaciones matemáticas y de matrices.

### Vista
La **Vista** gestiona las capturas de pantalla y la visualización de los datos, incluyendo la interacción visual del juego.

### Controlador
El **Controlador** ejecuta el bucle principal. El ciclo de funcionamiento sigue estos pasos:
1. Captura el estado actual del tablero.
2. Detecta los números y crea internamente un tablero representativo.
3. Analiza las jugadas posibles: arriba, abajo, izquierda, derecha.
4. Evalúa cuál de estos movimientos produce la mayor suma de números.
5. Realiza el movimiento que sume más puntos.

Actualmente, el algoritmo necesita mejoras, ya que no utiliza un sistema recursivo con un sistema de puntos adecuado para tomar decisiones óptimas a largo plazo. Es un área de mejora que planeo abordar pronto.

---

## Instrucciones para Jugar

### Paso 1:
Ejecuta el programa.

### Paso 2:
Haz clic en el área indicada por la imagen y observa cómo el bot toma decisiones automáticamente.

---

## Video de Demostración

Puedes ver una demostración del bot en acción a continuación:

https://github.com/user-attachments/assets/d6f8aadf-98f3-4c41-b7cf-725f67a9feba

---

## Agradecimientos

Gracias por leer este archivo. Si tienes alguna sugerencia o puedes aportar en la mejora del algoritmo, estaré encantado de recibir tu ayuda. Tengo pensado implementar una mejora recursiva en el sistema para optimizar la toma de decisiones.

---

## IMPORTANTE

Para usar este bot, ten en cuenta que los colores pueden variar dependiendo del navegador que utilices. Asegúrate de que los controles mostrados en el **Controlador** coincidan con los valores RGB que ves en tu navegador.

