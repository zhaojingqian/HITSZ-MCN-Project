<template>
  <el-container ref="mainpage_container" class="mainpage_container">
    <el-header class="mainpage_header">
      <mainHeader />
    </el-header>
    <el-main class="mainpage_main">
      <div class="mainpage_bar">
        <mainBar />
      </div>
      <div class="mainpage_info">
        <mainSlide class="mainpage_slide" />
        <mainGraph class="mainpage_forced_graph" />
      </div>
    </el-main>
  </el-container>
</template>

<script setup>
import mainHeader from './components/MainPageHeader.vue'
import mainBar from './components/MainPageBar.vue'
import mainGraph from './charts/ForceLayoutGraph.vue'
import mainSlide from './components/MainPageSlide.vue'

import { onMounted } from 'vue'
import axios from 'axios'
import { useDataStore } from './stores/data.js'
const dataStore = useDataStore()

const getInitDataList = async () => {
  await axios
    .get('http://127.0.0.1:8280/get_data_list')
    .then((res) => {
      dataStore.resetDataList(res.data)
    })
    .catch((err) => {
      console.log(err)
    })
}
onMounted(() => {
  getInitDataList()
})
</script>

<style>
.mainpage_main {
  display: flex;
  flex-direction: column;
  justify-content: center;
  /* margin-left: 3%; */
  gap: 20px;
  padding: 10px;
}

.mainpage_bar {
  display: flex;
  flex-direction: row;
  justify-content: center;
  gap: 100px;
  padding-bottom: 10px;
  border-bottom: 2px solid #f2f0f0;
}

.mainpage_info {
  display: flex;
  flex-direction: row;
  justify-content: center;
  gap: 30px;
}

.mainpage_forced_graph {
  width: 60%;
  height: 80vh;
  border: 3px solid #f2f0f0;
  border-radius: 5px;
}

.mainpage_slide {
  width: 40%;
  height: 80vh;

  display: flex;
  flex-direction: column;
  justify-content: space-between;
  gap: 15px;
}
</style>
