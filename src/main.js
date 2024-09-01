import Vue from 'vue'
import App from './App.vue'
import BootstrapVue from 'bootstrap-vue'
import VueApexCharts from 'vue-apexcharts'
import Vuelidate from 'vuelidate'
import VueSweetalert2 from 'vue-sweetalert2';
import VueMask from 'v-mask'
import ElementUI from 'element-ui' //element-ui的全部组件
import vco from "v-click-outside"
import axios from 'axios'
import router from './router'
import store from '@/state/store'
import i18n from './i18n'
import * as VCharts from 'v-charts'
import * as echarts from "echarts"
import VModal from 'vue-js-modal'

import 'element-ui/lib/theme-chalk/index.css'//element-ui的css

import "@/assets/scss/app.scss";

import { initFirebaseBackend } from './helpers/firebase/authUtils';

import { configureFakeBackend } from './helpers/fakebackend/fake-backend';


Vue.prototype.$echarts = echarts

Vue.use(VCharts)
Vue.use(VueApexCharts)
Vue.use(VModal, { componentName: 'Foo' })
Vue.component('apexchart', VueApexCharts)

axios.defaults.baseURL = '/api'
axios.defaults.headers.post['Content-Type'] = 'application/json';
Vue.prototype.$axios = axios

Vue.use(ElementUI) //使用elementUI
Vue.prototype.$echarts = echarts;
Vue.config.productionTip = false

const firebaseConfig = {
  apiKey: process.env.VUE_APP_APIKEY,
  authDomain: process.env.VUE_APP_AUTHDOMAIN,
  databaseURL: process.env.VUE_APP_VUE_APP_DATABASEURL,
  projectId: process.env.VUE_APP_PROJECTId,
  storageBucket: process.env.VUE_APP_STORAGEBUCKET,
  messagingSenderId: process.env.VUE_APP_MESSAGINGSENDERID,
  appId: process.env.VUE_APP_APPId,
  measurementId: process.env.VUE_APP_MEASUREMENTID
};

if (process.env.VUE_APP_DEFAULT_AUTH === "firebase") {
  initFirebaseBackend(firebaseConfig);
} else {
  configureFakeBackend();
}

Vue.config.productionTip = false
Vue.use(BootstrapVue)
Vue.use(vco)
Vue.use(Vuelidate)
Vue.use(VueSweetalert2);
Vue.use(VueMask)
Vue.use(require('vue-chartist'))
Vue.component('apexchart', VueApexCharts)

new Vue({
  router,
  store,
  i18n,
  render: h => h(App)
}).$mount('#app')
