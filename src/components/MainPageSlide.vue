<template>
  <el-carousel :autoplay="false" direction="vertical" type="card" v-show="!isEmpty(dataJson)">
    <el-carousel-item class="mainpage_box">
      <degreeChart />
    </el-carousel-item>
    <el-carousel-item class="mainpage_box">
      <corenessChart />
    </el-carousel-item>
    <el-carousel-item class="mainpage_box">
      <TriangleChart />
    </el-carousel-item>
    <el-carousel-item class="mainpage_box">
      <ShortestPathChart />
    </el-carousel-item>
    <el-carousel-item class="mainpage_box">
      <ClusteringCoefficientChart />
    </el-carousel-item>
  </el-carousel>
</template>

<script setup>
import { computed } from 'vue'
import degreeChart from '../charts/DegreeChart.vue'
import corenessChart from '../charts/CorenessChart.vue'
import TriangleChart from '../charts/TriangleChart.vue'
import ShortestPathChart from '../charts/ShortestPathChart.vue'
import ClusteringCoefficientChart from '../charts/ClusteringCoefficientChart.vue'
import { useDataStore } from '../stores/data.js'
const dataStore = useDataStore()
const dataJson = computed(() => dataStore.dataJson)

const isEmpty = (obj) => {
  if (!obj) return true
  for (let key of Object.keys(obj)) {
    if (obj[key].length !== 0) return false
  }
  return true
}

</script>

<style>
.mainpage_box {
  width: 100%;
  height: 100%;
}

.el-carousel__item:nth-child(2n) {
  background-color: #99a9bf;
  border-radius: 5px;
}

.el-carousel__item:nth-child(2n + 1) {
  background-color: #d3dce6;
  border-radius: 5px;
}
</style>
