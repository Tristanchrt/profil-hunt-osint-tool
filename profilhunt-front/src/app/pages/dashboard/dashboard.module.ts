import { ProfilComponent } from './profil/profil.component';
import { FormsModule } from '@angular/forms';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { DashboardRoutingModule } from "./dashboard-routing.module";
import { NzLayoutModule } from 'ng-zorro-antd/layout';
import { FirstLastNameComponent } from './first-last-name/first-last-name.component';
import { NzButtonModule } from 'ng-zorro-antd/button';
import { NzInputModule } from 'ng-zorro-antd/input';
import { NzResultModule } from 'ng-zorro-antd/result';
import { ResearchListComponent } from './research-list/research-list.component';
import { NzListModule } from 'ng-zorro-antd/list';
import { NzTagModule } from 'ng-zorro-antd/tag';
import { ResearchComponent } from './research/research.component';
import { NzGraphModule } from 'ng-zorro-antd/graph';
import { NzModalModule } from 'ng-zorro-antd/modal';
import { NzImageModule } from 'ng-zorro-antd/image';
import { NzToolTipModule } from 'ng-zorro-antd/tooltip';
import { NzIconModule } from 'ng-zorro-antd/icon';
import { GraphComponent } from 'src/app/shared/component/graph/graph.component';
import { NzPaginationModule } from 'ng-zorro-antd/pagination';
import { NzSpinModule } from 'ng-zorro-antd/spin';
import { NzSkeletonModule } from 'ng-zorro-antd/skeleton';
import { NzEmptyModule } from 'ng-zorro-antd/empty';
import { LottieModule } from 'ngx-lottie';
import player from 'lottie-web';
import { NzRadioModule } from 'ng-zorro-antd/radio';

@NgModule({
  declarations: [
    FirstLastNameComponent,
    ProfilComponent,
    ResearchListComponent,
    ResearchComponent,
    GraphComponent,
    ResearchComponent
  ],
  imports: [
    CommonModule,
    DashboardRoutingModule,
    NzLayoutModule,
    FormsModule,
    NzButtonModule,
    NzInputModule,
    NzResultModule,
    NzListModule,
    NzTagModule,
    NzGraphModule,
    NzModalModule,
    NzImageModule,
    NzToolTipModule,
    NzSpinModule,
    NzSkeletonModule,
    NzIconModule,
    NzEmptyModule,
    NzPaginationModule,
    NzRadioModule,
    LottieModule,
  ],
})
export class DashboardModule { }
