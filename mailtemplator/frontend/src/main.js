import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import Router from './plugins/router'


Vue.config.productionTip = false

new Vue({
  vuetify,
  router: Router,
  render: h => h(App)
}).$mount('#app')
