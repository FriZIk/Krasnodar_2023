<template>
  <div class="row justify-content-center">
    <div class="col-lg-4">
      <Bar id="my-chart-id" :options="chartOptions" :data="chartData" />
    </div>
    <div class="col-lg-4">
      <Bar id="my-chart-id" :options="chartOptions" :data="chartData1" />
    </div>
    <div class="col-lg-4">
      <Bar id="my-chart-id" :options="chartOptions" :data="chartData2" />
    </div>
    <div class="col-lg-4">
      <Bar id="my-chart-id" :options="chartOptions" :data="chartData3" />
    </div>
    <div class="col-lg-4">
      <Bar id="my-chart-id" :options="chartOptions" :data="chartData4" />
    </div>
    <div class="col-lg-4">
      <Bar id="my-chart-id" :options="chartOptions" :data="chartData5" />
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
        datasets: [{
          data: [40, 20, 12],
          backgroundColor: '#77b7cd',
          label: 'Кол-во билетов по месяцам',
        }],
      },
      chartData1: {
        labels: ['Plac', 'Kupe', 'CB'],
        datasets: [{ data: [30, 75, 10], backgroundColor: '#3F72AF', label: 'Класс обслуживания', }],
      },
      chartData2: {
        labels: ['<18', '18-25', '25-59', '60+'],
        datasets: [{ data: [35, 70, 164, 17], backgroundColor: '#00B8A9', label: 'Возраст купившего билет', }],
      },
      chartData3: {
        labels: ['pos', 'neu', 'neg'],
        datasets: [{ data: [19, 60, 23], backgroundColor: '#FF9999', label: 'Кол-во событий', }],
        // backgroundColor: '#b82828',
      },
      chartData4: {
        labels: ['<1500', '1500-4000', '4000+'],
        datasets: [{ data: [20, 35, 16], backgroundColor: '#F73859', label: 'Распределение по цене билетов', }],
        // backgroundColor: '#b82828',
      },
      chartData5: {
        labels: ['1', '1-3', '3+'],
        datasets: [{ data: [53, 19, 7], backgroundColor: '#FF6F3C', label: 'Кол-во купленных билетов за раз', }],
        // backgroundColor: '#b82828',
      },
      chartOptions: {
        responsive: true,
        legend: {
          display: false // отключает легенду, бесполезную когда на графике одна линия
        },

      }
    }
  }
}
</script>
