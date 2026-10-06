var lista = document.getElementById("lista");
var mensaje = document.getElementById("mensaje");
var buscador = document.getElementById("buscador");
var detalle = document.getElementById("detalle");
var informacion = document.getElementById("informacion");
var pokemones = [];

// Pedimos los primeros 24 Pokémon a PokéAPI.
fetch("https://pokeapi.co/api/v2/pokemon?limit=24")
  .then(function(respuesta) { return respuesta.json(); })
  .then(function(datos) {
    var peticiones = datos.results.map(function(pokemon) {
      return fetch(pokemon.url).then(function(respuesta) { return respuesta.json(); });
    });
    return Promise.all(peticiones);
  })
  .then(function(datos) {
    pokemones = datos;
    mostrarPokemones(pokemones);
    mensaje.textContent = "";
  })
  .catch(function() { mensaje.textContent = "No se han podido cargar los Pokémon. Revisa tu conexión."; });

function mostrarPokemones(datos) {
  lista.innerHTML = "";
  datos.forEach(function(pokemon) {
    var tarjeta = document.createElement("article");
    tarjeta.className = "pokemon";
    tarjeta.innerHTML = '<img src="' + pokemon.sprites.front_default + '" alt="' + pokemon.name + '">' +
      '<div class="numero">N.º ' + pokemon.id + '</div><h3>' + pokemon.name + '</h3>';
    tarjeta.addEventListener("click", function() { mostrarDetalle(pokemon); });
    lista.appendChild(tarjeta);
  });
}

function mostrarDetalle(pokemon) {
  lista.hidden = true;
  buscador.hidden = true;
  document.querySelector("main > h2").hidden = true;
  detalle.hidden = false;
  informacion.innerHTML = '<img src="' + pokemon.sprites.front_default + '" alt="' + pokemon.name + '">' +
    '<h2>' + pokemon.name + '</h2>' +
    '<p><b>Número:</b> ' + pokemon.id + '</p>' +
    '<p><b>Tipo:</b> ' + pokemon.types.map(function(t) { return t.type.name; }).join(", ") + '</p>' +
    '<p><b>Altura:</b> ' + (pokemon.height / 10) + ' m</p>' +
    '<p><b>Peso:</b> ' + (pokemon.weight / 10) + ' kg</p>';
}

document.getElementById("volver").addEventListener("click", function() {
  detalle.hidden = true;
  lista.hidden = false;
  buscador.hidden = false;
  document.querySelector("main > h2").hidden = false;
});

buscador.addEventListener("input", function() {
  var texto = buscador.value.toLowerCase();
  mostrarPokemones(pokemones.filter(function(pokemon) { return pokemon.name.indexOf(texto) !== -1; }));
});
