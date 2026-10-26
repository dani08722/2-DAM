# Manual de anotaciones OpenAPI para Spring Boot

Este manual recoge las anotaciones más habituales de **Swagger Core**, utilizadas normalmente a través de **springdoc-openapi**, para describir una API REST implementada con Spring Boot. OpenAPI genera la especificación y la interfaz de Swagger UI a partir de estas anotaciones y de las rutas de Spring MVC.

Las anotaciones de Swagger pertenecen a `io.swagger.v3.oas.annotations`. No sustituyen a las anotaciones de Spring que definen el comportamiento HTTP (`@RestController`, `@GetMapping`, `@PathVariable`, etc.): se complementan con ellas.

## Dependencia habitual

En una aplicación Spring Boot MVC se suele añadir el starter de Swagger UI de springdoc. La versión debe elegirse de acuerdo con la versión de Spring Boot del proyecto:

```xml
<dependency>
	<groupId>org.springdoc</groupId>
	<artifactId>springdoc-openapi-starter-webmvc-ui</artifactId>
	<version>${springdoc.version}</version>
</dependency>
```

Por defecto, springdoc publica la especificación en `/v3/api-docs` y Swagger UI en `/swagger-ui.html` (que normalmente redirige a la interfaz).

## 1. A nivel de toda la API

### `@OpenAPIDefinition`

Se coloca sobre una clase de configuración para definir información y valores comunes a toda la especificación.

**Atributos principales:**

| Atributo | Descripción |
| --- | --- |
| `info` | Metadatos de la API; recibe un `@Info`. |
| `servers` | Servidores donde se ofrece la API; recibe un array de `@Server`. |
| `security` | Requisitos de seguridad globales; recibe un array de `@SecurityRequirement`. |
| `tags` | Etiquetas disponibles para agrupar operaciones; recibe un array de `@Tag`. |
| `externalDocs` | Enlace a documentación externa; recibe un `@ExternalDocumentation`. |
| `webhooks` | Declaraciones de webhooks, cuando la versión de Swagger Core utilizada las admite. |
| `extensions` | Extensiones OpenAPI específicas del proveedor; recibe un array de `@Extension`. |

Anotaciones que pueden aparecer dentro de `@OpenAPIDefinition`:

- **`@Info`**: metadatos descriptivos. Sus atributos son `title`, `description`, `termsOfService`, `version`, `contact` (`@Contact`), `license` (`@License`) y `extensions` (`@Extension[]`).
- **`@Contact`**: datos de contacto. Incluye `name`, `url`, `email` y `extensions`.
- **`@License`**: licencia de la API. Incluye `name`, `url`, `identifier` y `extensions`.
- **`@Server`**: dirección de un servidor. Incluye `url`, `description`, `variables` (`@ServerVariable[]`) y `extensions`.
- **`@ServerVariable`**: variable de una URL de servidor. Incluye `name`, `defaultValue`, `allowableValues`, `description` y `extensions`.
- **`@SecurityRequirement`**: nombre del esquema de seguridad declarado y, para OAuth2/OpenID Connect, sus `scopes`.
- **`@Tag`**: grupo de operaciones con `name`, `description`, `externalDocs` (`@ExternalDocumentation`) y `extensions`.
- **`@ExternalDocumentation`**: documentación externa con `description`, `url` y `extensions`.
- **`@Extension`**: extensión del proveedor con `name` y `properties` (`@ExtensionProperty[]`). `parseValue` indica si se debe interpretar el valor de la propiedad como JSON. **`@ExtensionProperty`** contiene `name`, `value` y `parseValue`.

Ejemplo:

```java
@Configuration
@OpenAPIDefinition(
	info = @Info(
		title = "API de biblioteca",
		version = "1.0.0",
		description = "Operaciones para gestionar libros",
		contact = @Contact(name = "Equipo de desarrollo", email = "api@ejemplo.com"),
		license = @License(name = "Apache 2.0", url = "https://www.apache.org/licenses/LICENSE-2.0")
	),
	servers = @Server(url = "https://api.ejemplo.com", description = "Producción")
)
public class OpenApiConfig {
}
```

### Seguridad global: `@SecurityScheme` y `@SecuritySchemes`

`@SecurityScheme` registra un mecanismo de autenticación para que pueda referenciarse desde `@SecurityRequirement`. `@SecuritySchemes` permite declarar varios esquemas en una misma ubicación. Su atributo `value` es un array de `@SecurityScheme`.

