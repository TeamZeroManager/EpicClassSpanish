# EpicClassSpanish

Complemento independiente de traducción al **español neutro** para **Epic Class Mod 3.0.2**, Minecraft **1.20.1** y **Minecraft Forge 47.x**.

## Objetivo

Añadir recursos en español sin modificar las clases, habilidades, estadísticas, recompensas, requisitos ni mecánicas del mod original.

## Compatibilidad

- Minecraft 1.20.1
- Minecraft Forge 47.x
- Epic Class Mod 3.0.2 o superior
- Java 17

## Estado de traducción

El archivo de idioma inglés de la versión 3.0.2 contiene 1.389 claves. El archivo español que ya incluye el mod original contiene 613 claves; quedan 779 claves por traducir. El estado detallado está en [translation_status.txt](translation_status.txt).

El guion español de las misiones principales se prepara en:

`src/main/resources/assets/epicclassmod/quests/es_es.txt`

No se marcará una sección como terminada hasta revisar sus textos y probarla dentro del juego.

## Compilar

1. Instala Java 17.
2. Abre el proyecto con IntelliJ IDEA o Eclipse, o ejecuta Gradle desde una terminal.
3. Ejecuta `gradle build` (o `gradlew build` si tienes un wrapper local).
4. El JAR se genera en `build/libs/epicclassspanish-1.0.0.jar`.
5. Coloca el JAR junto al Epic Class Mod original en la carpeta `mods`.
6. Inicia Minecraft con el idioma Español (España).

## Nota técnica importante

Los recursos de traducción reutilizan el namespace original `epicclassmod`. La prioridad efectiva entre los recursos de ambos mods debe verificarse con la versión exacta del mod instalada. La compilación del complemento, por sí sola, no demuestra que el juego esté seleccionando los archivos traducidos.

## Créditos

Proyecto de traducción no oficial, sin afiliación con los autores de Epic Class Mod. Los créditos y derechos del mod original pertenecen a sus respectivos autores.
