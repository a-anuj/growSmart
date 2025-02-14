import { createStore } from "vuex";

export default createStore({
    state: {
        user: null, // Store user info globally
    },
    mutations: {
        setUser(state, user) {
            state.user = user;
        },
        logout(state) {
            state.user = null;
        }
    }
});
