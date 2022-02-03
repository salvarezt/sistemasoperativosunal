import { ActivatedRoute } from '@angular/router';
import { EventEmitter, Injectable } from '@angular/core';
import { CookieService } from 'ngx-cookie-service';
import { Socket } from 'ngx-socket-io';

@Injectable({
  providedIn: 'root'
})
export class SocketWebService extends Socket {

  outEven: EventEmitter<any> = new EventEmitter();
  callback: EventEmitter<any> = new EventEmitter();

  constructor(private cookieService: CookieService) {
    super({
      url:'http://localhost:5000', // Url del backend
      options : {
        query: {
          nameRoom: cookieService.get('room') // Obtiene sala de la cookie
        }
      }
    })

    this.listen() // Emite conexion
  }

  listen = () => {
    this.ioSocket.on('event', (res: any) => this.callback.emit(res))
  }

  emitEvent = (payload = {}) => {
    this.ioSocket.emit('event', payload);
  }
}
