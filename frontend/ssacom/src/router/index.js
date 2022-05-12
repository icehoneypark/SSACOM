import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/dashboard',
    name: 'dashboard',
    component: () => import('../views/DashboardView.vue')
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/notice',
    name: 'notice',
    component: () => import('../views/NoticeView.vue'),
  },
  {
    path: '/notice/create',
    name: 'noticecreate',
    component: () => import('../views/NoticeCreate.vue'),
  },
  {
    path: '/notice/:id',
    name: 'noticedetail',
    component: () => import('../views/NoticeDetail.vue'),
  },
  {
    path: '/notice/update/:id',
    name: 'noticeupdate',
    component: () => import('../views/NoticeUpdate.vue'),
  },
  {
    path: '/mypage',
    name: 'mypage',
    component: () => import('../views/MyPage.vue')
  },
  {
    path : '/login',
    name : 'login',
    component: () => import('../views/LoginView.vue')
  },
  {
    path: '/dashboard',
    name: 'dashboard',
    component: () => import('../views/DashboardView.vue') 
  },
  {
    path: '/findinfo',
    name: 'findinfo',
    component: () => import('../views/FindinfoView.vue')
  },
  {
    path : '/signup',
    name : 'signup',
    component: () => import('../views/SignUp.vue')
  },
  {
    path : '/dashboard',
    name : 'dashboard',
    component: () => import('../views/DashboardView.vue')
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
