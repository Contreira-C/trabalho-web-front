<template>
    <div class="container">
      <img src="../assets/logo.png" alt="Vue" class="img-fluid d-block mx-auto" style="width: 150px; height: 150px; margin-top: 20px; margin-bottom: 20px;"/>
      <form @submit.prevent="login" class="mt-4">
        <div class="mb-3">
          <label for="username" class="form-label">Username:</label>
          <input type="text" id="username" placeholder="admin" v-model="username" class="form-control" />
        </div>
        <div class="mb-3">
          <label for="password" class="form-label">Password:</label>
          <input type="password" id="password" placeholder="password" v-model="password" class="form-control" />
        </div>
        <button type="submit" class="btn botao">Login</button>
      </form>
      <p v-if="errorMessage" class="text-danger mt-3">{{ errorMessage }}</p>
    </div>
  </template>
  
  <script>
  import { ref } from 'vue';
  
  export default {
    name: 'Login',
    setup() {
      const username = ref('');
      const password = ref('');
      const errorMessage = ref('');
  
      const login = () => {
        if (username.value === 'admin' && password.value === 'password') {
          window.location.href = "/estoque";
          errorMessage.value = '';
        } else {
          errorMessage.value = 'Tente novamente.';
        }
      };
  
      return {
        username,
        password,
        errorMessage,
        login,

      };
    },
  };
  </script>
  
  <style>
  .botao {
    background-color: var(--primary);
  }
  
  .botao:hover {
    background-color: var(--primary-alt);
  }
  
  .form-label {
    color: white;
  }
  
  .container {
    max-width: 400px;
    margin: 0 auto;
    padding-top: 100px;
  }
  
  .text-center {
    text-align: center;
  }
  
  .mt-4 {
    margin-top: 1.5rem;
  }
  
  .mb-3 {
    margin-bottom: 1rem;
  }
  
  .form-label {
    font-weight: bold;
  }
  
  .form-control {
    width: 100%;
  }
  
  .btn-primary {
    width: 100%;
  }
  
  body {
    background-color: var(--dark-alt);
  }

  </style>