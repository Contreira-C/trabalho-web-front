<template>
    <Modal
      :isModalOpen="isModalOpen"
      @onClose="closeModal"
      :isEdit="editardata"
      :objectId="editarId"
      />
      
    <List
      @add-button-callback="openModal(false)"
      :columns="
      [
        { label: 'Id' },
        { label: 'Nome' },
        { label: 'Cor' },
        { label: 'Tamanho' },
        { label: 'Categoria' },
        { label: 'Quantidade' },
        { label: '', class: 'col-1 ms-auto' }
      ]"
      >
      <div v-for="item in Lista" class="row border p-2 bg-light text-center align-items-center" style="height: 55px">
        <div class="col mt-2">
          {{ item.id }}
        </div>
        <div class="col mt-2">
          {{ item.marca }}
        </div>
        <div class="col mt-2">
          {{ item.cor }}
        </div>
        <div class="col mt-2">
          {{ item.tamanho }}
        </div>
        <div class="col mt-2">
          {{ item.categoria }}
        </div>
        <div class="col mt-2">
          {{ item.quantidade }}
        </div>
        <div class="col-1 ms-auto">
          <button class="btn botao1 d-flex" @click="openModal(true,item.id)">
            <span class="material-icons" style="color: white">
              edit
            </span>
          </button>
        </div>
      </div>
    </List>
  </template>
  
  <script>
  import List from '../../components/List.vue'
  import Modal from './modalProdutos.vue'
  
  export default {
    components: {
      List,
      Modal
    },
    mounted() {
      this.requisicao()

    },
    data() {
      return {
        Lista: [],
        isModalOpen: false,
        editardata: false,
        editarId: null
      }
    },
    methods: {
      requisicao: async function() {
        try {
          const response = await this.$apiAxios.get('http://localhost:5000/estoque', {
            headers: {
              'Access-Control-Allow-Origin': '*', // Permitir todas as origens.
              'Access-Control-Allow-Methods': 'GET' // Permitir apenas o método GET.
            }
          });
          this.Lista = response.data;
        } catch (error) {
          console.error(error);
        }
      },

      openModal(isEdit, idObjeto = null) {
        this.editardata = isEdit;
        this.editarId = idObjeto;
        this.isModalOpen = true;
      },
      closeModal() {
        this.isModalOpen = false;
        this.editarId = 0;
        this.requisicao()

      }
    }
  }
  </script>
  
  <style>
  .botao1 {
    background-color: var(--grey);
  }
  
  .botao1:hover {
    background-color: var(--grey-alt);
  }
  </style>
  