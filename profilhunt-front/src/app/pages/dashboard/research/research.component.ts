import { GraphService } from './../../../core/services/graph.service';
import { Component, OnInit, ViewChild } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { NzGraphDataDef } from 'ng-zorro-antd/graph';
import { AnimationOptions } from 'ngx-lottie';

@Component({
  selector: 'app-research',
  templateUrl: './research.component.html',
  styleUrls: ['./research.component.scss']
})
export class ResearchComponent implements OnInit {

  constructor(private route: ActivatedRoute, private graphService: GraphService) { }

  isSpinning = false;

  research = {
    id: "",
  }

  options: AnimationOptions = {
    path: '/assets/animations/hacker.json',
  };

  graph: any = null

  data_graph: NzGraphDataDef | any = {}

  intervalId: any

  async get_graph(id: string) {
    setTimeout(async () => {
      let data: any = await this.graphService.getGraphById(id)
      if (data) {
        if(data.data != "In progress"){
          this.isSpinning = true;
          this.graph = data.data;
          console.log('graph :',data)
        }
      } else {
        console.log('Get graph failed...')
      }
      console.log('Get graph by id :', this.graph, data);      
    }, 500);
  }

  async ngOnInit() {
    this.research.id = this.route.snapshot.params['id'];
    await this.get_graph(this.research.id);
  }

  async ngAfterViewInit() {
    this.intervalId = setInterval(async () => {
      if (this.graph) {
        clearInterval(this.intervalId);
      }
      this.get_graph(this.research.id);
    }, 10000);
  }

  ngOnDestroy() {
    clearInterval(this.intervalId);
  }

}
