export const state = () => ({
    counter: 0
})
  
export const mutations = {
    increment (state) {
        state.counter++
    }
}
export const actions = {
    nuxtServerInit ({ commit }, { req }) {
        if (req.authUser) {
            commit('user', req.authUser)
        }
    }
}