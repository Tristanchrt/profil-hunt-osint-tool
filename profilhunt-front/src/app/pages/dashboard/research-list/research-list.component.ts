import { SearchService } from 'src/app/core/services/search.service';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-research-list',
  templateUrl: './research-list.component.html',
  styleUrls: ['./research-list.component.scss']
})
export class ResearchListComponent implements OnInit {

  constructor(private searchService: SearchService) { }

  allReasearch: any = []
  maxPagnination: number = 500
  intervalId: any
  isData: boolean = false
  currentIndexPag = 1

  async get_search(index = 1) {
    let data: any = await this.searchService.getAllsearchFirstLastName(index);
    if(data){
        console.log('Get search :', data);
        this.allReasearch = data.data;
        this.isData = true;
    }else{
      this.isData = false;
    }
    console.log(this.isData)
  }

  async nextPage(index: any){
    this.currentIndexPag = index
    this.get_search(this.currentIndexPag);
  }

  async ngOnInit() {
   this.get_search();
  }

  async ngAfterViewInit() {
    this.intervalId = setInterval(async () => {
      this.get_search();
    }, 10000);
  }

  ngOnDestroy() {
    clearInterval(this.intervalId);
  }

}
