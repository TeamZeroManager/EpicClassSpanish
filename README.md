# EpicClassSpanish

Complemento independiente de traducción al **español neutro** para **Epic Class Mod 3.0.2**, Minecraft **1.20.1** y **Minecraft Forge 47.x**.

## Objetivo

Añadir recursos en español sin modificar las clases, habilidades, estadísticas, recompensas, requisitos ni mecánicas del mod original.

## Compatibilidad

- Minecraft 1.20.1
- Minecraft Forge 47.x
- Epic Class Mod 3.0.2
- Java 17

## Contenido actual

- Guion en español de las **23 misiones principales y el epílogo**, en `src/main/resources/assets/epicclassmod/quests/es_es.txt`.
- Parche incremental de idioma con **779 claves nuevas** en `src/main/resources/assets/epicclassmod/lang/es_es.json`.
- Traducciones para partes del árbol de habilidades, selección de clase, interfaz de hechizos y misiones, objetivos, eventos, objetos, nombres de clases, controles, diálogos secundarios y misiones de clase, entidades, mensajes, tooltips, subtítulos y elementos del HUD.
- Proyecto ForgeGradle, metadatos del mod y flujo de compilación en GitHub Actions.

## Estado de traducción

La versión 3.0.2 contiene 1.389 claves en inglés. El mod original ya incluye 613 claves en español y este complemento añade las 779 restantes. No quedan claves del archivo inglés sin una traducción española correspondiente. Consulta [translation_status.txt](translation_status.txt) para ver el recuento y las áreas pendientes.

La cobertura de claves de idioma ya está completa. Aún falta validar en el juego la prioridad de los recursos, la carga de las misiones y el ajuste visual de los textos.

## Compilar

1. Instala Java 17.
2. Abre el proyecto con IntelliJ IDEA o Eclipse, o ejecuta Gradle desde una terminal.
3. Ejecuta `gradle build` (o `gradlew build` si tienes un wrapper local).
4. El JAR se genera en `build/libs/epicclassspanish-1.0.0.jar`.
5. Coloca el JAR junto al Epic Class Mod original en la carpeta `mods`.
6. Inicia Minecraft con el idioma Español (España).

## Pruebas pendientes

- Confirmar dentro del juego que el archivo de idioma incremental del complemento se combina correctamente con el del mod original.
- Confirmar que el guion de misiones se carga desde el complemento.
- Revisar dentro del juego la calidad contextual de las traducciones y el ajuste visual de los textos.
- Ejecutar la compilación de GitHub Actions y probar el JAR en una instancia limpia de Forge 1.20.1.

## Nota técnica

Los recursos reutilizan deliberadamente el namespace original `epicclassmod`, porque el mod consulta las rutas de idioma y misiones bajo ese namespace. La prioridad efectiva entre los recursos de ambos mods debe verificarse con la versión exacta instalada. La compilación del complemento, por sí sola, no demuestra que el juego esté seleccionando los archivos traducidos.

## Créditos

Proyecto de traducción no oficial, sin afiliación con los autores de Epic Class Mod. Los créditos y derechos del mod original pertenecen a sus respectivos autores.
