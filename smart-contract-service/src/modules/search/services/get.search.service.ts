import { HttpService } from '@nestjs/axios';
import { Injectable, Inject } from '@nestjs/common';
import { IGetSearchService } from '../interfaces/services/get.search.service.interface';
import { catchError, firstValueFrom } from 'rxjs';
import { AxiosError } from 'axios';
import { SCService } from 'src/common/service/sc.service';
import {
    Address,
    AddressValue,
    ContractFunction,
    Query
} from '@elrondnetwork/erdjs';
@Injectable()
export class GetSearchService implements IGetSearchService {
    constructor(private readonly httpService: HttpService, private scService: SCService) { }

    async getById(id: string): Promise<any> {
        let data = await this.scService.removeUserFromPaid(id);
        console.log('DATA REMOVE USER LIST', data);
        return data;
    }

    async getByAccount(address: string): Promise<any> {
        try {
            let data = await this.scService.query([new AddressValue(new Address(address))], "didUserPaid")
            if (data) {
                data = parseInt(Buffer.from(data['returnData'][0], 'base64').toString('hex'), 16);
                if (data == null)
                    data = false;
                return { 'adddress': address, "isValide": true };
            } else {
                return { 'adddress': address, "isValide": false };
            }
        } catch (e) {
            console.log('Error', e)
            return { 'adddress': address, "isValide": false };
        }
    }

}
