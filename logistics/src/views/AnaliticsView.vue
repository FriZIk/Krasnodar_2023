<template>
  <div class="row justify-content-center">
    <div class="col-lg-4">
      <Bar id="my-chart-id" :options="chartOptions" :data="chartData" />
    </div>
    <div class="col-lg-4">
      <Bar id="my-chart-id" :options="chartOptions" :data="chartData" />
    </div>
    <div class="col-lg-4">
      <Bar id="my-chart-id" :options="chartOptions" :data="chartData" />
    </div>
    <div class="col-lg-4">
      <Bar id="my-chart-id" :options="chartOptions" :data="chartData" />
    </div>
    <div class="col-lg-4">
      <Bar id="my-chart-id" :options="chartOptions" :data="chartData" />
    </div>
    <div class="col-lg-4">
      <Bar id="my-chart-id" :options="chartOptions" :data="chartData" />
    </div>
  </div>
</template>

<script>
import { Bar } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale, Colors } from 'chart.js'
import axios from 'axios'


ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale, Colors)

export default {
  name: 'BarChart',
  components: { Bar },

  methods: {
    GetConfigurationFile() {
      var date = document.getElementById("date");
      var from = document.getElementById("from");
      var to = document.getElementById("to");
      var Class = document.getElementById("Class");
      var count = document.getElementById("count");

      console.log(date.value);
      console.log(from.value);
      console.log(to.value);
      console.log(Class.value);
      console.log(count.value);

      axios.get("http://83.221.202.194:2500/backapi//")
        .then((response) => {
          console.log(response);
        })
        .catch((errors) => {
          console.log(errors); // Errors
        });
    }
  },

  data() {
    return {
      chartData: {
        labels: ['January', 'February', 'March'],
        datasets: [{ data: [40, 20, 12] }],
        backgroundColor: '#f87979',
      },
      chartOptions: {
        responsive: true
      }
    }
  }
  
}
</script>