**Atributos habituales de `@SecurityScheme`:** `name` (identificador usado al referenciarlo), `type` (`HTTP`, `APIKEY`, `OAUTH2`, `OPENIDCONNECT`), `description`, `in` (ubicación de una API key: `HEADER`, `QUERY` o `COOKIE`), `scheme` (por ejemplo `bearer` o `basic`), `bearerFormat` (por ejemplo `JWT`), `paramName` (nombre del parámetro de API key), `openIdConnectUrl`, `flows` (`@OAuthFlows`), `ref` y `extensions`.

Anotaciones anidadas para OAuth2:

- **`@OAuthFlows`**: define uno o varios flujos mediante `implicit`, `password`, `clientCredentials` y `authorizationCode` (cada uno es un `@OAuthFlow`), además de `extensions`.
- **`@OAuthFlow`**: contiene `authorizationUrl`, `tokenUrl`, `refreshUrl`, `scopes` (`@OAuthScope[]`) y `extensions`.
- **`@OAuthScope`**: describe un permiso OAuth con `name` y `description`.

Ejemplo de autenticación Bearer JWT:

```java
@Configuration
@SecurityScheme(
	name = "bearerAuth",
	type = SecuritySchemeType.HTTP,
	scheme = "bearer",
	bearerFormat = "JWT"
)
public class OpenApiConfig {
}
```

La declaración del esquema no obliga por sí sola a todas las operaciones a usarlo. Para aplicar la seguridad global puede añadirse `security = @SecurityRequirement(name = "bearerAuth")` a `@OpenAPIDefinition`; también se puede aplicar solo a ciertos controladores u operaciones.

## 2. A nivel de controlador

### `@Tag`

Agrupa las operaciones del controlador bajo una categoría en Swagger UI. Se puede colocar en la clase o en una operación.

**Atributos:** `name` (nombre del grupo), `description`, `externalDocs` (`@ExternalDocumentation`) y `extensions` (`@Extension[]`).

```java
@RestController
@RequestMapping("/api/libros")
@Tag(name = "Libros", description = "Consulta y mantenimiento del catálogo")
public class LibroController {
	// Endpoints...
}
```

### `@SecurityRequirement`

Asocia el controlador completo al esquema de seguridad declarado con `@SecurityScheme`. Sus atributos son `name` y `scopes` (permisos OAuth requeridos). Si se especifica en la clase, se aplica a sus operaciones; una operación puede declarar su propio requisito.

```java
@RestController
@RequestMapping("/api/libros")
@SecurityRequirement(name = "bearerAuth")
public class LibroController {
}
```

### `@Hidden`

Oculta el controlador completo de la documentación OpenAPI. No desactiva ni protege sus rutas en la aplicación.

## 3. A nivel de endpoint

### `@Operation`

Describe una operación HTTP. Se coloca sobre un método del controlador.

**Atributos habituales:**

| Atributo | Descripción |
| --- | --- |
| `summary`, `description` | Resumen breve y explicación detallada. |
| `operationId` | Identificador único de la operación. |
| `tags` | Nombres de los grupos asignados a la operación. |
| `parameters` | Parámetros adicionales o documentados explícitamente; array de `@Parameter`. |
| `requestBody` | Descripción del cuerpo de la petición; `@RequestBody`. |
| `responses` | Respuestas posibles; array de `@ApiResponse`. |
| `security` | Requisitos de seguridad de esta operación; array de `@SecurityRequirement`. |
| `servers` | Servidores específicos para esta operación; array de `@Server`. |
| `externalDocs` | Documentación externa; `@ExternalDocumentation`. |
| `deprecated` | Marca la operación como obsoleta. |
| `hidden` | Excluye la operación de la especificación. |
| `callbacks` | Callbacks asociados; array de `@Callback`. |
| `extensions`, `ref`, `method` | Extensiones, referencia externa y método HTTP explícito, respectivamente. |

### `@ApiResponses` y `@ApiResponse`

`@ApiResponses` agrupa las respuestas de una operación; su atributo `value` es un array de `@ApiResponse`. También se puede declarar una única respuesta con `@ApiResponse` directamente.

**Atributos de `@ApiResponse`:** `responseCode` (código HTTP o `default`), `description`, `headers` (`@Header[]`), `content` (`@Content[]`), `links` (`@Link[]`), `extensions`, `ref` y `useReturnTypeSchema` (usa el tipo de retorno del método como esquema cuando corresponda).

