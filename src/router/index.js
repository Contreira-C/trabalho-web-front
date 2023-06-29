import{ createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
    history: createWebHistory(),
    routes: 
    [
        { 
            path: '/',
            name: 'Login', 
            component: () => import('../views/Login.vue')
        },
        {
            path: '/configuracoes',
            name: 'Configurações',
            component: () => import('../views/Settings.vue')
        },

        {
            path: '/fornecedores',
            name: 'Fornecedores',
            component: () => import('../views/Fornecedores/Fornecedores.vue')
        },
        {
            path: '/estoque',
            name: 'Estoque',
            component: () => import('../views/Estoque/Estoque.vue')
        },
        {
            path: '/colaboradores',
            name: 'Colaboradores',
            component: () => import('../views/Colaboradores/Colaboradores.vue')
        },
        
    ]
})

export default router