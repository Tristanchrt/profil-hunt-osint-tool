import { ForbiddenComponent } from './shared/component/forbidden/forbidden.component';
import { NotfoundComponent } from './shared/component/notfound/notfound.component';
import { ProfilComponent } from './pages/dashboard/profil/profil.component';
import { LoginComponent } from './pages/login/login.component';
import { AboutComponent } from './pages/about/about.component';
import { PriceComponent } from './pages/price/price.component';
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './pages/home/home.component';
import { AuthGuardService } from './core/guards/auth-guard.service';
import { ResearchComponent } from './pages/dashboard/research/research.component';
import { ResearchListComponent } from './pages/dashboard/research-list/research-list.component';



const routes: Routes = [
  {
    path: "",
    component: HomeComponent,
    pathMatch: 'full'
  },
  {
    path: "price",
    component: PriceComponent,
    pathMatch: 'full'
  },
  {
    path: "about",
    component: AboutComponent,
    pathMatch: 'full'
  },
  {
    path: "dashboard",
    loadChildren: () => import("./pages/dashboard/dashboard.module").then(m => m.DashboardModule),
    canActivate: [AuthGuardService]
  },
  {
    path: "auth",
    children: [
      {
        path: "login",
        component: LoginComponent
      },
    ]
  },
  { path: '**', component: NotfoundComponent },
  { path: '403', component: ForbiddenComponent, pathMatch: 'full' },
  { path: '404', component: NotfoundComponent, pathMatch: 'full' },
];
@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
