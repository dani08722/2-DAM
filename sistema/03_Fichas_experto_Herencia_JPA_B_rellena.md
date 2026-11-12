# Ficha de experto B

Herencia en JPA · JOINED

Nombre: __________________________________  Grupo base: __________

Lee, resuelve y prepara tu explicación. Dispones de 12 minutos con los expertos y de 4 minutos para enseñar esta opción a tu grupo base.

## 1. Comprende la idea

Los atributos comunes se guardan en la tabla base y los específicos en la tabla del subtipo. Un mismo objeto ocupa una fila en cada una de esas dos tablas, unidas por su identificador.

## 2. Examina el código

Fragmentos de tres archivos distintos. Se omiten imports de `jakarta.persistence` y métodos de acceso. Los ids se asignan manualmente para centrar el trabajo en el mapeo.

```java
@Entity
@Table(name = "contenido")
@Inheritance(strategy = InheritanceType.JOINED)
public abstract class Contenido {
    @Id
    protected Long id;
    protected String titulo;
}

@Entity
@Table(name = "pelicula")
public class Pelicula extends Contenido {
    @Column(name = "duracion_minutos")
    private Integer duracionMinutos;
}

@Entity
@Table(name = "serie")
public class Serie extends Contenido {
    @Column(name = "numero_temporadas")
    private Integer numeroTemporadas;
}
```

## 3. Relaciona el mapeo con las consultas

`Contenido` es una entidad. Un repositorio `JpaRepository<Contenido, Long>` permite recuperar películas y series mediante `findAll()`. Hibernate combina la tabla base con las tablas de subtipos mediante `JOIN` para recuperar su estado.

Pista para decidir. El id de cada tabla de subtipo es a la vez PK y FK hacia `contenido`. Los atributos específicos pueden tener restricciones `NOT NULL` en su tabla. Recuperar objetos completos puede requerir varias uniones.

_Referencia de apoyo: Hibernate ORM User Guide, apartado 3.14 sobre herencia. JPA define el mapeo; Hibernate lo implementa; Spring Data JPA facilita los repositorios._

# Ficha B de trabajo

JOINED · Completa y lleva esta página al grupo base

## 4. Dibuja y sitúa los datos

Datos: `Pelicula (id=1, titulo="Órbita", duracionMinutos=120)` y `Serie (id=2, titulo="Horizonte", numeroTemporadas=3)`.

| **Tabla** | **Columnas completas** |
|---|---|
| `contenido` | `id` (PK), `titulo` |
| `pelicula` | `id` (PK y FK a `contenido.id`), `duracion_minutos` |
| `serie` | `id` (PK y FK a `contenido.id`), `numero_temporadas` |

**Filas de ejemplo**

```text
contenido
id (PK) | titulo
1       | Órbita
2       | Horizonte

pelicula
id (PK, FK → contenido.id) | duracion_minutos
1                          | 120

serie
id (PK, FK → contenido.id) | numero_temporadas
2                          | 3
```

Órbita se representa con dos filas: una en `contenido` y otra en `pelicula`, relacionadas por `id = 1`. Horizonte también se representa con dos filas: una en `contenido` y otra en `serie`, relacionadas por `id = 2`. En estas tablas no hace falta guardar `NULL` para los atributos del otro subtipo.

## 5. Valora su aplicación práctica

**Anotación principal y función:** `@Inheritance(strategy = InheritanceType.JOINED)` indica que los atributos comunes van en la tabla de la entidad base y los atributos específicos en las tablas de cada subtipo. El id de cada subtipo es PK y también FK a `contenido.id`.

**Ventaja y situación en la que elegiríamos esta opción:** Evita repetir los atributos comunes y permite definir restricciones, como `NOT NULL`, para los atributos específicos en sus tablas. Puede convenir cuando cada subtipo tiene muchos atributos propios y se quieren imponer esas restricciones.

**Limitación o coste que debemos aceptar:** Para recuperar objetos completos, Hibernate puede tener que combinar varias tablas mediante `JOIN`. Esto hace más complejas o costosas las consultas, especialmente al recuperar muchos tipos de contenido.

## 6. Prepara tu explicación y comprueba

**Corrección de la afirmación «Con JOINED, el título de la película se repite en contenido y en pelicula»:** Es incorrecta. `titulo` se guarda una sola vez, en `contenido`. La tabla `pelicula` guarda el `id` como PK y FK a `contenido.id`, además de `duracion_minutos`. Hibernate combina ambas filas para reconstruir el objeto `Pelicula`.

**Pregunta para los compañeros:** ¿Basta con leer la tabla `pelicula` para recuperar también el título? **No.** `pelicula` contiene el id y la duración; hay que combinarla con `contenido` para obtener el título.

Antes de volver: todos debéis poder explicar el mapeo y sus consecuencias.
