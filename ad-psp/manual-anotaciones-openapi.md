# Manual de anotaciones de OpenAPI
## 1. Nivel Global (Configuración)

Se coloca en una clase `@Configuration` para definir la metainformación de la API y la seguridad global.

### `@OpenAPIDefinition`
* `info`: Recibe `@Info` (título, versión, descripción).
* `servers`: Lista de `@Server` con las URLs base de la API.

#### Anotaciones secundarias:
* `@Info`: title, version, description.
* `@Server`: url, description.

### `@SecurityScheme`
Define el mecanismo de autenticación (ej. JWT Bearer).
* `name`: Identificador único del esquema.
* `type`: SecuritySchemeType.HTTP.
* `scheme`: "bearer".
* `bearerFormat`: "JWT".

---

## 2. Nivel Controlador (`@RestController`)

### `@Tag`
Agrupa los endpoints bajo un mismo título en Swagger UI.
* `name`: Nombre del grupo.
* `description`: Breve descripción del grupo.

### `@SecurityRequirement`
Aplica la seguridad definida en `@SecurityScheme` a todo el controlador.
* `name`: Nombre del `@SecurityScheme` a aplicar.

---

## 3. Nivel Endpoint (Método)

### `@Operation`
Describe el funcionamiento del endpoint.
* `summary`: Resumen corto en una línea.
* `description`: Explicación detallada.
* `hidden`: `true` para ocultar de la documentación.

### `@ApiResponse` / `@ApiResponses`
Describe las respuestas HTTP del endpoint.
* `responseCode`: Código HTTP (`"200"`, `"400"`, `"404"`, etc.).
* `description`: Explicación del resultado.
* `content`: Recibe `@Content` con el esquema retornado (`@Schema` o `@ArraySchema`).

#### Anotaciones secundarias:
* `@Content`: `mediaType` (`"application/json"`), `schema = @Schema(...)`, `array = @ArraySchema(...)`.
* `@ArraySchema`: `schema = @Schema(...)` cuando devuelve una lista.

### `@Parameter`
Documenta un parámetro de ruta (`@PathVariable`) o consulta (`@RequestParam`).
* `name`: Nombre del parámetro.
* `description`: Explicación.
* `required`: true / false.
* `example`: Valor de ejemplo.

### `@RequestBody` *(io.swagger.v3.oas.annotations.parameters.RequestBody)*
Documenta el cuerpo de la petición.
* `description`: Explicación del cuerpo requerido.
* `required`: true / false.

---

## 4. Nivel DTO y Atributos

### `@Schema`
Se usa tanto en la clase DTO como en sus campos.

* En Clase DTO:
  * `description`: Qué representa este objeto.
* En Campos/Atributos:
  * `description`: Propósito del campo.
  * `example`: Valor de muestra (`"123"`, `"Juan"`).
  * `requiredMode`: `Schema.RequiredMode.REQUIRED` / `NOT_REQUIRED`.
  * `accessMode`: `Schema.AccessMode.READ_ONLY` / `WRITE_ONLY`.

---

## 5. Ejemplo de Código

### Configuración Global (`OpenApiConfig.java`)

```java
package com.ejemplo.config;

import io.swagger.v3.oas.annotations.OpenAPIDefinition;
import io.swagger.v3.oas.annotations.enums.SecuritySchemeType;
import io.swagger.v3.oas.annotations.info.Info;
import io.swagger.v3.oas.annotations.security.SecurityScheme;
import io.swagger.v3.oas.annotations.servers.Server;
import org.springframework.context.annotation.Configuration;

@Configuration
@OpenAPIDefinition(
    info = @Info(title = "API de Productos", version = "1.0", description = "Gestión de catálogo"),
    servers = @Server(url = "http://localhost:8080", description = "Servidor Local")
)
@SecurityScheme(
    name = "bearerAuth",
    type = SecuritySchemeType.HTTP,
    scheme = "bearer",
    bearerFormat = "JWT"
)
public class OpenApiConfig {}
```

### DTOs (`ProductoRequestDTO.java` y `ProductoResponseDTO.java`)

```java
package com.ejemplo.dto;

import io.swagger.v3.oas.annotations.media.Schema;
import java.math.BigDecimal;

@Schema(description = "Datos de entrada para crear un producto")
public record ProductoRequestDTO(
    @Schema(description = "Nombre comercial", example = "Teclado RGB", requiredMode = Schema.RequiredMode.REQUIRED)
    String nombre,

    @Schema(description = "Precio unitario", example = "49.99", requiredMode = Schema.RequiredMode.REQUIRED)
    BigDecimal precio
) {}
```

```java
package com.ejemplo.dto;

import io.swagger.v3.oas.annotations.media.Schema;
import java.math.BigDecimal;

@Schema(description = "Datos de salida de un producto")
public record ProductoResponseDTO(
    @Schema(description = "ID asignado", example = "1", accessMode = Schema.AccessMode.READ_ONLY)
    Long id,

    @Schema(description = "Nombre comercial", example = "Teclado RGB")
    String nombre,

    @Schema(description = "Precio unitario", example = "49.99")
    BigDecimal precio
) {}
```

### Controlador (`ProductoController.java`)

```java
package com.ejemplo.controller;

import com.ejemplo.dto.ProductoRequestDTO;
import com.ejemplo.dto.ProductoResponseDTO;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.Parameter;
import io.swagger.v3.oas.annotations.media.Content;
import io.swagger.v3.oas.annotations.media.Schema;
import io.swagger.v3.oas.annotations.responses.ApiResponse;
import io.swagger.v3.oas.annotations.responses.ApiResponses;
import io.swagger.v3.oas.annotations.security.SecurityRequirement;
import io.swagger.v3.oas.annotations.tags.Tag;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/productos")
@Tag(name = "Productos", description = "Operaciones del catálogo")
@SecurityRequirement(name = "bearerAuth")
public class ProductoController {

    @GetMapping("/{id}")
    @Operation(summary = "Obtener producto por ID", description = "Retorna un producto según su ID")
    @ApiResponses({
        @ApiResponse(responseCode = "200", description = "Encontrado", 
            content = @Content(schema = @Schema(implementation = ProductoResponseDTO.class))),
        @ApiResponse(responseCode = "404", description = "No encontrado", content = @Content)
    })
    public ResponseEntity<ProductoResponseDTO> obtenerPorId(
        @Parameter(description = "ID del producto", example = "1", required = true)
        @PathVariable Long id
    ) {
        return ResponseEntity.ok(new ProductoResponseDTO(id, "Teclado RGB", new java.math.BigDecimal("49.99")));
    }

    @PostMapping
    @Operation(summary = "Crear producto", description = "Crea un nuevo producto en el catálogo")
    @ApiResponse(responseCode = "201", description = "Creado exitosamente")
    public ResponseEntity<ProductoResponseDTO> crear(
        @io.swagger.v3.oas.annotations.parameters.RequestBody(description = "Datos del producto a crear", required = true)
        @RequestBody ProductoRequestDTO request
    ) {
        return ResponseEntity.status(HttpStatus.CREATED)
                .body(new ProductoResponseDTO(1L, request.nombre(), request.precio()));
    }
}
```