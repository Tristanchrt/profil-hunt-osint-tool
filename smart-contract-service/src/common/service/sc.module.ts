import { Module } from '@nestjs/common';
import { SCService } from './sc.service';

@Module({
  controllers: [],
  providers: [SCService],
  exports: [SCService]
})
export class SCModule {}