import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TransactionModalSuccessComponent } from './transaction-modal-success.component';

describe('TransactionModalSuccessComponent', () => {
  let component: TransactionModalSuccessComponent;
  let fixture: ComponentFixture<TransactionModalSuccessComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ TransactionModalSuccessComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(TransactionModalSuccessComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
