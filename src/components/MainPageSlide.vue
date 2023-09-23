<template>
  <el-carousel :autoplay="false" direction="vertical" type="card">
    <el-carousel-item class="mainpage_box" v-for="item in 6" :key="item">
      <h3 class="mainpage_box" text="2xl" justify="center">{{ item }}</h3>
    </el-carousel-item>
  </el-carousel>
</template>

<script setup>

</script>

<style>

.mainpage_box {
  width: 100%;
  height: 100%;
}

.el-carousel__item h3 {
  color: #475669;
  opacity: 0.75;
  line-height: 200px;
  margin: 0;
  text-align: center;
}

.el-carousel__item:nth-child(2n) {
  background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n + 1) {
  background-color: #d3dce6;
}
</style>
