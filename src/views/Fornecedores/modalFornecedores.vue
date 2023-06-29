<template>
    <modal
    :statusmodalopen="isModalOpen"
    @closemodal="$emit('onClose');"
    @salvar="salvar()"
    @deletar="deletar()"
    :isedit="isEdit"
    :title="titulo"
    >
        <div class="mb-3 col-6">
                <label class="form-label">Nome</label>
                <input class="form-control" placeholder="Digite o nome" v-model="dataForm.nome">
            </div>
            <div class="mb-3 col-6">
                <label class="form-label">Email</label>
                <input class="form-control" placeholder="Digite o email" v-model="dataForm.email">
            </div>
            <div class="mb-3 col-6">
                <label class="form-label">Cnpj</label>
                <input class="form-control" placeholder="Digite o cnpj" v-model="dataForm.cnpj">
            </div>
            <div class="mb-3 col-6">
                <label class="form-label">Telefone</label>
                <input class="form-control" placeholder="Escolha o telefone" v-model="dataForm.telefone">
            </div>
            <div class="mb-3 col-6">
                <label class="form-label">Categoria</label>
                <input class="form-control" placeholder="Digite a categoria" v-model="dataForm.categoria">
            </div>
    </modal>
</template>
<script>
import modal from  '../../components/Modal.vue'
export default {
    components: {
        modal
    },
    data(){
        return{
            dataForm:{
                nome: '',
                email: '',
                cnpj: '',
                telefone: '',
                categoria: '',
            },
            isModalOpen: true,
            titulo:'Cadastro de fornecedor'
        }
    },
    watch: {
        isEdit(newVal) {
            if (newVal && this.objectId) {
                this.titulo = 'Editar Fornecedor'
                const response = this.$apiAxios.get('http://localhost:5000/fornecedores/'+this.objectId)
                const content = response.data

                this.dataForm.nome = content.nome
                this.dataForm.email = content.email
                this.dataForm.cnpj = content.cnpj
                this.dataForm.telefone = content.telefone
                this.dataForm.categoria = content.categoria
            }else{
                this.freshstart()
                this.titulo = 'Cadastro de Fornecedor'
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
            this.dataForm.nome = ''
            this.dataForm.email = ''
            this.dataForm.cnpj = ''
            this.dataForm.telefone = ''
            this.dataForm.categoria = ''
        },
        salvar: async function()
      {
        const params = {
            'nome': this.dataForm.nome,
            'email': this.dataForm.email,
            'cnpj': this.dataForm.cnpj,
            'telefone': this.dataForm.telefone,
            'categoria': this.dataForm.categoria,
        }
        
        try {
          if(this.objectId){
            await this.$apiAxios.put('http://localhost:5000/fornecedores'+ this.objectId, params);
          }else{
            await this.$apiAxios.post('http://localhost:5000/fornecedores', params);
        }
        } catch (error) { console.log('Falha na requisição') }

        this.$emit('onClose');
      },
      deletar: async function(){
        try {
            await this.$apiAxios.delete('http://localhost:5000/fornecedores'+ this.objectId);
        } catch (error) { console.log('Falha na requisição') }

        this.$emit('onClose');
      }
    }
}
</script>