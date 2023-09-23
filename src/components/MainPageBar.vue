<template>
    <el-button type="primary" @click="handleClick">DATA 1</el-button>
    <el-button @click="handleClick2">DATA 2</el-button>
    <el-upload v-model:file-list="fileList" class="upload-demo"
        :action="storeData" multiple :on-preview="handlePreview"
        :on-remove="handleRemove" :before-remove="beforeRemove" :limit="1" :on-exceed="handleExceed">
        <el-button type="primary">Click to upload</el-button>
    </el-upload>
</template>

<script setup>
import { ref } from 'vue'


import axios from 'axios'
import { useDataStore } from '../stores/data.js'

const dataStore = useDataStore()

const passDataJson = async (data_path) => {
    await axios
        .get(data_path)
        .then((res) => {
            dataStore.setDataJson(res.data)
        })
        .catch((err) => {
            console.log(err)
        })
}

const handleClick = () => {
    dataStore.setDataPath('./data/test_data.json')
    passDataJson(dataStore.getDataPath())
}

const handleClick2 = () => {
    dataStore.setDataPath('./data/cora_data.json')
    passDataJson(dataStore.getDataPath())
}

const storeData = (file) => {
    console.log(file)
}

</script>

<style></style>