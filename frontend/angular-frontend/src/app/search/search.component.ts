import { CommonModule } from '@angular/common';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-search',
  standalone: true,
  imports: [FormsModule, HttpClientModule,CommonModule],
  templateUrl: './search.component.html',
  styleUrl: './search.component.scss'
})
export class SearchComponent {

  SearchArray : any[] = [];

  drawing_number: string = '';
  
  constructor (private http: HttpClient){
    // this.getData();
  }
  searchRecords(){
    let bodyData = {
      'drawing_number' : this.drawing_number
    };
    this.http.post('http://127.0.0.1:8000/student',bodyData).subscribe((resultData: any)=>
    {
        console.log(resultData);
        alert('Search Successful');
        this.SearchArray = resultData;
        // this.getData();
    });
  }
  // getData(){
  //   this.http.get('http://127.0.0.1:8000/student').subscribe((resultData: any)=>
  //   {
  //     console.log(resultData);
  //     this.SearchArray = resultData;
  //   })
  // }
}
