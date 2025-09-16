
Modo de Ahorro de Energía - SmartHome Luces Inteligentes
========================================================

Descripción General
-------------------

Función: Opción 5 del Menú Principal
Módulo: src/services/gestion_dispositivos.automatizacion_por_horario()
Tipo: Automatización por horario programado

Objetivo
--------
Optimizar automáticamente el consumo energético del sistema de iluminación mediante la aplicación de reglas predefinidas basadas en horarios específicos.

Funcionamiento
Flujo de Ejecución
------------------

Secuencia de la automatización
------------------------------
1. usuario selecciona opción 5 → menu()
2. cargar lista de luces → cargar_luces()
3. ejecutar automatización → automatizacion_por_horario(luces)
4. aplicar reglas según horario actual
5. mostrar confirmación → "Modo de ahorro de energia ejecutado."
Reglas de Automatización
Horario Nocturno (22:00 - 06:00)
Acción: Apagar 70% de luces no esenciales

Áreas afectadas: Habitaciones vacías, pasillos, áreas comunes

Excepciones: Luces en áreas ocupadas, iluminación de seguridad

Horario Laboral (09:00 - 17:00)
Acción: Mantener iluminación mínima en áreas no ocupadas

Intensidad: Reducción al 30% en zonas de baja frecuencia

Monitorización: Sensores de presencia activados

Horario Pico Energético (18:00 - 21:00)
Acción: Reducir intensidad lumínica en 50%

Enfoque: Áreas con mayor consumo energético

Optimización: Balance entre confort y ahorro

Parámetros Configurables
python

Estructura de Función
---------------------
- Lógica de detección de horario actual
- Aplicación de reglas correspondientes
- Registro de cambios realizados

Mensajes al Usuario
-------------------
Confirmación de ejecución:
"Modo de ahorro de energia ejecutado."



python
METRICAS_AHORRO = {
    "luces_afectadas": int,
    "watts_ahorrados": float,
    "porcentaje_reduccion": float,
    "tiempo_ejecucion": float
}
