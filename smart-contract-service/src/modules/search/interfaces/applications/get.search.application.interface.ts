
export interface IGetSearchApplication {
    getById(id: string): Promise<any>;
    getByAccount(address: string): Promise<any>;
}
