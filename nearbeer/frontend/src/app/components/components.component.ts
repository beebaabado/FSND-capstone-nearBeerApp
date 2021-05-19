import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-components',
  templateUrl: './components.component.html',
  styleUrls: ['./components.component.scss'],
})
export class ComponentsComponent implements OnInit {
 
  


  constructor(title: string) {
      console.log ("Beer card title: ", title; )
   }

  ngOnInit() {}

}
