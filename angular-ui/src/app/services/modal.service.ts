import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable } from 'rxjs';

/** 
 * Provides Angular components the ability to subscribe to 'open' and 'close'
 * events associated with a modal window. This code was adapted from:
 * https://dev.to/daviddalbusco/create-a-modal-for-your-angular-app-without-libs-4hh9
 */
@Injectable({
  providedIn: 'root'
})
export class ModalService {

  /** 
   * A BehaviorSubject (type of observable) that emits 'open' or 'close' 
   * string values. Subscribers immediately receive 'close' as the first value,
   * even though no data has been emitted yet.
   */
  private display: BehaviorSubject<'open' | 'close'> = new BehaviorSubject('close');

  /**
   * A method to subscribe to the BehaviorSubject and catch values it emits.
   */
  watch(): Observable<'open' | 'close'> {
    return this.display.asObservable();
  }

  /**
   * Calls the BehaviorSubject to emit an 'open' event.
   */
  open() {
    document.body.classList.add("unscrollable")
    this.display.next('open');
  }

  /**
   * Calls the BehaviorSubject to emit a 'closed' event.
   */
  close() {
    document.body.classList.remove("unscrollable");
    this.display.next('close');
  }
}