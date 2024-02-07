import { Component } from '@angular/core';
import { SearchService } from '../search.service';
import { HttpClientModule } from "@angular/common/http";

@Component({
  selector: 'app-search',
  standalone: true,
  imports: [HttpClientModule],
  templateUrl: './search.component.html',
  styleUrl: './search.component.scss'
})
export class SearchComponent {
  params: any = {
    drawing_number: ''
  }
  results: any[] = [];

  constructor(private searchService: SearchService) {}

  search(): void {
    this.searchService.search(this.params)
      .subscribe((data: any[]) => {
        this.results = data;
      });
  }
}
