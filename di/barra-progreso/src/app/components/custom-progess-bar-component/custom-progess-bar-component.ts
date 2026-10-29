import { Component, computed, input } from '@angular/core';

@Component({
  selector: 'app-custom-progress-bar',
  styleUrl: './custom-progess-bar-component.css',
  templateUrl: './custom-progess-bar-component.html',
})
export class CustomProgressBarComponent {
  value = input(0);
  color = input('primary');
  percentage = computed(() => Math.min(100, Math.max(0, this.value())));
}
