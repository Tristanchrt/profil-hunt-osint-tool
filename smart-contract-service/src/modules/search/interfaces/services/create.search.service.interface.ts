import { SearchDomain } from "../../domain/search.domain"

export interface ICreateSearchService {
    create(SearchDomain: SearchDomain): Promise<SearchDomain>;
}
