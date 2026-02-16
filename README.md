# Trabajo 18: Gestión hospitalaria

Para esta tarea, tuvimos que crear una aplicación que contenga dos apartados, uno para pacientes y el otro para médicos.

## Archivos utilizados
Como venimos haciendo hasta ahora, tenemos que usar `scaffold` para crear los ficheros necesarios para la realización de esta tarea.

Además de usar la carpeta models, views y security, fue recomendado usar la carpeta demo para que, al activar la casilla `Demo data`, aparezacan una serie de datos al instalar el módulo.
En el archivo `demo/hospital_demo.xml` es donde creamos los datos de demostración. Primero, creamos nuestros pacientes con `<record id="demo_paciente_(Nº paciente)" model="hospital.paciente">`, después, los médicos `<record id="demo_medico_(Nº médico)" model="hospital.medico">`, por último, las consultas con `<record id="demo_consulta_(Nº consulta)" model="hospital.consulta">`. Cada uno de estos <record> constan de un <field> el cual se encarga de instanciar las variables que tiene cada una de las clases que creamos.

## En Odoo
Creamos la base de datos, entramos a Odoo con "Demo data" activado, activamos el modo de desarrollador y recargamos la lista de aplicaciones, ya podremos ver nuestra aplicación:

<img width="1280" height="390" alt="Captura de pantalla 2026-02-16 115748" src="https://github.com/user-attachments/assets/a478faf7-9006-489c-82f2-a55404292ef1" />

<img width="1280" height="640" alt="Captura de pantalla 2026-02-16 115752" src="https://github.com/user-attachments/assets/7b892aed-1e96-424e-89b3-b31f97a6046e" />

Al activarlo ya podremos entrar en el módulo sin problema y, además, nos aparecerán los datos que introducimos como demostración:

<img width="1280" height="415" alt="Captura de pantalla 2026-02-16 122447" src="https://github.com/user-attachments/assets/f7cfd002-579e-4522-b112-b7d1fa89d348" />

<img width="1280" height="415" alt="Captura de pantalla 2026-02-16 122452" src="https://github.com/user-attachments/assets/da4e7805-4dd1-405f-8fe5-b7d6457d0aa3" />

<img width="1280" height="415" alt="Captura de pantalla 2026-02-16 122456" src="https://github.com/user-attachments/assets/1d02c397-a370-467e-bfa0-033028bbef31" />

También, podemos añadir nuestros propios datos:

<img width="1280" height="640" alt="Captura de pantalla 2026-02-16 122637" src="https://github.com/user-attachments/assets/c63482a6-5108-4f3c-b437-f3bcfa2cf570" />

<img width="1280" height="591" alt="Captura de pantalla 2026-02-16 122642" src="https://github.com/user-attachments/assets/ad6af1b5-5fed-4b6c-b381-6cb90c582328" />

<img width="1280" height="470" alt="Captura de pantalla 2026-02-16 122647" src="https://github.com/user-attachments/assets/bed77486-6274-40b5-b0b4-27c637747cd3" />

Y el resultado sería el siguiente:

<img width="1280" height="415" alt="Captura de pantalla 2026-02-16 122709" src="https://github.com/user-attachments/assets/d6d567b5-9efb-474b-9f87-dc169e87a06a" />

<img width="1280" height="415" alt="Captura de pantalla 2026-02-16 122711" src="https://github.com/user-attachments/assets/5283448d-e419-43df-85d1-95454de586ba" />

<img width="1280" height="415" alt="Captura de pantalla 2026-02-16 122714" src="https://github.com/user-attachments/assets/265840fe-9a49-4216-ad40-3e7ae7bea744" />

