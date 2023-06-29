<template>
    <Modal
    :isModalOpen="isModalOpen"
    @onClose="closeModal();"
    :isEdit="editardata"
    :objectId="editarId"
    />
    <List 
        @add-button-callback="openModal(false)"
        :columns = "
        [
            { label: 'Usuario'},
            { label: 'Email'},
            { label: '', class: 'col-1 ms-auto' }
        ]">

        <div  v-for="item in Lista" class="row border p-2 bg-light text-center align-items-center" style="height: 55px">
            <div class="col mt-2">
                {{ item.username }}
            </div>
            <div class="col mt-2">
                {{ item.email }}
            </div>
            <div class="col-1 ms-auto">
                <button class="btn botao1 d-flex botao1" @click="openModal(true,item.id)">
                    <span class="material-icons" style="color:white">
                        edit
                    </span>
                </button>
            </div>
        </div>
    </List>
</template>
<script>
import List from '../../components/List.vue'
import Modal from  './modalColaboradores.vue'

export default{
    components:{
        List,
        Modal
    },
        mounted() {
            this.requisicao()
        },
        data(){
            return{
                Lista:[],
                isModalOpen: false,
                editardata:false,
                editarId:null
            }
        },
        methods:{
            requisicao: async function(){
                const response = await this.$apiAxios.get('http://localhost:5000/usuarios', {
                    headers: {
                        'Access-Control-Allow-Origin': '*', // Permitir todas as origens.
                        'Access-Control-Allow-Methods': 'GET', // Permitir apenas o metodo GET.
                    }
                });
                // this.Lista = response.data
                console.log(response)
                this.Lista = response.data
            },
            closeModal() {
                this.isModalOpen = false;
                this.editarId = 0;
                this.requisicao()
            },
            openModal(isEdit, objectId = null) {
                this.editardata = isEdit;
                this.editarId = objectId;
                this.isModalOpen = true;
            },
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