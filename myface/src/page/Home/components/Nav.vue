<template>
  <div class="nav">
    <div class="container">
      <div class="item item-active">应用场景</div>
      <div class="item">相关新闻</div>
      <div class="item">特色优势</div>
      <div class="item">支持与交流</div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Nav'
}
</script>

<style lang="scss" scoped>
.nav{
  height: 50px;
  box-shadow: 0 2px 6px 0 rgb(202, 199, 199);
  position: relative;
  .container{
    position: absolute;
    left: 50%;
    transform: translate(-50%);
    .item{
      color: black;
      display: inline-block;
      margin-left: 11px;
      margin-right: 31px;
      line-height: 54px;
      cursor: pointer;
      font-size: 10px;
    }
    .item-active{
      font-weight: 800;
    }
  }
}
</style>
