<template>
  <div class="facerecognize">
    <h2>信息</h2>
    <p>用户ID：</p>
    <h2>用户头像</h2>
    <h2>识别对比（密文）</h2>
    <hr />
    <div class="upload-area">
      <p class="info">请限制照片大小在6M之内<span>0/1</span></p>
      <div class="img-area"></div>
    </div>
    <hr />
    <button>上传</button>
    <h2>原始脸型数据:</h2>

    <button>点击获取</button>
    <h2>加密脸型数据:</h2>

    <button>点击获取</button>
  </div>
</template>

<script>
export default {
  name: 'FaceRecognize'
}
</script>

<style lang="scss" scoped>
.facerecognize {
  background: rgb(51, 51, 51);
  height: 100%;
  color: white;
  max-width: 800px;
  margin: 0 auto;
}
h2 {
  font-size: x-large;
  margin: 0.5rem;
}
p {
  margin: 0.5rem;
}
button {
  text-align: center;
  padding: 0.5em 1em;
  margin: auto;
  display: block;
  background-color: rgb(51, 51, 51);
  border: 2px solid white;
  color: white;
  border-radius: 5px;
  cursor: pointer;
}

.info {
  text-align: center;
}

.info span {
  float: right;
}

.upload-area {
  margin: 0.5rem;
}

.img-area {
  width: 100px;
  height: 100px;
  border: 5px solid white;
  margin: auto;
  cursor: pointer;
}
</style>
