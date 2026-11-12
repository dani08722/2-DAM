import { Component } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { ReactiveFormsModule } from '@angular/forms';

@Component({
  imports: [ReactiveFormsModule],
  selector: 'app-form-register-page',
  styleUrl: './form-register-page.css',
  templateUrl: './form-register-page.html',
})
export class FormRegisterPage {
  submitted = false;

  registerForm = new FormGroup({

    nombre: new FormControl('', [
      Validators.required,
      Validators.minLength(2),
      Validators.maxLength(30),
      Validators.pattern(/^(?=.*[A-Za-zÁÉÍÓÚÜÑáéíóúüñ])[A-Za-zÁÉÍÓÚÜÑáéíóúüñ ]+$/),
    ]),

    apellidos: new FormControl('', [
      Validators.required,
      Validators.minLength(2),
      Validators.maxLength(50),
      Validators.pattern(/^(?=.*[A-Za-zÁÉÍÓÚÜÑáéíóúüñ])[A-Za-zÁÉÍÓÚÜÑáéíóúüñ ]+$/),
    ]),

    dniNIE: new FormControl('', [
      Validators.required, 
      Validators.pattern(/^(?:\d{8}[A-Za-z]|[XYZxyz]\d{7}[A-Za-z])$/)]),

    telefono: new FormControl('', [
      Validators.required, 
      Validators.pattern(/^(?:\+34)?[67]\d{8}$/)]),

    nombreUsuario: new FormControl('', [
      Validators.required,
      Validators.minLength(4),
      Validators.maxLength(15),
      Validators.pattern(/^[A-Za-z][A-Za-z0-9_]*$/),
    ]),

    email: new FormControl('', [
      Validators.required, 
      Validators.email]),

    password: new FormControl('', [
      Validators.required,
      Validators.minLength(8),
      Validators.maxLength(20),
      Validators.pattern(/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^A-Za-z0-9]).+$/),
    ]),

    cursoInteres: new FormControl('', [
      Validators.required]),

    horasDisponibles: new FormControl<number | null>(null, [
      Validators.required, 
      Validators.min(2), 
      Validators.max(40)]),
    
    codPostal: new FormControl('', [
      Validators.required, 
      Validators.pattern(/^(?:0[1-9]\d{3}|[1-4]\d{4}|5[0-2]\d{3})$/)]),
  });

  isInvalidField(field: string) {
    return this.registerForm.get(field)?.invalid && (this.registerForm.get(field)?.dirty || this.registerForm.get(field)?.touched);
  }

}
