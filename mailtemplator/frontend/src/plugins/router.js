import Vue from 'vue'
import Router from 'vue-router'
import Top from '../pages/Top'

Vue.use(Router)

export default new Router({
    mode: 'history',
    routes: [
        {
            path: '/',
            component: Top,
            name: "Top"
        }
    ]
})