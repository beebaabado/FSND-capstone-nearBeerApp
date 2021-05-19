import { TestBed } from '@angular/core/testing';

import { UntappdServerService } from './untappd-server.service';

describe('UntappdServerService', () => {
  let service: UntappdServerService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(UntappdServerService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
