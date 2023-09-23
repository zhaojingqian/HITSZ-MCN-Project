<script setup>
// components
import mainHeader from './components/MainPageHeader.vue'
import mainBar from './components/MainPageBar.vue'
import forceLayoutGraph from './charts/ForceLayoutGraph.vue'

// references

// import lodash from 'lodash'
// import { ref, onMounted, onBeforeUnmount } from 'vue'

// const debouncedHandleWindowResize = lodash.debounce(, 10)

// onMounted(() => {
//   window.addEventListener('resize', debouncedHandleWindowResize);
// })
// onBeforeUnmount(() => {
//   window.removeEventListener('resize', debouncedHandleWindowResize);
// })
</script>

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
                <div class="mainpage_other_info">
                    <h1 class="mainpage_box">Other Info1</h1>
                    <h1 class="mainpage_box">Other Info2</h1>
                    <h1 class="mainpage_box">Other Info3</h1>
                    <h1 class="mainpage_box">Other Info4</h1>
                </div>
                <forceLayoutGraph class="mainpage_forced_graph" />
            </div>
        </el-main>
    </el-container>
</template>

<style>
.mainpage_main {
    display: flex;
    flex-direction: column;
    justify-content: center;
    /* margin-left: 3%; */
    gap: 20px;
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
    height: 82vh;
    border: 3px solid #f2f0f0;
    border-radius: 5px;
}

.mainpage_other_info {
    width: 40%;

    display: flex;
    flex-direction: column;
    justify-content: space-between;
    gap: 15px;
}

.mainpage_box {
    width: 100%;
    height: 25%;

    text-align: center;
    border: 3px solid #f2f0f0;
    border-radius: 5px;
}
</style>
