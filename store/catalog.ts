import {defineStore} from "pinia";

export const useCatalogStore = defineStore('products', {
    state: () => ({
        catalog: []
    }),
    actions: {
        async getCatalog(): Promise<string[]> {
           return await fetch('http://localhost:8000/api/product/list-product/', {
               method: 'GET',
               headers: {
                   'Content-Type': 'application/json'
               },
           }).then(r => r.json())
        }
    }
})