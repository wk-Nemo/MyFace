<template>
  <div class='facerecognize'>
    <div class="user-info">
      <div class="user-info-wraper">
        <div class="user-pic-wraper">
          <img class="user-pic" :src="this.$store.state.userPic">
        </div>
        <div class="usermsg-userid">用户ID：{{ userId }}</div>
      </div>
    </div>

    <div class="content">

      <div class="photobox">
        <div id="photo">
          <h3 class="photo-title">请选择对比的照片</h3>
          <div
            class="container"
          >
            <img v-if="hasImg" src="https://cdn.ai.qq.com/ai/page/product/face/img/banner-ico-7706573879.png">
            <img
              id="Img"
            >
          </div>
        </div>
        <div class="inputwrap">
          <div class="upload">
            上传照片
            <input
              type="file"
              id="imageUpload"
              @change="onImgchange"
            >
          </div>
          <!-- 负数据加密 -->
          <div
            class="upload"
            @click="sendNDB"
          >
            负数据库
          </div>
          <!-- 局部排序加密 -->
          <div class="upload"
            @click="getOrderingEncryptData"
          >
            局部排序
          </div>
        </div>
      </div>

      <div id="origin" v-if="isShowOrigin">
      </div>

      <div class="ndbwraper">
        <div id="ndb0" class="ndb" v-if="isShowEncrypt"></div>
      </div>
      <div class="ndbwraper">
        <div id="ndb1" class="ndb" v-if="isShowEncrypt"></div>
      </div>

      <div id='order' class="encryptdata" v-if="isShowOrder">
      </div>
    </div>
  </div>
</template>

<script>
import * as faceapi from 'face-api.js'
import { getModels } from '../../util/getface.js'
import { MyNDB } from '../../util/getNDB.js'
import axios from 'axios'

const encrypt = require('ordering-encrypt')

