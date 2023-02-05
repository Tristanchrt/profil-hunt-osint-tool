import { SearchDomain } from "../../domain/search.domain"

export interface ICreateSearchApplication {
    create(SearchDomain: SearchDomain): Promise<SearchDomain>;
}
