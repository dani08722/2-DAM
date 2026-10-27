import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';

@Component({
  imports: [FormsModule],
  selector: 'app-formulario-component',
  styleUrl: './formulario-component.css',
  templateUrl: './formulario-component.html',
})
export class FormularioComponent {

  nombreForm = 'Daniel';
  apellidosForm = 'Mejias Lora';
  nifForm = '12345678A';
  emailForm = 'daniel.mejias@example.com';
  telefonoForm = '123456789';
  sexoForm = 'Hombre';
  passwordForm = 'password123';
  passwordConfirmForm = 'password123';

  sendForm() {
  console.log(this.emailForm, this.nombreForm, this.apellidosForm, this.nifForm, 
    this.telefonoForm, this.sexoForm, this.passwordForm, this.passwordConfirmForm);
  }
}
