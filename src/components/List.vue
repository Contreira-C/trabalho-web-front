<template>

    <div class="p-4">
    <div class="ps-5 pe-5">
      <div class="container card ">
        <div class="row border"  style="height: 55px">
            <div class="col-12 p-2 d-flex" >
                <button class="btn botao d-flex"  @click=clickAddButton()>
                  <span class="material-icons" style="color:white" @click="isModalOpen=true">
                    add
                  </span>
                </button>
            </div>
        </div>
        
        <div class="row p-2 text-center border align-items-center" style="height: 45px">
          <div v-for="column in columns" class="col" :class="column.class">
            {{ column.label }}
          </div>
        </div>
        
        <slot></slot>
    </div>
    </div>
</div>
</template>
<script>
import axios from 'axios'
import Modal from './Modal.vue'
export default {
  components: {
    Modal
  },
	data() {
		return {
			Lista:
      [
        {
          "nome": "Mizuno",
          "modelo": "Prophecy 11",
          "cor": "Laranja com preto",
          "tamanho": 34,
          "margem": 12,
          "estilo": "Corrida",
          "id": 1
        },
        {
          "nome": "Nike",
          "modelo": "Dunk",
          "cor": "Preto",
          "tamanho": 34,
          "margem": 12,
          "estilo": "Esporte",
          "id": 2
          }
      ],
      isModalOpen: false,
		}
	},
	methods:{
	
      openModal() {
      this.isModalOpen = true
      console.log('rodei')
    },
    clickAddButton() { 
      this.$emit('add-button-callback');
      console.log('rodei') 
    }
	},
  props: {
    columns: { type: Object, default: [] }
  },
  emits: ['onClose', 'add-button-callback']
}
</script>
<style>
.botao {
    background-color: var(--primary);
}

.botao:hover {
    background-color: var(--primary-alt);
}

</style>