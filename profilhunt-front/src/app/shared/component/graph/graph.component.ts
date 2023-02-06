import { Component, Input, OnInit, ViewChild } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import {
  NzGraphComponent,
  NzGraphData,
  NzGraphDataDef,
  NzGraphZoomDirective,
  NzRankDirection
} from 'ng-zorro-antd/graph';

@Component({
  selector: 'app-graph',
  templateUrl: './graph.component.html',
  styleUrls: ['./graph.component.scss']
})
export class GraphComponent implements OnInit {

  @Input() graph: any;

  constructor(private route: ActivatedRoute) { }

  research = {
    id: "",
  }
  
  currentNode: any = {
    name: '', 
    id: '',
    company: '',
    country: '',
    city: '',
    state: '',
    pseudo: '',
    insta_follower: '',
    insta_following: '',
  }
  
  rankDirection: NzRankDirection = 'TB';
  graphData: any = null;

  @ViewChild(NzGraphComponent, { static: true }) nzGraphComponent!: NzGraphComponent;
  @ViewChild(NzGraphZoomDirective, { static: true }) zoomController!: NzGraphZoomDirective;

  ngOnInit() {
    this.graphData = new NzGraphData(this.graph);
    this.research.id = this.route.snapshot.params['id'];
    this.expandAll();
  }

  expand(name: string): void {
    this.graphData.expand(name);
  }

  collapse(name: string): void {
    this.graphData.collapse(name);
  }

  expandAll(): void {
    this.graphData.expandAll();
  }

  collapseAll(): void {
    this.graphData.collapseAll();
  }

  fit(): void {
    this.zoomController?.fitCenter();
  }

  focusNode(e: string | number): void {
    this.zoomController?.focus(e);
    this.currentNode = this.graphData.dataSource['nodes'][e]
    this.showModal();
  }

  graphInitialized(_ele: NzGraphComponent): void {
    this.zoomController?.fitCenter();
  }

  zoom = 0.5;

  isVisible = false;

  showModal(): void {
    this.isVisible = true;
  }

  handleOk(): void {
    console.log('Button ok clicked!');
    this.isVisible = false;
  }

  handleCancel(): void {
    console.log('Button cancel clicked!');
    this.isVisible = false;
  }
  
}
