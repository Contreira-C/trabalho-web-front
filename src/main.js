import { createApp } from 'vue';
import App from './App.vue';
import axios from 'axios';
import 'bootstrap';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap/dist/js/bootstrap.js';
import router from './router';

const apiAxios = axios.create({
  baseURL: '/api/',
  headers: {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Headers": "Authorization",
  }
});

const app = createApp(App);

app.config.globalProperties.$apiAxios = apiAxios;

app.use(router);
app.mount('#app');







