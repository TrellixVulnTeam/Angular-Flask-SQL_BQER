import { Component } from '@angular/core';
import { Subscription } from 'rxjs';
import { ApiService } from './api-service.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'frontend';

  indexSubs: Subscription | undefined;
  index: string | undefined;

  constructor(private restApi: ApiService){}

  ngOnInit() {
    this.indexSubs = this.restApi.getIndex()
        .subscribe((res: string) => this.index = res);

  }

  ngOnDestroy() {
  }
}
