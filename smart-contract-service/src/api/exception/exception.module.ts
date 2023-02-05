import { Module } from '@nestjs/common';
import { HttpExceptionService } from './http-exception.service';

@Module({
  controllers: [],
  providers: [HttpExceptionService],
  exports: [HttpExceptionService]
})
export class ExceptionModule {}