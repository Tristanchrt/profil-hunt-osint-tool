import { Controller, Inject, Post, Res, Body, HttpStatus, UsePipes, Get, Param, ParseUUIDPipe, UseGuards, Req, ArgumentsHost, UseInterceptors, CacheInterceptor, CACHE_MANAGER } from '@nestjs/common';
import { TYPES } from '../interfaces/types';
import { ICreateSearchApplication } from '../interfaces/applications/create.search.application.interface';
import { IGetSearchApplication } from '../interfaces/applications/get.search.application.interface';
import { AuthGuard } from 'src/common/guard/auth.guard';
import { HttpResponseService } from 'src/api/response/http-response.service';

@Controller('auth')
export class SearchController {
    constructor(
        @Inject(TYPES.applications.ICreateSearchApplication) private createSearchApp: ICreateSearchApplication,
        @Inject(TYPES.applications.IGetSearchApplication) private getSearchApp: IGetSearchApplication,
        private httpResponseService: HttpResponseService
    ) {}

    @Get(':id')
    // @UseGuards(new AuthGuard())
    async findOne(@Res() res, @Req() req, @Param('id') id: string) {
        const search = await this.getSearchApp.getById(id);
        return this.httpResponseService.sendResponse(res, req, HttpStatus.OK, search);
    }

    @Get('/account/:id')
    async findOn2e(@Res() res, @Req() req, @Param('id') address: string) {
        const account = await this.getSearchApp.getByAccount(address);
        return this.httpResponseService.sendResponse(res, req, HttpStatus.OK, account);
    }
}
