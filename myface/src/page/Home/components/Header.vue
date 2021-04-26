<template>
  <div class="header">
    <div class="content">
      <div class="title">隐私安全的人脸识别</div>
      <div class="info">人脸检测与属性分析、人脸对比、人脸搜索、活体检测等能力。灵活应用于金融、泛安防、零售等行业场景，满足身份核验、人脸考勤、闸机通行等业务需求</div>
      <div class="news">不同于传统人脸识别方案,我们在最重要的数据处理环节选择将用户数据不可逆加密后存储,即使暴露也不必担心安全问题</div>
      <div class="btn">
        <div class="btn-primary" @click="ready">立即使用</div>
        <a href="https://github.com/wk-Nemo/MyFace" class="btn-document">技术文档</a>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Header',
  methods: {
    ready: function () {
      this.$router.push('/facephoto')
    }
  }
}
</script>

<style lang="scss" scoped>
.header {
  background-image: url("https://ai.bdstatic.com/file/2DB693AACDDE49C0940410B3FB74DFA0") !important;
  height: 10rem;
  background: no-repeat 50%;
  background-size: cover;
  overflow: hidden;
  position: relative;
  .content {
    overflow: hidden;
    position: absolute;
    top: 50%;
    left: 50%;
    width: 30%;
    transform: translate(-50%,-50%);
    padding-right: 15rem;
    .title {
      font-size: 1rem;
      line-height: 1.8rem;;
    }
    .info {
      font-size: 0.3rem;
      line-height: 0.4rem;
      margin: 10px 0;
    }
    .news {
      font-size: 0.3rem;
      line-height: 0.4rem;
      color: #faad15;
      margin: 10px 0;
    }
    .btn {
      display: flex;
      font-size: 0.4rem;
      margin-top: 26px;
      .btn-primary {
        background-color: rgb(3,111,226);
        padding: 7px 15px;
        margin-right: 40px;
        font-weight: 100;
      }
      .btn-primary:hover {
        cursor: pointer;
        background-color: rgb(28,136,252);
      }
      .btn-document {
        background-color: #ccc;
        padding: 7px 15px;
        font-weight: 100;
      }
      .btn-document:hover {
        background: white;
        color:black;
        cursor: pointer;
      }
    }
  }
}
</style>
