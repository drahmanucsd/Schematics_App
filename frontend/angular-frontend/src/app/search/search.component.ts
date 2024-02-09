import { Component, OnInit } from '@angular/core';
import { FormControl } from '@angular/forms';
import { Observable } from 'rxjs';
import { startWith, map } from 'rxjs/operators';
import { CommonModule } from '@angular/common';
import { HttpClient, HttpClientModule } from '@angular/common/http';  
import { MaterialModule } from '../material/material.module';
import { Location } from '@angular/common';

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
  electric_remote_2_way_panel = false;
  central_hydraulic_panel = false;
  electric_failsafe_panel = false;
  supply_panel = false;
  air_motor_panel = false;
  electric_motor_panel = false;
  self_contained_panel = false;
  pneumatic_panel = false;


  myControl = new FormControl('');
  options: string[] = ['A', 'B', 'C', 'D','E'];
  filteredOptions!: Observable<string[]>;

  total_results: string = '';
  SearchArray: any[] = [];
  drawing_number: string = '';
  descr: string = '';
  operator_type: string = '';
  special: string = '';
  approved_by: string = '';
  drawn_by: string = '';
  date_drawn: string = '';
  nitrogen_power: boolean = false;
  power_regulator: boolean = false;
  trigger_valve: boolean = false;
  lockout: boolean = false;
  sequencing: boolean = false;
  latching_feature: boolean = false;
  low_pressure_solenoid: boolean = false;
  high_pressure_solenoid: boolean = false;
  pilot_isolation_valve: boolean = false;
  double_holding_valve: boolean = false;
  redundant_solenoid: boolean = false;
  momentary_impulse: boolean = false;
  pilot_regular: boolean = false;
  pilot_valve: boolean = false;
  
  fail_close: boolean = false;
  dashpot: boolean = false;
  pilot_regulator: boolean = false;
  solenoid: boolean = false;

  electric_remote_2_way_view: number = 0;


  constructor(private http: HttpClient, private location: Location) { }

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
  clearFields(){
    window.location.reload();

  }
  searchRecords() {
    let bodyData = {
      'drawing_number': this.drawing_number,
      'descr': this.descr,
      'date_drawn':this.date_drawn,
      'sheet_size' : this.myControl.value,
      'operator_type': this.operator_type,
      'drawn_by': this.drawn_by,
      'approved_by' :this.approved_by,
      'special': this.special,
      'ght': this.gas_hydraulic_panel,
      'latching_feature': this.latching_feature
    };
    this.http.post('http://127.0.0.1:8000/search', bodyData).subscribe((resultData: any) => {
      console.log(resultData);
      alert('Search Successful');
      this.total_results = resultData.total_results;
      this.SearchArray = resultData.search_results;
    });
  }
}
