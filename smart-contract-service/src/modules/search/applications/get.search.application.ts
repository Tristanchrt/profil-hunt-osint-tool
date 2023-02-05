import { Injectable, Inject, NotFoundException } from '@nestjs/common';
import { SearchDomain } from '../domain/search.domain';
import { TYPES } from '../interfaces/types';
import { IGetSearchApplication } from '../interfaces/applications/get.search.application.interface';
import { IGetSearchService } from '../interfaces/services/get.search.service.interface';
import { HttpExceptionService } from 'src/api/exception/http-exception.service';

@Injectable()
export class GetSearchApplication implements IGetSearchApplication {
    constructor(@Inject(TYPES.services.IGetSearchService) private getSearchService: IGetSearchService,
    private httpExceptionService: HttpExceptionService) {}

    async getById(id: string): Promise<SearchDomain> {
        try {
            const search = await this.getSearchService.getById(id);
            if (!search) 
                this.httpExceptionService.notFoundException("Id not found on seach object");
            return search;
        }catch (e) {
            return this.httpExceptionService.badRequestException(e);
        }
    }
    async getByAccount(address: string): Promise<any> {
        try {
            const search = await this.getSearchService.getByAccount(address);
            if (!search) 
                this.httpExceptionService.notFoundException("Id not found on seach object");
            return search;
        }catch (e) {
            return this.httpExceptionService.badRequestException(e);
        }
    }
}
