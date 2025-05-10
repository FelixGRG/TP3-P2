# TP3-P2
Gestión de Productos (API Simple)

Este proyecto es una API simple para agregar y listar productos, implementada en Python Flask, con separación en tres capas.

# Estructura del proyecto
.
├── app.py               # Capa de presentación
├── business_logic.py    # Capa de lógica de negocio
├── data_access.py       # Capa de acceso a datos
└── README.md 
# Descripción de cada capa
	1.	Capa de presentación (app.py):
	•	Se encarga de recibir y responder a las solicitudes HTTP (rutas/endpoints).
	•	Solo delega las peticiones a la lógica de negocio y formatea la respuesta para el cliente.
	2.	Capa de lógica de negocio (business_logic.py):
	•	Contiene las reglas de negocio.
	•	Valida los datos recibidos, estructura los productos y gestiona la lógica antes de interactuar con la capa de acceso a datos.
	3.	Capa de acceso a datos (data_access.py):
	•	Simula la base de datos usando una lista en memoria.
	•	Proporciona funciones para guardar y recuperar productos.

⸻

# Ventajas respecto a la versión monolítica
	•	Mantenibilidad: El código está organizado por responsabilidades, lo que facilita localizar errores y hacer cambios en una parte específica sin afectar otras capas.
	•	Reusabilidad: La lógica de negocio y acceso a datos pueden ser reutilizadas por otros tipos de interfaces (por ejemplo, una CLI o un servicio externo).
	•	Escalabilidad: Permite reemplazar fácilmente la capa de datos (por ejemplo, cambiar la lista en memoria por una base de datos real) sin modificar la lógica de negocio ni la presentación.
	•	Pruebas más simples: Cada capa se puede testear de forma independiente (mockeando las otras capas).
