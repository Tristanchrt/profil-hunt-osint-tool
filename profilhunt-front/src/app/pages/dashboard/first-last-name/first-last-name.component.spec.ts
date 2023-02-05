import { ComponentFixture, TestBed } from '@angular/core/testing';

import { FirstLastNameComponent } from './first-last-name.component';

describe('FirstLastNameComponent', () => {
  let component: FirstLastNameComponent;
  let fixture: ComponentFixture<FirstLastNameComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ FirstLastNameComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(FirstLastNameComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
