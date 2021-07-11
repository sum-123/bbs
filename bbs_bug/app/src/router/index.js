import Vue from 'vue'
import VueRouter from 'vue-router'
import login from '../views/login.vue'
import register from '../views/register.vue'
import index from '../views/index.vue'
import search from '../views/search.vue'
import personal from '../views/personal.vue'
import myMessage1 from '../views/myMessage1.vue'
import myMessage2 from '../views/myMessage2.vue'
import createMessage from '../views/createMessage.vue'
import messageDetail from '../views/messageDetail.vue'
import changePass from '../views/changePass.vue'
import changeAvatar from '../views/changeAvatar.vue'
import createComment from '../views/createComment.vue'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'index',
    component:index
  },
  {
    path:'/index',
    name:'index',
    component:index
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path:'/login',
    name:'login',
    component:login
  },
  {
    path:'/register',
    name:'register',
    component:register
  },
  {
    path:'/search',
    name:'search',
    component:search
  },
  {
    path:'/personal',
    name:'personal',
    component:personal
  },
  {
    path:'/myMessage1',
    name:'myMessage1',
    component:myMessage1
  },
  {
    path:'/myMessage2',
    name:'myMessage2',
    component:myMessage2
  },
  {
    path:'/createMessage',
    name:'createMessage',
    component:createMessage
  },
  {
    path:'/messageDetail',
    name:'messageDetail',
    component:messageDetail
  },
  {
    path:'/changePass',
    name:'changePass',
    component:changePass
  },
  {
    path:'/changeAvatar',
    name:'changeAvatar',
    component:changeAvatar
  },
  {
    path:'/createComment',
    name:'createComment',
    component:createComment
  }
  
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
