import { createRouter, createWebHistory } from 'vue-router'

const routes = [

  {
    path: '/dashboard',
    name: 'dashboard',
    component: () => import('../views/DashboardView.vue')
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
    path: '/qna',
    name: 'qna',
    component: () => import('../views/QnaView.vue'),
  },
  {
    path: '/qna/create',
    name: 'qnacreate',
    component: () => import('../views/QnaCreate.vue'),
  },
  {
    path: '/qna/:id',
    name: 'qnadetail',
    component: () => import('../views/QnaDetail.vue'),
  },
  {
    path: '/qna/update/:id',
    name: 'qnaupdate',
    component: () => import('../views/QnaUpdate.vue'),
  },
  {
    path : '/faq',
    name : 'faq',
    component: () => import('../views/FaqView.vue')
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
    path: '/findinfo',
    name: 'findinfo',
    component: () => import('../views/FindinfoView.vue')
  },
  {
    path : '/signup',
    name : 'signup',
    component: () => import('../views/SignUp.vue')
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
