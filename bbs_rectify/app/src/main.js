import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import router from './router'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import _escape from 'lodash/escape'

import VueQuillEditor from 'vue-quill-editor'

import 'quill/dist/quill.core.css' // import styles
import 'quill/dist/quill.snow.css' // for snow theme
import 'quill/dist/quill.bubble.css' // for bubble theme



import axios from 'axios'
import qs from 'qs'

Vue.use(VueRouter)
Vue.use(ElementUI);
Vue.use(VueQuillEditor, /* { default global options } */)

Vue.prototype.$axios = axios    //全局注册，使用方法为:this.$axios
Vue.prototype.qs = qs           //全局注册，使用方法为:this.qs
Vue.prototype.$escape = _escape

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
