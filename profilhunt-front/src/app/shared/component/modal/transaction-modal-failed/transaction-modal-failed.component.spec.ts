import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TransactionModalFailedComponent } from './transaction-modal-failed.component';

describe('TransactionModalFailedComponent', () => {
  let component: TransactionModalFailedComponent;
  let fixture: ComponentFixture<TransactionModalFailedComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ TransactionModalFailedComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(TransactionModalFailedComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
