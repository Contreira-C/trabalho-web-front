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
                <label class="form-label">Usuario</label>
                <input type="text" class="form-control"  placeholder="Digite o usuario" v-model="dataForm.username">
            </div>
            <div class="mb-3 col-6">
                <label class="form-label">Email</label>
                <input type="email" class="form-control"  placeholder="Digite o email" v-model="dataForm.email">
            </div>
            <div class="mb-3 col-6">
                <label class="form-label">Senha</label>
                <input type="password" class="form-control"  placeholder="Digite a senha" v-model="dataForm.password">
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
                username: '',
                email: '',
                password: '',
            },
            isModalOpen: true,
            titulo:'Adicionar Colaborador'
        }
    },  
    watch: {
        isEdit(newVal) {
            console.log(this.objectId)
            if (newVal && this.objectId) {
                this.titulo = 'Editar Usuario'
                const response = this.$apiAxios.get('http://localhost:5000/usuarios/'+this.objectId)
                const content = response.data

                this.dataForm.username = content.username
                this.dataForm.email = content.email
                this.dataForm.password = content.senha
            }else{
                this.freshstart()
                this.titulo = 'Cadastro de Usuario'
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
        salvar: async function()
      {
        const params = {
            'username': this.dataForm.username,
            'email': this.dataForm.email,
            'senha': this.dataForm.password,
        }
        
        try {
          if(this.idEditar){
            await this.$apiAxios.put('http://localhost:5000/usuarios'+ this.objectId, params);
          }else{
            await this.$apiAxios.post('http://localhost:5000/usuarios', params);
        }
        } catch (error) { console.log('Falha na requisição') }

        this.$emit('onClose');
      },
      deletar: async function(){
        try {
            await this.$apiAxios.delete('http://localhost:5000/usuarios'+ this.objectId);
        } catch (error) { console.log('Falha na requisição') }

        this.$emit('onClose');
      }
    }
}
</script>