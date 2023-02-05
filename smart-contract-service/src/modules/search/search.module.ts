import { Module } from '@nestjs/common';
import { SearchController } from './controller/search.controller';
import { CreateSearchApplication } from './applications/create.search.application';
import { TYPES } from './interfaces/types';
import { GetSearchApplication } from './applications/get.search.application';
import { GetSearchService } from "./services/get.search.service";
import { CreateSearchService } from "./services/create.search.service";
import { ExceptionModule } from 'src/api/exception/exception.module';
import { ReponseModule } from 'src/api/response/reponse.module';
import { HttpModule } from '@nestjs/axios';
import { SCModule } from 'src/common/service/sc.module';

const createSearchApp = { provide: TYPES.applications.ICreateSearchApplication, useClass: CreateSearchApplication };
const getSearchApp = { provide: TYPES.applications.IGetSearchApplication, useClass: GetSearchApplication };

const createSearchService = { provide: TYPES.services.ICreateSearchService, useClass: CreateSearchService };
const getSearchService = { provide: TYPES.services.IGetSearchService, useClass: GetSearchService };

@Module({
    imports: [ExceptionModule, ReponseModule, HttpModule, SCModule],
    controllers: [SearchController],
    providers: [createSearchApp, getSearchApp, createSearchService, getSearchService],
})
export class SearchModule {}
