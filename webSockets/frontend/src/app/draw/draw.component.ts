import { AfterViewInit, Component, Host, HostListener, OnInit, ViewChild } from '@angular/core';
import { Socket } from 'ngx-socket-io';
import { SocketWebService } from '../socket-web.service';

@Component({
  selector: 'app-draw',
  templateUrl: './draw.component.html',
  styleUrls: ['./draw.component.css']
})
export class DrawComponent implements OnInit, AfterViewInit {

  @ViewChild('canvasRef', {static: false}) canvasRef: any // Referencia html
  public isPressing: Boolean = false;
  public width = 800;
  public height = 800;

  private cx: any; // CanvasRenderingContext2D
  private points: Array<any> = [];

  @HostListener('document:mousemove', ['$event'])
  onMouseMove = (e:any) => {
    // e -> Evento: Movimiento de mouse
    if (e.target.id == 'canvasId' && this.isPressing) {
      this.write(e);
    }
  }

  @HostListener('click', ['$event'])
  onClick = (e:any) => {
    if( e.target.id == 'canvasId'){
      this.isPressing = !this.isPressing;
      const prevPos = {
        x: e.clientX - e.left,
        y: e.clientY - e.top
      }
      this.points.push(prevPos);
    }
    
  }
  constructor(private socketWebService: SocketWebService) {
    socketWebService.callback.subscribe(res => {
      const {prevPos} = res
      console.log(res);
      this.writeSingle(prevPos, false)
    })
   }

  ngOnInit(): void {
  }

  ngAfterViewInit(): void {
      this.render()
  }

  private render(): any {
    const canvasEl = this.canvasRef.nativeElement;
    this.cx = canvasEl.getContext('2d');

    canvasEl.width = this.width;
    canvasEl.height = this.height;

    this.cx.lineWidth = 3; // Pixeles de anchor de pincel
    this.cx.lineCap = 'round'; // Terminacion redondeada
    this.cx.strokeStyle = '#000'; // Color de pincel: Negro
  }

  private write(res : MouseEvent): any {
    const canvasEl = this.canvasRef.nativeElement;
    const rect = canvasEl.getBoundingClientRect(); // Coordenadas del elemento en pantalla
    const prevPos = {
      x: res.clientX - rect.left,
      y: res.clientY - rect.top
    }
    
    this.writeSingle(prevPos); // Inserta prevPos en el arreglo de puntos
  }

  private writeSingle = (prevPos : any, emit = true) => {
    this.points.push(prevPos);
    if (this.points.length > 3){
      const prevPost = this.points[this.points.length - 1];
      const currentPos = this.points[this.points.length - 2];

      if( !this.cx ) {
        return;
      } else {
        this.cx.beginPath();
        this.cx.moveTo(prevPost.x, prevPost.y);
        this.cx.lineTo(currentPos.x, currentPos.y);
        this.cx.stroke();
      }

      if(emit){
        this.socketWebService.emitEvent({prevPos})
      }
    }
  }

  public clearZone = () => {
      this.points = [];
      this.cx.clearRect(0, 0, this.width, this.height);
  }
}
