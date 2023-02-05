import { Injectable, Inject } from '@nestjs/common';
import { SearchDomain } from '../domain/search.domain';
import { ICreateSearchService } from '../interfaces/services/create.search.service.interface';

@Injectable()
export class CreateSearchService implements ICreateSearchService {
    constructor() {}

    async create(search: SearchDomain): Promise<any> {
        return Promise.resolve('pomme');
    }
}
