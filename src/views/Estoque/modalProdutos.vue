<template>
    <modal
    :statusmodalopen="isModalOpen"
    @closemodal="$emit('onClose');"
    @salvar="salvar()"
    @deletar="deletar()"
    :title="titulo"
    >
        <div class="mb-3 col-6">
                <label  class="form-label">Marca</label>
                <input class="form-control" placeholder="Digite a marca" v-model="dataForm.marca">
            </div>
            <div class="mb-3 col-6">
                <label  class="form-label">Modelo</label>
                <input class="form-control"  placeholder="Digite o modelo" v-model="dataForm.modelo">
            </div>
            <div class="mb-3 col-6">
                <label  class="form-label">Cor</label>
                <input class="form-control"  placeholder="Digite a cor" v-model="dataForm.cor">
            </div>
            <div class="mb-3 col-6">
                <label  class="form-label">Tamanho</label>
                <input class="form-control"  placeholder="Escolha o tamanho" v-model="dataForm.tamanho">
            </div>
            <div class="mb-3 col-6">
                <label  class="form-label">Categoria</label>
                <input class="form-control"  placeholder="Escolha o estilo" v-model="dataForm.categoria">
            </div>
            <div class="mb-3 col-6">
                <label  class="form-label">Quantidade</label>
                <input class="form-control"  placeholder="Digite a quantidade" v-model="dataForm.quantidade">
            </div>
    </modal>
</template>
<script>
import modal from  '../../components/Modal.vue'
export default {
    components: {
        modal
    },
    mounted(){
    },
    data(){
        return{
            dataForm:{
                marca: '',
                modelo: '',
                cor: '',
                tamanho: '',
                margem: '',
                categoria: '',
                quantidade: '',
            },
            titulo:'Cadastro de produto'
        }
    },
    
    watch: {
        isEdit(newVal) {
            if (newVal && this.objectId) {
                this.titulo = 'Editar Produto'
                const response = this.$apiAxios.get('http://localhost:5000/estoque/'+this.objectId)
                const content = response.data

                this.dataForm.marca = content.marca
                this.dataForm.modelo = content.modelo
                this.dataForm.cor = content.cor
                this.dataForm.tamanho = content.tamanho
                this.dataForm.categoria = content.categoria
                this.dataForm.quantidade = content.quantidade
            }else{
                this.freshstart()
                this.titulo = 'Cadastro de produto'
            }
        }
    },

    watch: {
        isEdit(newVal) {
            if (newVal && this.objectId) {
                this.titulo = 'Editar Fornecedor'
                
            }else{
                this.titulo = 'Cadastrar Fornecedor'
            }
        }
    },
    props: {
        isModalOpen: {
            type: Boolean, 
            default: false 
        },
        isEdit: {
            type: Boolean,
            default: false
        },
        objectId: {
            type: Number
        }
    },
    methods:{
        freshstart(){
            this.dataForm.marca = ''
            this.dataForm.modelo = ''
            this.dataForm.cor = ''
            this.dataForm.tamanho = ''
            this.dataForm.categoria = ''
            this.dataForm.quantidade = ''
        },
        salvar: async function()
      {
        const params = {
            'marca': this.dataForm.marca,
            'modelo': this.dataForm.modelo,
            'cor': this.dataForm.cor,
            'tamanho': this.dataForm.tamanho,
            'categoria': this.dataForm.categoria,
            'quantidade': this.dataForm.quantidade,
        }
        
        try {
          if(this.idEditar){
            await this.$apiAxios.put('http://localhost:5000/estoque'+ this.objectId, params);
          }else{
            await this.$apiAxios.post('http://localhost:5000/estoque', params);
        }
        } catch (error) { console.log('Falha na requisição') }

        this.$emit('onClose');
      },
      deletar: async function(){
        try {
            await this.$apiAxios.delete('http://localhost:5000/estoque'+ this.objectId);
        } catch (error) { console.log('Falha na requisição') }

        this.$emit('onClose');
      }
    }
}
</script>
