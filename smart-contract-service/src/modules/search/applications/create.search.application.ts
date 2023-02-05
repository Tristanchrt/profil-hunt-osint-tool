import { Injectable, Inject } from '@nestjs/common';
import { SearchDomain } from '../domain/search.domain';
import { ICreateSearchApplication } from '../interfaces/applications/create.search.application.interface';
import { TYPES } from '../interfaces/types';
import { ICreateSearchService } from '../interfaces/services/create.search.service.interface';

@Injectable()
export class CreateSearchApplication implements ICreateSearchApplication {
    constructor(@Inject(TYPES.services.ICreateSearchService) private searchService: ICreateSearchService) {}

    async create(search: SearchDomain): Promise<SearchDomain> {
        return this.searchService.create(search);
    }
}
