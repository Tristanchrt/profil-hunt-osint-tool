import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { NZ_I18N } from 'ng-zorro-antd/i18n';
import { en_US } from 'ng-zorro-antd/i18n';
import { registerLocaleData } from '@angular/common';
import en from '@angular/common/locales/en';
import { FormsModule } from '@angular/forms';
import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { NzCardModule } from 'ng-zorro-antd/card';
import { NzInputModule } from 'ng-zorro-antd/input';
import { NzButtonModule } from 'ng-zorro-antd/button';
import { HomeComponent } from './pages/home/home.component';
import { HeaderComponent } from './shared/header/header.component';
import { PriceComponent } from './pages/price/price.component';
import { AboutComponent } from './pages/about/about.component';
import { QRCodeModule } from 'angularx-qrcode';
import { LoginComponent } from './pages/login/login.component';
import { NzIconModule } from 'ng-zorro-antd/icon';
import { HttpTokenInterceptor } from './core/interceptors/http.token.interceptor';
import { NzMessageModule } from 'ng-zorro-antd/message';
import { DashboardComponent } from './pages/dashboard/dashboard.component';
import { NzLayoutModule } from 'ng-zorro-antd/layout';
import { SidebarComponent } from './shared/sidebar/sidebar.component';
import { NzDropDownModule } from 'ng-zorro-antd/dropdown';
import { NzListModule } from 'ng-zorro-antd/list';
import { NzGraphModule } from 'ng-zorro-antd/graph';
import { NzModalModule } from 'ng-zorro-antd/modal';
import { ServiceWorkerModule } from '@angular/service-worker';
import { environment } from '../environments/environment';
import { TransactionModalSuccessComponent } from './shared/component/modal/transaction-modal-success/transaction-modal-success.component';
import { TransactionModalFailedComponent } from './shared/component/modal/transaction-modal-failed/transaction-modal-failed.component';
import { TransactionModalWaitingComponent } from './shared/component/modal/transaction-modal-waiting/transaction-modal-waiting.component';
import { NzProgressModule } from 'ng-zorro-antd/progress';
import { NzSpinModule } from 'ng-zorro-antd/spin';
import { NzPaginationModule } from 'ng-zorro-antd/pagination';
import { LottieModule } from 'ngx-lottie';
import player from 'lottie-web';
import { NzAlertModule } from 'ng-zorro-antd/alert';
import { NotfoundComponent } from './shared/component/notfound/notfound.component';
import { NzResultModule } from 'ng-zorro-antd/result';
import { ForbiddenComponent } from './shared/component/forbidden/forbidden.component';
import { NzRadioModule } from 'ng-zorro-antd/radio';
import { NzNotificationModule } from 'ng-zorro-antd/notification';


registerLocaleData(en);
export function playerFactory() {
  return player;
}
@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    HeaderComponent,
    PriceComponent,
    AboutComponent,
    LoginComponent,
    DashboardComponent,
    SidebarComponent,
    TransactionModalSuccessComponent,
    TransactionModalFailedComponent,
    TransactionModalWaitingComponent,
    NotfoundComponent,
    ForbiddenComponent,

  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule,
    BrowserAnimationsModule,
    NzCardModule,
    NzInputModule,
    NzButtonModule,
    QRCodeModule,
    NzIconModule,
    NzMessageModule,
    NzLayoutModule,
    NzDropDownModule,
    NzListModule,
    NzGraphModule,
    NzModalModule,
    NzSpinModule,
    NzAlertModule,
    NzProgressModule,
    NzResultModule,
    NzRadioModule,
    NzNotificationModule,
    NzPaginationModule,
    LottieModule.forRoot({ player: playerFactory }),
    ServiceWorkerModule.register('ngsw-worker.js', {
      enabled: environment.production,
      // Register the ServiceWorker as soon as the application is stable
      // or after 30 seconds (whichever comes first).
      registrationStrategy: 'registerWhenStable:30000'
    })
  ],
  providers: [
    { provide: NZ_I18N, useValue: en_US },
    { provide: HTTP_INTERCEPTORS, useClass: HttpTokenInterceptor, multi: true }
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
