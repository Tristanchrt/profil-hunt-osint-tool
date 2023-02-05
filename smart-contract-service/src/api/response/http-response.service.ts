import { BadRequestException, NotFoundException, Injectable, HttpStatus } from '@nestjs/common';

@Injectable()
export class HttpResponseService {

    async sendResponse(res: any, req: any, status: HttpStatus, data: any): Promise<any> {
        return res.status(status).json({
            statusCode: status,
            timestamp: new Date().toISOString(),
            path: req.url,
            body: data
        });
    }
}
