import { ResearchComponent } from './research/research.component';
import { ResearchListComponent } from './research-list/research-list.component';
import { FirstLastNameComponent } from './first-last-name/first-last-name.component';
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DashboardComponent } from './dashboard.component';
import { ProfilComponent } from './profil/profil.component';

const routes: Routes = [
  {
    path: "",
    component: DashboardComponent,
    children: [
      {
        path: "profil",
        component: ProfilComponent
      },
      {
        path: "first-last-name",
        component: FirstLastNameComponent
      },
      {
        path: "research-list",
        component: ResearchListComponent
      },
      {
        path: "research/:id",
        component: ResearchComponent
      },
    ]
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class DashboardRoutingModule { }
