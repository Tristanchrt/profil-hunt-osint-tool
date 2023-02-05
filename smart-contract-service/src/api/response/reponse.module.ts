import { Module } from '@nestjs/common';
import { HttpResponseService } from './http-response.service';

@Module({
  controllers: [],
  providers: [HttpResponseService],
  exports: [HttpResponseService]
})
export class ReponseModule {}