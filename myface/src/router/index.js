import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/page/Home/Home'
import FacePhoto from '@/page/facephoto/FacePhoto'
import FaceVideo from '@/page/facevideo/FaceVideo'
import FaceRecognize from '@/page/facerecognize/FaceRecognize'
import Login from '@/page/user/Login'
import Signup from '@/page/user/Signup'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      redirect: '/home'
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/signup',
      name: 'Signup',
      component: Signup
    },
    {
      path: '/home',
      name: 'Home',
      component: Home
    },
    {
      path: '/facephoto',
      name: 'FacePhoto',
      component: FacePhoto
    },
    {
      path: '/facevideo',
      name: 'FaceVideo',
      component: FaceVideo
    },
    {
      path: '/facerecognize',
      name: 'FaceRecognize',
      component: FaceRecognize
    }
  ]
})
