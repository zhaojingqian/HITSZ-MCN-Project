<template>
  <el-menu
    :default-active="activeIndex"
    class="mainpage_header_meau"
    mode="horizontal"
    :ellipsis="false"
    @select="handleSelect"
  >
    <el-menu-item index="0" @click="testPing"> LOGO </el-menu-item>
    <div class="mainpage_header_menu_flex_grow"></div>
    <el-menu-item index="1"> Home </el-menu-item>
    <el-menu-item index="2"> About </el-menu-item>
    <el-menu-item index="3"> Contact </el-menu-item>
  </el-menu>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
const activeIndex = ref('1')
const handleSelect = (index) => {
  activeIndex.value = index
}

const testPing = async () => {
  await axios
    .get('http://10.249.46.195:8280/test')
    .then((res) => {
      console.log(res.data)
    })
    .catch((err) => {
      console.log(err)
    })
}
</script>

<style>
.mainpage_header_menu_flex_grow {
  flex-grow: 1;
}
</style>
