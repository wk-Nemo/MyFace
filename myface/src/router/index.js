import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/page/Home/Home'
import FacePhoto from '@/page/facephoto/FacePhoto'
import FaceVideo from '@/page/facevideo/FaceVideo'
import FaceRecognize from '@/page/facerecognize/FaceRecognize'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      redirect: '/home'
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
