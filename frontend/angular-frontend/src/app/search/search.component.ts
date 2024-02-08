import { Component, OnInit } from '@angular/core';
import { FormControl } from '@angular/forms';
import { Observable } from 'rxjs';
import { startWith, map } from 'rxjs/operators';
import { CommonModule } from '@angular/common';
import { HttpClient, HttpClientModule } from '@angular/common/http';  
import { MaterialModule } from '../material/material.module';

@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  standalone: true,
  imports: [ HttpClientModule,CommonModule,MaterialModule],
  styleUrls: ['./search.component.scss']
})
export class SearchComponent implements OnInit {
  panelOpenState = false;
  gas_hydraulic_panel = false;
  gas_hydraulic_manual_panel = false;




  myControl = new FormControl('');
  options: string[] = ['A', 'B', 'C', 'D','E'];
  filteredOptions!: Observable<string[]>;

  SearchArray: any[] = [];
  drawing_number: string = '';
  descr: string = '';
  operator_type: string = '';
  special: string = '';
  date_drawn: string = '';
  nitrogen_power: boolean = false;
  power_regulator: boolean = false;
  



  constructor(private http: HttpClient) { }

  ngOnInit() {
    this.filteredOptions = this.myControl.valueChanges.pipe(
      startWith(''),
      map(value => this._filter(value || '')),
    );
  }

  private _filter(value: string): string[] {
    const filterValue = value.toLowerCase();
    return this.options.filter(option => option.toLowerCase().includes(filterValue));
  }

  searchRecords() {
    let bodyData = {
      'drawing_number': this.drawing_number,
      'descr': ''
      // sheet_size = this.myControl.value
    };
    this.http.post('http://127.0.0.1:8000/search', bodyData).subscribe((resultData: any) => {
      console.log(resultData);
      alert('Search Successful');
      this.SearchArray = resultData;
    });
  }
}
