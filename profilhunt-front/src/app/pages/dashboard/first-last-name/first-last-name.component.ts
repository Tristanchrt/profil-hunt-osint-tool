import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { NzMessageService } from 'ng-zorro-antd/message';
import { LogService } from 'src/app/core/services/log.service';
import { ModalService } from 'src/app/core/services/modal.service';
import { ScSearchService } from 'src/app/core/services/sc-search.service';
import { SearchService } from 'src/app/core/services/search.service';

@Component({
  selector: 'app-first-last-name',
  templateUrl: './first-last-name.component.html',
  styleUrls: ['./first-last-name.component.scss']
})
export class FirstLastNameComponent implements OnInit {

  constructor(private router: Router, private searchService: SearchService, private message: NzMessageService, private modalService: ModalService, private scSearchService: ScSearchService) { }

  fnValue?: string;
  lnValue?: string;
  paramsValue?: string;
  isLoadingOne = false;

  ngOnInit(): void {
  }

  async createTransaction(): Promise<any> {
    return await this.scSearchService.newSearch();
  }

  async startSearching() {
    if (this.fnValue && this.lnValue) {
      try {
        const val = await this.createTransaction()
        if (val.status == "success") {
          console.log('Data =>', val);
          const search: any = await this.searchService.postsearchFirstLastName(this.fnValue, this.lnValue, this.paramsValue);
          console.log('Address paid =>', search);
          this.router.navigate(["dashboard/research/" + search.data._id])
        } else {
          throw new Error('Something went wrong')
        }
      } catch (e: any) {
        this.message.error(e.message);
      }
    } else {
      this.message.error('First name and last name is required');
    }
  }

  serversendevent() {
    this.modalService.transactionSuccess();
  }

  loadOne(): void {
    this.startSearching();
  }

}
