import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';


@Component({
  imports: [FormsModule],
  selector: 'app-formulario',
  styleUrl: './formulario.css',
  templateUrl: './formulario.html',
})
export class Formulario {
  nombreForm = 'Daniel'
  apellidosForm= 'Mejías Lora'
  nifForm= '12345678A'
  emailForm= 'daniel.mejias@alumno.edu'
  telefonoForm= '123456789'
  sexoForm= 'Hombre'
  conocidoPaginaForm= 'Buscando en Google'
  contraseniaForm= 'contraseña123'
  confirmarContraseniaForm= 'contraseña123'

  sendForm() {
    console.log('Nombre: ' + this.nombreForm);
    console.log('Apellidos: ' + this.apellidosForm);
    console.log('NIF: ' + this.nifForm);
    console.log('Email: ' + this.emailForm);
    console.log('Teléfono: ' + this.telefonoForm);
    console.log('Sexo: ' + this.sexoForm);
    console.log('Cómo conoció la página: ' + this.conocidoPaginaForm);
    console.log('Contraseña: ' + this.contraseniaForm);
    console.log('Confirmar Contraseña: ' + this.confirmarContraseniaForm);
  }
}
