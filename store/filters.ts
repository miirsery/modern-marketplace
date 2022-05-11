// store/filters.js
import { defineStore } from 'pinia'

export const useCounterStore = defineStore('main', {
    state: () => ({
        counter: 2,
        name: 'Alex'
    }),
    getters: {
        doubleCount: (state) => {
            state.counter * 2
        }
    },
    actions: {
        reset() {
            this.counter = 0
        },
        addOne() {
            this.counter++
        }
    }
})