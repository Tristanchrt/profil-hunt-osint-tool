import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TransactionModalWaitingComponent } from './transaction-modal-waiting.component';

describe('TransactionModalWaitingComponent', () => {
  let component: TransactionModalWaitingComponent;
  let fixture: ComponentFixture<TransactionModalWaitingComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ TransactionModalWaitingComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(TransactionModalWaitingComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
