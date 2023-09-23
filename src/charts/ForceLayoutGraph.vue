<template>
    <v-chart class="force_layout_graph" :option="updateOption(dataJson)" v-show="dataJson" />
</template>

<script setup>
import { use } from 'echarts/core'
import { GraphChart } from 'echarts/charts'
import { TitleComponent, TooltipComponent, LegendComponent } from 'echarts/components'
import { CanvasRenderer } from 'echarts/renderers'
import VChart from 'vue-echarts'
import { computed } from 'vue'
import { useDataStore } from '../stores/data.js'

use([TitleComponent, TooltipComponent, LegendComponent, GraphChart, CanvasRenderer])

const dataStore = useDataStore()
const dataJson = computed(() => dataStore.dataJson)
// import dataJson from '../../public/data/test_data.json'

const isEmpty = (obj) => {
    if (!obj) return true
    for (let key of Object.keys(obj)) {
        if (obj[key].length !== 0) return false
    }
    return true
}

const updateOption = (dataJson) => {
    if (isEmpty(dataJson)){
        return {}
    }
    return {
        legend: [{ data: dataJson.categories.map(a => a.name) }],
        series: [
            {
                type: 'graph',
                layout: 'force',
                label: { position: 'right' },
                draggable: true,
                data: dataJson.nodes,
                links: dataJson.links,
                categories: dataJson.categories,
                roam: true,
                force: {

                    repulsion: 200,
                }
            }
        ]
    }
}
// const option = ref({
//     legend: [{data: dataJson.categories.map(a => a.name)}],
//     series: [
//         {
//             type: 'graph',
//             layout: 'force',
//             label: { position: 'right' },
//             draggable: true,
//             data: dataJson.nodes,
//             links: dataJson.links,
//             categories: dataJson.categories,
//             roam: true,
//             force: {

//                 repulsion: 200,
//             }
//         }
//     ]
// })
</script>

<style></style>
