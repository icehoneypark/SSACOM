import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import BootstrapVue3 from 'bootstrap-vue-3'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue-3/dist/bootstrap-vue-3.css'

import 'bootstrap/dist/css/bootstrap.min.css'
import "bootstrap"

// import axios from 'axios'

import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"

createApp(App).use(store).use(router).mount('#app')
App.use(BootstrapVue3)

// App.use(axios)