Anotaciones anidadas frecuentes:

- **`@Content`**: tipo de contenido de la respuesta o petición. Incluye `mediaType`, `schema` (`@Schema`), `array` (`@ArraySchema`), `examples` (`@ExampleObject[]`), `encoding` (`@Encoding[]`) y `extensions`.
- **`@Header`**: cabecera de respuesta. Incluye `name`, `description`, `required`, `deprecated`, `schema` (`@Schema`), `examples`, `content` y `extensions`.
- **`@ExampleObject`**: ejemplo con `name`, `summary`, `description`, `value` (contenido del ejemplo), `externalValue` (URL a un ejemplo externo), `ref`, `extensions` y `mediaType`.
- **`@Link`**: enlace a otra operación. Incluye `name`, `operationId` o `operationRef`, `parameters` (`@LinkParameter[]`), `requestBody`, `description`, `server` (`@Server`), `ref` y `extensions`. **`@LinkParameter`** asocia un `name` con una expresión o valor mediante `expression`.
- **`@Encoding`**: codificación de una propiedad de un cuerpo, especialmente `multipart/form-data`. Incluye `name`, `contentType`, `style`, `explode`, `allowReserved`, `headers` (`@Header[]`) y `extensions`.

### `@Parameter` y `@Parameters`

`@Parameter` documenta un parámetro de ruta, consulta, cabecera o cookie. Puede colocarse en el método o junto a un parámetro Java. `@Parameters` agrupa varios y su atributo `value` es un array de `@Parameter`.

**Atributos habituales de `@Parameter`:** `name`, `description`, `in` (ubicación: `PATH`, `QUERY`, `HEADER`, `COOKIE`), `required`, `deprecated`, `allowEmptyValue`, `allowReserved`, `style`, `explode`, `schema` (`@Schema`), `array` (`@ArraySchema`), `content` (`@Content[]`), `example`, `examples` (`@ExampleObject[]`), `hidden`, `ref` y `extensions`.

Los parámetros `@PathVariable` son obligatorios por definición. Para parámetros `@RequestParam` opcionales, `required = false` debe coincidir con el comportamiento real del controlador.

### `@RequestBody` de Swagger

`io.swagger.v3.oas.annotations.parameters.RequestBody` describe el cuerpo de una petición en OpenAPI. **No es** `org.springframework.web.bind.annotation.RequestBody`, que es la anotación de Spring MVC que hace que el framework lea el cuerpo HTTP y lo convierta en un objeto.

**Atributos:** `description`, `required`, `content` (`@Content[]`), `extensions` y `ref`.

Normalmente se usa dentro de `@Operation`; la anotación de Spring se mantiene en el parámetro Java:

```java
@Operation(
	summary = "Crear un libro",
	requestBody = @io.swagger.v3.oas.annotations.parameters.RequestBody(
		required = true,
		description = "Datos del libro que se va a crear",
		content = @Content(schema = @Schema(implementation = LibroAltaDTO.class))
	),
	responses = {
		@ApiResponse(responseCode = "201", description = "Libro creado"),
		@ApiResponse(responseCode = "400", description = "Datos no válidos")
	}
)
@PostMapping
public ResponseEntity<LibroDTO> crear(
	@org.springframework.web.bind.annotation.RequestBody LibroAltaDTO datos) {
	// Implementación...
}
```

### `@Hidden` en una operación o parámetro

Oculta el elemento correspondiente de la documentación. No cambia el comportamiento HTTP de la aplicación.

## 4. A nivel de DTO y sus atributos

### `@Schema`

Describe un objeto o una propiedad del modelo. Se coloca sobre una clase DTO, un campo o un getter.

**Atributos de uso frecuente:**

