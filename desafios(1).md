# Desafíos para Practicantes — Secure Ecommerce (FastAPI + Arquitectura Hexagonal)

Este documento define **desafíos incrementales** para extender el proyecto base `secure_ecommerce_hexagonal` (backend en FastAPI con Arquitectura Hexagonal) e incorporar un **frontend integrado**.  
La idea es que cada desafío sea **entregable**, evaluable y alineado a prácticas de ingeniería de software y ciberseguridad.

---

## 0) Regla de oro de ingeniería (aplica a todo)
- Mantener **Arquitectura Hexagonal**:  
  - **Dominio** (entidades + reglas) no depende de frameworks.  
  - **Puertos** (interfaces) definen contratos.  
  - **Adaptadores** (infraestructura) implementan puertos.
- Cada cambio relevante debe incluir:
  - Pruebas (unitarias o integración, según corresponda).
  - Documentación mínima (README / OpenAPI / decisiones).
  - Manejo de errores consistente.

---

## 1) Backend: Productos “de verdad” (persistencia y validación)
### Objetivo
Pasar de repositorio en memoria a persistencia real.

### Entregables
- Implementar un adaptador de persistencia (por ejemplo, base de datos relacional).
- Agregar operaciones CRUD:
  - Crear, listar, obtener por id, actualizar, eliminar (con borrado lógico opcional).
- Validación robusta con modelos de entrada/salida:
  - Precio positivo
  - Nombre no vacío, largo máximo
  - Stock no negativo (si aplica)

### Criterios de éxito
- Dominio y puertos no dependen de la base de datos.
- Las rutas usan servicios/casos de uso (no lógica en controladores).
- Pruebas de integración mínimas para CRUD.

---

## 2) Backend: Carrito de compras (caso de uso central)
### Objetivo
Implementar un carrito por usuario (o por sesión).

### Entregables
- Entidades de dominio sugeridas:
  - `Cart`, `CartItem`
- Casos de uso:
  - Crear carrito
  - Agregar ítem (producto + cantidad)
  - Quitar ítem
  - Vaciar carrito
  - Obtener carrito (con totales)
- Reglas de negocio:
  - Cantidad mínima 1
  - No permitir agregar productos inexistentes
  - Recalcular totales de forma consistente

### Criterios de éxito
- Reglas en dominio/servicios, no en API.
- Pruebas unitarias para reglas de totales/cantidades.

---

## 3) Backend: Órdenes (checkout) y estado
### Objetivo
Convertir un carrito en una orden.

### Entregables
- Entidades sugeridas:
  - `Order`, `OrderItem`
- Estados:
  - `CREADA`, `PAGADA`, `DESPACHADA`, `CANCELADA`
- Caso de uso “checkout”:
  - Toma el carrito
  - Valida stock
  - Genera orden
  - Vacía carrito
- Persistencia de órdenes y consultas por usuario.

### Criterios de éxito
- Estados controlados (no strings libres).
- Validaciones en el dominio (transiciones válidas).

---

## 4) Backend: Inventario y concurrencia (problema real)
### Objetivo
Evitar sobreventa en escenarios concurrentes.

### Entregables
- Implementar control de stock al crear una orden:
  - Estrategia 1: transacción + bloqueo
  - Estrategia 2: control optimista (versionado)
- Simular concurrencia con pruebas:
  - 2 checkouts simultáneos sobre el mismo producto.

### Criterios de éxito
- No se permite stock negativo.
- Prueba reproducible que demuestra que el enfoque funciona.

---

## 5) Ciberseguridad: Autenticación y autorización (nivel profesional)
### Objetivo
Proteger el backend con control de acceso.

### Entregables
- Autenticación:
  - Registro de usuarios
  - Login seguro (hash fuerte)
  - Tokens de acceso y refresco
- Autorización:
  - Roles sugeridos: `admin`, `customer`, `auditor`
  - Reglas:
    - `admin`: CRUD productos, ver todas las órdenes
    - `customer`: ver sus órdenes, usar carrito/checkout
    - `auditor`: lectura de auditoría
- Endpoints protegidos por dependencia de seguridad.

### Criterios de éxito
- Contraseñas hasheadas (nunca en claro).
- Tokens con expiración y validación correcta.
- Pruebas de “no autorizado” y “forbidden”.

---

## 6) Ciberseguridad: Protección de API (OWASP y abuso)
### Objetivo
Reducir superficie de ataque y abuso.

### Entregables
- Rate limiting en endpoints críticos (login, checkout).
- CORS configurado correctamente (solo orígenes permitidos).
- Validación de entrada estricta (sin campos inesperados).
- Respuestas de error consistentes (sin filtrar trazas internas).
- Cabeceras recomendadas (cuando aplique).
- Política de contraseñas y bloqueo por intentos fallidos (básico).

### Criterios de éxito
- Evidencia en documentación: “amenaza → mitigación”.
- Pruebas básicas para inputs inválidos y límites.

---

## 7) Auditoría y trazabilidad (listo para auditoría interna)
### Objetivo
Registrar acciones relevantes de manera útil.

