# El Ciego Inteligente

## Descripción del Problema
En una cárcel, había tres prisioneros: uno con vista normal, uno tuerto y uno ciego. El gobierno decidió indultar a uno de ellos, pero solo el que pudiera resolver un enigma podría salir libre. El alcalde les explicó que iba a colocarles boinas de un conjunto de tres boinas blancas y dos negras, de manera que cada uno no pudiera ver su propia boina.

Después de colocarles las boinas, el alcalde apagó las luces y luego las encendió. Preguntó al prisionero con vista normal si podía adivinar el color de su boina. Él respondió que no podía. Luego, hizo la misma pregunta al tuerto, quien también confesó que no podía deducir el color de su boina. Por último, el alcalde, seguro de que el ciego no podría resolverlo, le preguntó lo mismo. Sin embargo, el prisionero ciego, sorprendiendo al alcalde, respondió que deducía que llevaba una boina blanca.

## Condiciones Iniciales
- Hay tres prisioneros: uno con vista normal, uno tuerto y uno ciego.
- Se colocan boinas de un conjunto de tres boinas blancas y dos negras.
- El prisionero con vista normal puede ver las boinas de los otros dos prisioneros.
- El prisionero tuerto puede ver solo una de las boinas.
- El prisionero ciego no puede ver nada.

## Razonamiento
El razonamiento del prisionero ciego se basa en las respuestas de los otros dos prisioneros:

1. **El prisionero con vista normal** no pudo adivinar el color de su boina. Esto indica que, al observar las boinas de los otros dos, no vio dos boinas negras; si hubiera visto eso, habría deducido que su propia boina era blanca. Por lo tanto, al menos uno de los otros prisioneros (el tuerto o el ciego) debe estar usando una boina blanca.

2. **El prisionero tuerto** también confesó que no podía deducir el color de su boina. Si el prisionero ciego tuviera una boina negra, el prisionero tuerto, habría deducido que su propia boina era blanca, de lo controrio el primer prisionero hubiera deducido el color de la boina. Su incapacidad para deducir su color significa que también lleva una boina blanca.

Con esta información, el ciego concluye que, dado que ambos prisioneros no pudieron deducir el color de sus boinas, él debe llevar una boina blanca.

## Instalación
1. Clona este repositorio:
   ```bash
   git clone https://github.com/RobinsonMolina/The-Intelligent-Blind-Man.git
   ```
2. Navega al directorio del proyecto:
   ```bash
   cd el-ciego-inteligente
   ```
3. Ejecuta el programa:
   ```bash
   python main.py
   ```
