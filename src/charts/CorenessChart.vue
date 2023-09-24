<template>
  <v-chart
    class="coreness_chart"
    :option="updateOption(corenessData)"
    autoresize
  />
</template>

<script setup>
import {computed} from 'vue'
import { use } from 'echarts/core'
import { BarChart } from 'echarts/charts'
import { TitleComponent, TooltipComponent, GridComponent } from 'echarts/components'
import { CanvasRenderer } from 'echarts/renderers'
import VChart from 'vue-echarts'
import { useDataStore } from '../stores/data.js'
use([TitleComponent, TooltipComponent, GridComponent, BarChart, CanvasRenderer])

const dataStore = useDataStore()
const corenessData = computed(() => dataStore.getCorenessData())

const updateOption = (corenessData) => {
  return {
    title: {
      text: ' Corness Distribution',
      left: 'center',
      top: '5px'
    },
    tooltip: {
      trigger: 'item',
      formatter: '{b} : {c}'
    },
    xAxis: {
      type: 'category',
      name: 'Coreness',
      nameLocation: 'middle',
      nameGap: 30,
      data: corenessData.coreness
    },
    yAxis: {
      type: 'value',
      name: 'Number of Nodes',
      nameLocation: 'middle',
      nameGap: 40
    },
    series: [
      {
        name: 'Coreness',
        type: 'bar',
        data: corenessData.count
      }
    ]
  }
}
</script>
