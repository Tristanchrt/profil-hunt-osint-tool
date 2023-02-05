import { SearchDomain } from "../../domain/search.domain"

export interface IGetSearchService {
    getById(id: string): Promise<SearchDomain>;
    getByAccount(address: string): Promise<any>
}
