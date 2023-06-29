<template>
  <div>
    <div v-if="statusmodalopen" class="modal">
      <div class="modal-content">
        <span class="close" @click="closeModal">&times;</span>
        <div class="header">
          <h4 class="mt-3 ms-3">{{ title }}</h4>
        </div>
        <div class="container">
          <div class="p-2 row"> 
            <slot></slot>
          </div>
        </div>
        <div class="footer text-end">
          <button class="btn" @click="$emit('salvar')">
              <span class="material-icons" style="color:white">
                  save
              </span>
          </button>
          <button v-if="isedit" class="btn" @click="$emit('deletar')">
              <span class="material-icons text-danger">
                  delete
              </span>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>
  
  <script>
  export default {
    data() {
      return {
        isModalOpen: false,
      };
    },
    methods: {
      openModal() {
        this.isModalOpen = true;
      },
      closeModal() {
        this.$emit("closemodal");
      },
    },
    props: {
      statusmodalopen: { type: Boolean, default: false },
      title: { type: String, default: "Titulo" },
      isedit: { type: Boolean, default: false}
    },
  };
  </script>
  
  <style scoped>
.header {
  background-color: var(--dark-alt);
  color: white;
  height: 50px;
  border-radius: 10px 10px 0px 0px;
}

.footer {
  background-color: var(--dark-alt);
  color: white;
  padding-top: 5px;
  border-radius: 0px 0px 10px 10px;
}

.modal {
  display: block;
  position: fixed;
  z-index: 9999;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
}

.modal-content {
  position: relative;
  background-color: #fefefe;
  margin: 15% auto;
  border: 1px solid #888;
  width: 80%;
  max-width: 800px;
  border-radius: 10px; /* Rounded edges */
}

.close {
  color: white;
  position: absolute;
  top: 5px;
  right: 20px;
  font-size: 28px;
  font-weight: bold;
  cursor: pointer;
}
</style>