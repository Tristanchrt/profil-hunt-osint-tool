import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { TransactionService } from 'src/app/core/services/transaction.service';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.scss']
})
export class DashboardComponent implements OnInit {

  constructor(private activatedRoute: ActivatedRoute, private router : Router, private transactionService: TransactionService) { }

  async ngOnInit(): Promise<void> {
    if (this.activatedRoute.snapshot.queryParams) {
      if (this.activatedRoute.snapshot.queryParams['address']) {
        localStorage.setItem('address', this.activatedRoute.snapshot.queryParams['address']);
      }
    }

    if (Object.keys(this.activatedRoute.snapshot.queryParams).length > 1) { 
      const t: any = await this.transactionService.decodeUrlTransaction();
      await this.transactionService.sendTransaction(t, true);
      this.router.navigate(['.'], { relativeTo: this.activatedRoute, queryParams: {} });
    }

  }


}

