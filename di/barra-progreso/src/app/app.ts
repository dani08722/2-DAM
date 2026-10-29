import { Component, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { CustomProgressBarComponent } from './components/custom-progess-bar-component/custom-progess-bar-component';

@Component({
  imports: [CustomProgressBarComponent],
  selector: 'app-root',
  styleUrl: './app.css',
  templateUrl: './app.html',
})
export class App {
  protected readonly title = signal('barra-progreso');
}
