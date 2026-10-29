import {
  ApplicationConfig,
  provideBrowserGlobalErrorListeners,
  importProvidersFrom,
} from '@angular/core';
import { provideRouter } from '@angular/router';
import { routes } from './app.routes';
<<<<<<< HEAD
import { provideClientHydration } from '@angular/platform-browser';
=======
>>>>>>> 489f18378362a303a27d9043d4d0df54611ad4ca
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';

export const appConfig: ApplicationConfig = {
  providers: [
    provideBrowserGlobalErrorListeners(),
    provideRouter(routes),
<<<<<<< HEAD
    provideClientHydration(),
=======
>>>>>>> 489f18378362a303a27d9043d4d0df54611ad4ca
    importProvidersFrom(NgbModule),
  ],
};
