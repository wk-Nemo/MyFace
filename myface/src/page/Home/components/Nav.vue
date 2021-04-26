<template>
  <div class="nav">
    <div class="container">
      <a href="#section" :class="{'item': true, 'item-active': activeList === 0}">应用场景</a>
      <a href="#news" :class="{'item': true, 'item-active': activeList === 1}">相关新闻</a>
      <a href="#superiority" :class="{'item': true, 'item-active': activeList === 2}">特色优势</a>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Nav',
  props: {
    activeList: Number
  }
}
</script>

<style lang="scss" scoped>
.nav{
  height: 1rem;
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
      font-size: 0.35rem;
      line-height: 1rem;
      cursor: pointer;
    }
    .item-active{
      font-weight: 800;
      border-bottom: 2px solid black;
    }
  }
}
</style>
