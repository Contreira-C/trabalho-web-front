<template>
   
     <div class="ms-4 mt-4 d-flex">
      <router-link to="/colaboradores" class="button" style="text-decoration: none; color: inherit;">
       <div class="card bg-light botao1 me-2" style="height: 150px; width: 150px;">
         <div style="height: 190px;" >
           <span class="material-icons" style="font-size: 80px; display: flex; justify-content: center; align-items: center; height: 100%;">
             group
           </span>
         </div>
         <h5 class="text-center align-bottom">Colaboradores</h5>
       </div>
      </router-link>
      <router-link to="/" class="button" style="text-decoration: none; color: inherit;">
       <div class="card bg-light" style="height: 150px; width: 150px;">
         <div style="height: 190px;">
           <span class="material-icons text-danger" style="font-size: 80px; display: flex; justify-content: center; align-items: center; height: 100%;">
             logout
           </span>
         </div>
         <h5 class="text-center align-bottom">Logout</h5>
       </div>
      </router-link>
     </div>
 </template>
 <style>
.botao1:hover {
  color: var(--primary);
}
</style>