export default {
  name: 'FaceRecognize',
  data () {
    return {
      num: 0,
      userId: '',
      originData: [],
      encryptData: '',
      Pos: [],
      orderingEncryptData: '',
      imgUrl: '',
      hasImg: true,
      descriptor: [],
      before_s: '',
      isShowOrigin: false,
      isShowEncrypt: false,
      isShowOrder: false,
      data: {
        userID: undefined,
        NDB: '',
        flag: [],
        specific: ''
      }
    }
  },
  methods: {
    onImgchange: async function (e) {
      // 获取照片
      const image = await faceapi.bufferToImage(e.target.files[0])

      // 判断是否上传了照片
      var flag
      if (this.hasImg === true) {
        flag = true
        this.hasImg = false
      } else {
        flag = false
      }

      // 获取img元素
      const img = document.querySelector('#Img')
      img.setAttribute('src', image.src)

      // 创建画布
      const canvas = faceapi.createCanvasFromMedia(img)
      const displaySize = {
        width: img.width,
        height: img.height
      }
      // canvas.setAttribute('class', 'mycanvas')
      canvas.style = `position:absolute; left:50%; top:0; transform: translate(-50%)`
      const photodiv = document.querySelector('#photo .container')
      // console.log(photodiv)
      if (flag === false) {
        document.querySelector('#photo .container').removeChild(document.querySelector('#photo .container').children[1])
      }
      photodiv.append(canvas)
      // 设置面部特征点和画布匹配
      faceapi.matchDimensions(canvas, displaySize)

      // 获取照片上的所有人脸并存入数组
      const detections = await faceapi.detectAllFaces(image).withFaceLandmarks().withFaceDescriptors()

      this.descriptor = []

      // 匹配画布尺寸
      const resizedDetections = faceapi.resizeResults(detections, displaySize)
      resizedDetections.forEach(detection => {
        const box = detection.detection.box
        const drawBox = new faceapi.draw.DrawBox(box, {
          label: 'face'
        })
        drawBox.draw(canvas)
        faceapi.draw.drawDetections(canvas, resizedDetections)
        faceapi.draw.drawFaceLandmarks(canvas, resizedDetections)
        this.descriptor.push(detection.descriptor)
      })
      console.log(this.descriptor[0])
      this.originData = this.descriptor[0]
      this.isShowOrigin = true
      setTimeout(this.drawOriginData, 0)
    },
    sendNDB: function () {
      if (this.descriptor[0] === undefined) {
        alert('请先上传照片')
      } else {
        let ndb = new MyNDB(this.descriptor[0])
        this.Pos = ndb.Pos
        this.encryptData = ndb.NDB
        this.isShowEncrypt = true
        this.data.NDB = ndb.NDB
        this.data.flag = ndb.flag
        this.data.specific = ndb.specific
        this.data.userID = this.userId
        setTimeout(this.drawNdbData, 0)
        this.postNDB()
      }
    },
    getOrderingEncryptData: function () {
      if (this.descriptor[0] === undefined) {
        alert('请先上传照片')
      } else {
        let ndb = new MyNDB(this.descriptor[0])
        // console.log(ndb.before_s);
        let data = String(ndb.before_s).split('').map(a => { return Number(a) })
        console.log(data)
        let p = new Array(data.length).fill(0)
        let final = encrypt.decode(data, p)
        // console.log('encrypt data:', final.join(''), 'keydata:', p.join(''))
        // final为人脸加密后的结果，p为密钥
        // let saveData = {
        //   username: '12312313',
        //   part: final.join(''),
        //   p: p.join('')
        // }
        this.orderingEncryptData = final
        this.isShowOrder = true
        setTimeout(this.drawOrderChart, 0)
        this.postOrder()
      }
    },
    postOrder: function () {
      axios({
        method: 'post',
        url: 'http://myface.kingfish404.cn/faceRecognize_part/',
        dataType: 'json',
        data: {
          'userID': this.$store.state.userID,
          'part': JSON.stringify(this.orderingEncryptData)
        }
      }).then((response) => {
        console.log(response)
        if (response.data.result === true) {
          alert('识别成功')
        } else {
          alert('识别失败')
        }
      })
    },
    drawOrderChart: function () {
      // console.log('drawOrderChart>query#order', document.querySelector('#order'))
      let orderCharts = this.$echarts.init(document.querySelector('#order'))
      let xAxisData = []
      for (let i = 0; i < this.orderingEncryptData.length; i++) {
        xAxisData.push(i)
      }
      // 绘制图表
      orderCharts.setOption(
        {
          title: { text: '局部排序加密脸型数据' },
          xAxis: {
            type: 'category',
            data: xAxisData
          },
          yAxis: {
            type: 'value'
          },
          series: [{
            data: this.orderingEncryptData,
            type: 'line',
            smooth: true
          }]
        }
      )
    },
    postNDB: function () {
      axios({
        method: 'post',
        url: 'http://myface.kingfish404.cn/faceRecognize_native/',
        dataType: 'json',
        data: JSON.stringify(this.data)
      }).then((response) => {
        console.log(response)
        if (response.data.result === true) {
          alert('识别成功')
        } else {
          alert('识别失败')
        }
      })
    },
    getOriginData: function () {
      var file = document.querySelector('input[type=file]').files[0]
      if (!file) {
        this.originData = '请先选择图片!'
      } else {
        this.originData = this.descriptor[0]
      }
      this.isShowOrigin = !this.isShowOrigin
    },
    getEncryptData: function () {
      var file = document.querySelector('input[type=file]').files[0]
      if (!file) {
        this.encryptData = '请先选择图片!'
      } else {
        if (this.encryptData === '') {
          this.encryptData = '请生成负数据库!'
        }
      }
      this.isShowEncrypt = !this.isShowEncrypt
    },
    drawOriginData: function () {
      // 基于准备好的dom，初始化echarts实例
      let myChart = this.$echarts.init(document.querySelector('#origin'))
      let data = []
      for (let i = 0; i < 128; i++) {
        data[i] = i + 1
      }
      let originData = []
      for (let i = 0; i < 128; i++) {
        originData.push(this.originData[i])
      }
      // 绘制图表
      myChart.setOption({
        title: { text: '原始人脸数据' },
        xAxis: {
          data: data
        },
        yAxis: {},
        series: [{
          name: '原始数据',
          type: 'bar',
          data: originData
        }]
      })
    },
    drawNdbData: function () {
      let ndbChart0 = this.$echarts.init(document.querySelector('#ndb0'))
      let ndbChart1 = this.$echarts.init(document.querySelector('#ndb1'))
      let data = []
      for (let i = 0; i < 1280; i++) {
        data[i] = i + 1
      }
      console.log(this.Pos)
      let data0 = []
      for (let i = 0; i < 1280; i++) {
        data0[i] = this.Pos[i][0]
      }
      let data1 = []
      for (let i = 0; i < 1280; i++) {
        data1[i] = this.Pos[i][1]
      }
      console.log(data1)
      let option0 = {
        title: { text: '负数据加密脸型数据' },
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'shadow'
          }
        },
        legend: {
          data: ['取0次数']
        },
        grid: {
          left: '3%',
          right: '4%',
          bottom: '3%',
          containLabel: true
        },
        xAxis: [
          {
            type: 'category',
            data: data
          }
        ],
        yAxis: [
          {
            type: 'value'
          }
        ],
        series: [
          {
            name: '取0次数',
            type: 'bar',
            emphasis: {
              focus: 'series'
            },
            data: data0
          }
        ]
      }
      let option1 = {
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'shadow'
          }
        },
        legend: {
          data: ['取1次数']
        },
        grid: {
          left: '3%',
          right: '4%',
          bottom: '3%',
          containLabel: true
        },
        xAxis: [
          {
            type: 'category',
            data: data
          }
        ],
        yAxis: [
          {
            type: 'value'
          }
        ],
        series: [
          {
            name: '取1次数',
            type: 'bar',
            emphasis: {
              focus: 'series'
            },
            data: data1
          }
        ]
      }
      ndbChart0.setOption(option0)
      ndbChart1.setOption(option1)
    }
  },
  mounted () {
    getModels()
    this.userId = localStorage.getItem('NDB_userID')
  }
}
</script>

