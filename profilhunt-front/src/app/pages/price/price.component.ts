import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-price',
  templateUrl: './price.component.html',
  styleUrls: ['./price.component.scss']
})
export class PriceComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
  }

  pricingBox = [
    {
      name: 'Free',
      price: 0,
      features: ["Name","Friends","__","__","__"]
    },
    {
      name: 'Pro',
      price: 0.3,
      features: ["Name","Friends","Skills","Hobbies","__"]
    },
    {
      name: 'Business',
      price: 0.5,
      features: ["Name","Friends","Skills","Hobbies","life style analyse"]
    }
  ];
}
