import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { CookieService } from 'ngx-cookie-service';

@Component({
  selector: 'app-room',
  templateUrl: './room.component.html',
  styleUrls: ['./room.component.css']
})
export class RoomComponent implements OnInit {

  room: string = '';
  constructor(private router: ActivatedRoute, private cookieService: CookieService) { }

  ngOnInit(): void {
    let k = this.router.snapshot.paramMap.get('room');
    if(k){
      this.room = k;
    } else {
      this.room = '';
    }
    this.cookieService.set('room', this.room);
    console.log(this.room);
  }

}
