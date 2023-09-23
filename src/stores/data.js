import { ref } from 'vue'
import { defineStore } from 'pinia'

export const useDataStore = defineStore('data', () => {
    const dataPath = ref('')
    const dataJson = ref({})

    const setDataPath = (path) => {
        dataPath.value = path
    }

    const getDataPath = () => {
        return dataPath.value
    }

    const setDataJson = (data) => {
        dataJson.value = data
    }
    const getDataJson = () => {
        return dataJson.value
    }

    return {
        dataPath,
        dataJson,
        
        setDataPath,
        getDataPath,
        setDataJson,
        getDataJson,
    }
})
