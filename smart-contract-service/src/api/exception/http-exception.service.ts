import { BadRequestException, NotFoundException, Injectable } from '@nestjs/common';

@Injectable()
export class HttpExceptionService {

    async badRequestException(error: string): Promise<any> {
        throw new BadRequestException(error);
    }
    async notFoundException(error: string): Promise<any> {
        throw new NotFoundException(error);
    }
}
