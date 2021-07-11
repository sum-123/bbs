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
    component: index
  },
  {
    path: '/index',
    name: 'index',
    component: index
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
    path: '/login',
    name: 'login',
    component: login
  },
  {
    path: '/register',
    name: 'register',
    component: register
  },
  {
    path: '/search',
    name: 'search',
    component: search
  },
  {
    path: '/personal',
    name: 'personal',
    component: personal
  },
  {
    path: '/myMessage1',
    name: 'myMessage1',
    component: myMessage1
  },
  {
    path: '/myMessage2',
    name: 'myMessage2',
    component: myMessage2
  },
  {
    path: '/createMessage',
    name: 'createMessage',
    component: createMessage
  },
  {
    path: '/messageDetail',
    name: 'messageDetail',
    component: messageDetail
  },
  {
    path: '/changePass',
    name: 'changePass',
    component: changePass
  },
  {
    path: '/changeAvatar',
    name: 'changeAvatar',
    component: changeAvatar
  },
  {
    path: '/createComment',
    name: 'createComment',
    component: createComment
  }

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

//前置
// router.beforeEach((to,from,next)=>{
// //如果要去My或者index页面
//   if(to.path=='/changeAvatar' || to.path=='/personal' || 
//   to.path=='/changePass'|| to.path=='/createMessage'|| to.path=='/createComment'|| 
//   to.path=='/myMessage2'){
//   //判断l如果ocalStorage里面是否有Username
//     if(localStorage.getItem("username")){
//    //有用户信息让它继续走
//       next(true);
//     }else{
//       //否则让它跳转到登录界面，跳转到登录界面时，需要把to.path传入，方便在登录成功时跳转到对应界面上
//       next({"path":"/login",query:{"topath":to.path}})
//     }
//   }else{
//   //否则去其他界面时 让它继续走
//     next(true);
//   }
// })

// 路由守护
router.beforeEach((to, from, next) => {
  const accessToken = window.sessionStorage.getItem('accessToken')

  if (accessToken) {
    // 重新登录后，转到之前的页面
    if (Object.keys(from.query).length !== 0) {
      let redirect = from.query.redirect
      if (to.path === redirect) // 解决无限循环问题
      {
        next({ "path": "/index" })
      }
      else {
        next({ path: redirect }) // 重新登录后，转到之前的页面
      }
    }
  }

  if (accessToken && to.path !== '/login') {
    // 有token 但不是去 login页面
    next(true)
  }
  else if (accessToken && to.path === '/login') {
    //用户已经登陆，不让访问Login登录界面
    localStorage.state = 1
    alert("您已登录！")
    next({ path: from.fullPath })
  }
  else if (!accessToken) {
    if (to.path == '/login') {
      next(true)
    } else if (to.path == '/') {
      next({ "path": "/index" })
    } else if (to.path == '/index') {
      next(true)
    } else if (to.path == '/register') {
      next(true)
    } else if (to.path == '/search') {
      next(true)
    } else {
      alert("请先登录！")
      next({ "path": "/login" })
    }

  }
  else {
    next(true)
  }
})

export default router