### Entregables
- Registro de eventos para:
  - Login exitoso/fallido
  - Creación/modificación de productos
  - Checkout y cambios de estado de orden
- Guardar:
  - Usuario
  - Acción
  - IP (si está disponible)
  - Fecha/hora
  - Recurso (endpoint)
  - Resultado (éxito/fallo)
- Endpoint de consulta para rol `auditor`.

### Criterios de éxito
- Los eventos no rompen la arquitectura (puerto + adaptador).
- Documentación de auditoría en `README` o `docs/`.

---

## 8) Observabilidad: logging, métricas y trazas
### Objetivo
Operabilidad en producción.

### Entregables
- Logging estructurado (con correlación por request-id).
- Métricas mínimas:
  - Latencia por endpoint
  - Tasa de errores
- Healthcheck:
  - `/health` (API viva)
  - `/ready` (dependencias listas)

### Criterios de éxito
- Logs útiles para investigar incidentes.
- Endpoints de salud usados en despliegue.

---

## 9) Calidad: pruebas, cobertura y estándares
### Objetivo
Subir calidad a estándar profesional.

### Entregables
- Pruebas unitarias:
  - Reglas de dominio (carrito, totales, estados)
- Pruebas de integración:
  - Flujo: registro → login → carrito → checkout
- Cobertura mínima sugerida: 70% (ajustable).
- Formato y calidad:
  - Linter / formateador
  - Tipado estático básico

### Criterios de éxito
- Pipeline ejecutable localmente con un comando.
- Reporte de cobertura visible.

---

## 10) Documentación y diseño (para “handover”)
### Objetivo
Que otro equipo lo pueda operar y extender.

### Entregables
- README mejorado:
  - Arquitectura (capas y responsabilidades)
  - Cómo correr local
  - Variables de entorno
  - Seguridad (qué se implementó y por qué)
- OpenAPI:
  - Ejemplos en request/response
  - Códigos de error
- Documento de decisiones (ADR):
  - 3 decisiones importantes explicadas.

### Criterios de éxito
- Un lector externo entiende el sistema en 15 minutos.

---

# 11) Frontend (obligatorio): Aplicación web integrada con el backend
## Objetivo
Crear un frontend profesional que consuma la API y demuestre flujos ecommerce.

## Recomendación técnica (no obligatoria)
- React + TypeScript
- Cliente HTTP con interceptores (tokens)
- Manejo de estado para carrito y sesión
- Rutas protegidas

## Vistas mínimas (MVP)
1. **Login / Registro**
2. **Catálogo de productos**
3. **Detalle de producto**
4. **Carrito**
5. **Checkout**
6. **Historial de órdenes**
7. (Opcional) **Panel admin** (CRUD productos)

## Integración con el backend
### Requisitos
- Configurar base URL por entorno.
- Manejar token:
  - Guardar tokens de forma segura (según estrategia acordada)
  - Refrescar token (si existe refresh)
  - Interceptor: si 401 → reintentar flujo de refresh
- Mostrar errores de forma amigable (sin mensajes técnicos).

## Seguridad del frontend (mínimo)
- Validación en cliente (pero siempre validación final en servidor).
- Evitar almacenar secretos en el frontend.
- Proteger rutas y ocultar UI según rol.
- CORS: coordinar con el backend.

## Criterios de éxito
- Flujo completo funciona:
  - Usuario se registra → inicia sesión → agrega productos → compra → ve orden.
- Código con estructura limpia:
  - `pages/`, `components/`, `services/`, `store/`, `routes/`.

---

## 12) DevOps básico: contenedores y despliegue local
### Objetivo
Reproducibilidad y ejecución fácil.

### Entregables
- Dockerfile para backend
- Dockerfile para frontend
- docker-compose para levantar:
  - Backend
  - Base de datos
  - (Opcional) proxy o servicio de métricas
- Variables por entorno

### Criterios de éxito
- Un comando: `docker compose up`
- Documentación de puertos y configuración.

---

## 13) Desafío final (capstone): “modo empresa”
### Objetivo
Entregar un sistema cercano a producción.

### Entregables
- Modelo de amenazas (simple):
  - 5 amenazas y mitigaciones
- Auditoría activa
- Rate limiting
- Pruebas CI (pipeline)
- Informe final:
  - arquitectura, seguridad, pruebas, riesgos

### Criterios de éxito
- Se puede evaluar con checklist.
- Demuestra criterio de ingeniería.

---

## Checklist de evaluación sugerido
- [ ] Arquitectura hexagonal respetada
- [ ] Seguridad base implementada y probada
- [ ] Flujo ecommerce completo (carrito + checkout + órdenes)
- [ ] Frontend integrado y funcional
- [ ] Pruebas relevantes y reproducibles
- [ ] Documentación clara y suficiente
- [ ] Manejo de errores consistente
- [ ] Auditoría con evidencia

---

## Sugerencia de planificación (4–8 semanas)
- Hito 1: Persistencia + CRUD + pruebas
- Hito 2: Carrito + órdenes
- Hito 3: Seguridad (auth + roles)
- Hito 4: Frontend (MVP integrado)
- Hito 5: Auditoría + observabilidad
- Hito 6: Hardening + documentación + capstone