<style lang='scss' scoped>
.line {
  border-bottom: 1px solid white;
}
.facerecognize {
  color: black;
  .user-info {
    background: url('https://static3.sycdn.imooc.com/static/img/u/temp1.png') no-repeat center top #000;
    background-size: cover;
    height: 100px;
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    .user-info-wraper {
      width: 60%;
      position: relative;
      height: 100%;
      .user-pic-wraper {
        position: absolute;
        width: 100px;
        height: 100px;
        top: 20%;
        border-radius: 50%;
        border: 2px solid white;
        box-shadow: 0 4px 8px 0 rgb(7, 17, 27);
        background: white;
        overflow: hidden;
        display: flex;
        justify-content: center;
        align-items: center;
        .user-pic {
          text-align: center;
          height: 100px;
        }
      }
    }
    .usermsg-userid {
      color: white;
      font-size: 20px;
      font-weight: 600;
      position: absolute;
      left: 130px;
      top: 30%;
    }
  }
  .content {
    width: 60%;
    margin: 50px auto;
    padding-bottom: 50px;
    .photobox {
      border-radius: 4px;
      box-shadow: 0 8px 14px 0 rgb(42, 44, 46);
      #photo {
        position: relative;
        text-align: center;
        .photo-title{
          padding: 20px 0 10px 0;
          font-size: 20px;
          font-weight: 900;
          line-height: 60px;
        }
        .container {
          height: 400px;
          overflow: auto;
          display: block;
          margin: 0 auto;
          position: relative;
          background: rgb(191, 197, 201);
          #Img {
            height: 100%;
          }
        }
      }
      .inputwrap{
        display: flex;
        justify-content: center;
        align-items: center;
        .upload{
          padding: 4px 10px;
          margin: 10px 45px;
          height: 20px;
          line-height: 20px;
          position: relative;
          cursor: pointer;
          color: #888;
          background: #fafafa;
          border: 1px solid #ddd;
          border-radius: 4px;
          overflow: hidden;
          display: inline-block;
          *display: inline;
          *zoom: 1;
          width: auto;
          #imageUpload {
            position: absolute;
            font-size: 100px;
            right: 0;
            top: 0;
            opacity: 1;
            filter: alpha(opacity=0);
            cursor: pointer
          }
        }
        .upload:hover{
          color: rgb(200, 22, 35);
          background: #eee;
          border-color: #ccc;
          text-decoration: none;
          cursor: pointer;
        }
      }
    }
    #origin {
      margin: 50px 0;
      height: 500px;
    }
    .ndbwraper {
      overflow: auto;
      width: 100%;
      .ndb {
        margin: 50px 0;
        height: 500px;
        width: 100%;
      }
    }
  }
}

#order{
  overflow: auto;
  height: 500px;
}

.encryptdata {
  height: 350px;
}

.encryptbtn {
  padding: 10px;
}

.encryptdata {
  height: 350px;
  overflow: auto;
  font-family: monospace;
  margin-top: 10px;
  padding-left: 10px;
  .errorencrypt {
    font-size: 20px;
    font-weight: 800;
    text-align: center;
    line-height: 350px;
  }
}
.data-desc{
  word-break: break-word;
}
</style>