| Atributo | Descripción |
| --- | --- |
| `name`, `title`, `description` | Nombre, título y explicación del esquema o propiedad. |
| `type`, `format` | Tipo OpenAPI y formato, por ejemplo `string` y `date-time`. |
| `example`, `defaultValue` | Ejemplo y valor predeterminado. |
| `allowableValues` | Valores permitidos, útil para enumeraciones. |
| `requiredMode` | Indica si es obligatorio (`REQUIRED`, `NOT_REQUIRED` o `AUTO`). |
| `accessMode` | Acceso (`READ_ONLY`, `WRITE_ONLY` o `READ_WRITE`). |
| `nullable`, `deprecated`, `hidden` | Nulabilidad, obsolescencia u ocultación de la propiedad. |
| `implementation`, `ref` | Tipo de implementación o referencia de esquema. |
| `minimum`, `maximum`, `exclusiveMinimum`, `exclusiveMaximum`, `multipleOf` | Restricciones numéricas. |
| `minLength`, `maxLength`, `pattern` | Restricciones de cadenas. |
| `minItems`, `maxItems`, `uniqueItems` | Restricciones de listas. |
| `minProperties`, `maxProperties` | Restricciones del número de propiedades. |
| `oneOf`, `anyOf`, `allOf` | Composición con otros tipos Java. |
| `discriminatorProperty`, `discriminatorMapping` | Discriminador para modelos polimórficos; `discriminatorMapping` recibe `@DiscriminatorMapping[]`. |
| `externalDocs`, `extensions` | Documentación externa (`@ExternalDocumentation`) y extensiones (`@Extension[]`). |

Swagger Core incorpora más atributos para casos avanzados, por ejemplo `accessMode`, composiciones, validaciones y metadatos de serialización. Para los campos normales de un DTO, los más usados suelen ser `description`, `example`, `requiredMode`, `allowableValues` y las restricciones de longitud o rango.

### `@ArraySchema`

Describe una propiedad que es un array o colección. Sus atributos habituales son `schema` (`@Schema` para los elementos), `arraySchema` (`@Schema` para el propio array), `minItems`, `maxItems`, `uniqueItems`, `contains` (`@Schema`), `deprecated`, `hidden`, `ref` y `extensions`.

Se utiliza en vez de `@Schema` cuando es necesario documentar por separado la colección y el esquema de sus elementos.

Ejemplo de DTO:

```java
@Schema(description = "Información de un libro del catálogo")
public class LibroDTO {

	@Schema(description = "Identificador único", example = "42", accessMode = Schema.AccessMode.READ_ONLY)
	private Long id;

	@Schema(description = "Título del libro", example = "El camino", minLength = 1, maxLength = 150,
			requiredMode = Schema.RequiredMode.REQUIRED)
	private String titulo;

	@Schema(description = "Estado del libro", allowableValues = {"DISPONIBLE", "PRESTADO"},
			example = "DISPONIBLE")
	private String estado;

	@ArraySchema(
		schema = @Schema(description = "Etiqueta", example = "novela"),
		arraySchema = @Schema(description = "Etiquetas asociadas al libro"),
		maxItems = 10
	)
	private List<String> etiquetas;

	// Constructores, getters y setters...
}
```

## 5. Ejemplo conjunto

El siguiente fragmento muestra cómo conviven las anotaciones de Spring MVC y las de OpenAPI:

```java
@RestController
@RequestMapping("/api/libros")
@Tag(name = "Libros", description = "Gestión del catálogo")
@SecurityRequirement(name = "bearerAuth")
public class LibroController {

	@Operation(summary = "Buscar libros", description = "Filtra el catálogo por texto")
	@ApiResponses({
		@ApiResponse(responseCode = "200", description = "Resultados encontrados",
			content = @Content(mediaType = "application/json",
				array = @ArraySchema(schema = @Schema(implementation = LibroDTO.class)))),
		@ApiResponse(responseCode = "400", description = "Parámetro de búsqueda no válido")
	})
	@GetMapping
	public List<LibroDTO> buscar(
		@Parameter(description = "Texto que se buscará en el título", example = "camino")
		@RequestParam(required = false) String texto) {
		// Implementación...
		return List.of();
	}
}
```

## 6. Recomendaciones

- Documenta los códigos HTTP que realmente devuelve cada operación; evita declarar respuestas que la implementación no produce.
- Usa `@Operation` para el resumen y la descripción, y `@ApiResponse` para explicar cada resultado.
- Prefiere DTOs de entrada y salida explícitos. `@Schema(accessMode = READ_ONLY)` o `WRITE_ONLY` ayuda a describir campos de solo lectura o escritura.
- No confundas una anotación documental (`@Hidden`, `@Schema`) con controles de seguridad o validación. La autorización corresponde a Spring Security y la validación, por ejemplo, a Jakarta Bean Validation (`@NotNull`, `@Size`).
- Las anotaciones `@Schema` no sustituyen a las validaciones del servidor: documenta restricciones que también se hagan cumplir en la aplicación.
- La disponibilidad exacta de algunos atributos depende de la versión de Swagger Core que incorpore springdoc.
        