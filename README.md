# exercise_ioet 
Ioet's exercise solution, made in Python by Brayan Lechon 

Solucion al ejercicio de Ioet, hecho en Python por Brayan Lechon

**Table of contents/ lista de contenidos**


- [exercise_ioet](#exercise_ioet)
- [English version](#english-version)
  - [Problem](#problem)
  - [Solution Structure](#solution-structure)
  - [How Run localy](#how-run-localy)
    - [Requirements](#requirements)
    - [Steps to run](#steps-to-run)
    - [Recomendations](#recomendations)
  - [Execution Example](#execution-example)
- [Version en Español](#version-en-español)
  - [Problema](#problema)
  - [Estructura de la Solucion](#estructura-de-la-solucion)
  - [Instrucciones de Ejecucion](#instrucciones-de-ejecucion)
    - [Requerimientos](#requerimientos)
    - [Pasos para ejecutar el programa](#pasos-para-ejecutar-el-programa)
    - [Recomendaciones](#recomendaciones)
  - [Ejemplo de ejecución](#ejemplo-de-ejecución)
  
# English version

## Problem
The company X offers their employees the flexibility to work the hours they want. But due to some external circumstances they need to know what employees have been at the office within the same time frame

The goal of this exercise is to output a table containing pairs of employees and how often they have coincided in the office.
## Solution Structure
![flowchart](https://user-images.githubusercontent.com/75377942/141475995-ffeeb633-df92-4ad3-8df7-a9c2238ce058.png)
## How Run localy
### Requirements
- Python3 (3.9 or  superior)
- The proyect not need external libraries because of that **requirements.txt** is empty

### Steps to run
- Clone this repository in your local machine 
- Open the Terminal (if you have windows open CMD)
- Go to the path that cointains the repository files in your machine
- execute the comand:
	- for Windows:
	**`py main.py "name_file"`**
	
	- for Unix(Linux or Mac):  
	**`python3 main.py "name_file"`**
	
	**name_file** = the name of your file with the input information, the repository has an example file named ***data.txt***

### Recomendations
- Be shure that your input file is in the ***"input_file"*** folder
- The extension of the input file is **.txt**
- Follow the next structure to register the hours of the workers in the input file

  ![structure](https://user-images.githubusercontent.com/75377942/141385730-c09f4c8a-4898-4aeb-9d68-39bd9ee3f080.jpg)

## Execution Example 

* Imput file **data.txt** with the register of the employers

  ![image](https://user-images.githubusercontent.com/75377942/141492631-ad3d1a90-9ed4-44cd-a106-d28ef58c1f62.png)
  
  **Reminder:** This file needs to be in the ***input_file*** folder

* In the terminal execution of the code
**`python3 main.py data`**

  ![screen2](https://user-images.githubusercontent.com/75377942/141493220-0848b4f2-0247-4345-a6a9-206a551400ff.jpg)

The program shows the coincidence hours and the output table solution. 

- Finally the output table is saved in a .txt file in the ***results*** folder

  ![Screen3](https://user-images.githubusercontent.com/75377942/141493453-2478885e-09e8-4e3e-8a4b-44b6776f9b3b.jpg)


# Version en Español
## Problema

La compania X ofrece a sus empleados la flexibilidad de trabajar las horas que deseen. Pero por alguna razon ellos necesitan saber que empleados estivieron en la oficina al mismo tiempo

El objetivo de este ejercicio es obtener una tabla que contenga el par de empleados y cuantas veces coincidieron en la oficina.
## Estructura de la Solucion
![flujo](https://user-images.githubusercontent.com/75377942/141477708-5bf6f5f6-92ca-415d-a544-ec44ca1cd4e1.png)
## Instrucciones de Ejecucion
### Requerimientos
- Python3 (3.9 o  superior)
- El proyecto no necesita librerias externas por ello el archivo **requirements.txt** esta vacio.

### Pasos para ejecutar el programa
- Clona este repositorio en una carpeta en tu equipo local
- Abrir la terminal (si tienes Windows abrir el CMD)
- Cambiar el directorio apuntando a la carpeta que contenga los archivos del repositorio
- Ejecuta el comando:
	- en Windows:
	**`py main.py "name_file"`**
	
	- en Unix(Linux o Mac):  
	**`python3 main.py "nombre_archivo"`**
	
	**nombre_archivo** = el nombre del archivo que contiene el registro de los empleados, el repositorio contiene un archivo de ejemplo llamado ***data.txt***

### Recomendaciones
- Asegurate que tu archivo de registros se encuentra en la carpeta ***"input_file"***
- La extension del archivo de registro tiene que ser **.txt**
- La estructura para registrar las horas de los empleados es la siguiente:

  ![structure](https://user-images.githubusercontent.com/75377942/141385730-c09f4c8a-4898-4aeb-9d68-39bd9ee3f080.jpg)


## Ejemplo de ejecución

- Archivo ***data.txt*** con los registros de los empleados
  
  ![image](https://user-images.githubusercontent.com/75377942/141492631-ad3d1a90-9ed4-44cd-a106-d28ef58c1f62.png)

Recordatorio: El archivo debe estar en la carpeta ***input_files***
- Ejecucion del programa en la Terminal con el comando
**`python3 main.py data`**

  ![screen2](https://user-images.githubusercontent.com/75377942/141493220-0848b4f2-0247-4345-a6a9-206a551400ff.jpg)

  El programa muestra las horas en la que los empleados han coincidido y la tabla con los resultados

- Finalmente la salida es guardada en un archivo .txt en la carpeta ***results***.
  
  ![Screen3](https://user-images.githubusercontent.com/75377942/141493453-2478885e-09e8-4e3e-8a4b-44b6776f9b3b.jpg)



