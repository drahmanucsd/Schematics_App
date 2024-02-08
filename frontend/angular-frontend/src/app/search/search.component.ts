import { CommonModule } from '@angular/common';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { MaterialModule } from '../material/material.module';

@Component({
  selector: 'app-search',
  standalone: true,
  imports: [FormsModule, HttpClientModule,CommonModule,MaterialModule],
  templateUrl: './search.component.html',
  styleUrl: './search.component.scss'
})
export class SearchComponent {

  SearchArray : any[] = [];

  drawing_number: string = '';
  descr: string = '';
  operator_type: string = '';
  special: string = '';
  date_drawn: string = ''; 
  
  constructor (private http: HttpClient){
  }
  searchRecords(){
    let bodyData = {
      'drawing_number' : this.drawing_number,
      'descr' : ''
    };
    this.http.post('http://127.0.0.1:8000/search',bodyData).subscribe((resultData: any)=>
    {
        console.log(resultData);
        alert('Search Successful');
        this.SearchArray = resultData;
    });
  }
}

