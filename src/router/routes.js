import store from '@/state/store'

export default [
    {
        path: '/register',
        name: 'register',
        component: () => import('@/views/pages/account/register'),
        meta: {
            beforeResolve(routeTo, routeFrom, next) {
                // If the user is already logged in
                if (store.getters['auth/loggedIn']) {
                    // Redirect to the home page instead
                    next({ name: 'home' })
                } else {
                    // Continue to the login page
                    next()
                }
            },
        },
    },
    {
        path: '/registeruser',
        name: 'registeruser',
        component: () => import('@/views/pages/account/registeruser'),
        meta: {
            beforeResolve(routeTo, routeFrom, next) {
                // If the user is already logged in
                if (store.getters['auth/loggedIn']) {
                    // Redirect to the home page instead
                    next({ name: 'home' })
                } else {
                    // Continue to the login page
                    next()
                }
            },
        },
    },
    {
        path: '/forgot-password',
        name: 'Forgot-password',
        component: () => import('../views/pages/account/forgot-password'),
        meta: {
            beforeResolve(routeTo, routeFrom, next) {
                // If the user is already logged in
                if (store.getters['auth/loggedIn']) {
                    // Redirect to the home page instead
                    next({ name: 'home' })
                } else {
                    // Continue to the login page
                    next()
                }
            },
        },
    },
    {
        path: '/logout',
        name: 'logout',
        meta: {
            authRequired: true,
            beforeResolve(routeTo, routeFrom, next) {
                if (process.env.VUE_APP_DEFAULT_AUTH === "firebase") {
                    store.dispatch('auth/logOut')
                } else {
                    store.dispatch('authfack/logout')
                }
                const authRequiredOnPreviousRoute = routeFrom.matched.some(
                    (route) => route.push('/login')
                )
                // Navigate back to previous page, or home as a fallback
                next(authRequiredOnPreviousRoute ? { name: 'home' } : { ...routeFrom })
            },
        },
    },
    {
        path: '/ecommerce/orders',
        name: 'Orders',
        meta: { authRequired: true },
        component: () => import('../views/pages/ecommerce/orders')
    },
    {
        path: '/email',
        name: 'email',
        meta: { authRequired: true },
        component: () => import('../views/pages/email/inbox'),
    },
    {
        path: '/email/read',
        name: 'Read Email',
        meta: { authRequired: true },
        component: () => import('../views/pages/email/reademail')
    },
    {
        path: '/pages/timeline',
        name: 'Timeline',
        meta: { authRequired: true },
        component: () => import('../views/pages/utility/timeline/index')
    },
    {
        path: '/pages/faqs',
        name: 'Faqs',
        meta: { authRequired: true },
        component: () => import('../views/pages/utility/faqs')
    },
    {
        path: '/icons/font-awesome',
        name: 'Font Awesome 5',
        meta: { authRequired: true },
        component: () => import('../views/pages/icons/font-awesome/index')
    },
    {
        path: '/icons/dripicons',
        name: 'Dripicons',
        meta: { authRequired: true },
        component: () => import('../views/pages/icons/dripicons')
    },
    {
        path: '/icons/material-design',
        name: 'Material Design',
        meta: { authRequired: true },
        component: () => import('../views/pages/icons/materialdesign/index')
    },
    {
        path: '/icons/remix',
        name: 'Remix Icons',
        meta: { authRequired: true },
        component: () => import('../views/pages/icons/remix/index')
    },
    {
        path: '/es',
        name: 'es',
        meta: { authRequired: true },
        component: () => import('../views/EnterpriseIndex.vue')
    },
    {
        path: '/',
        name: 'HelloWorld',
        redirect: '/index',
      },
      {
        path: '/index',
        name: 'index',
        component: () => import('../views/index.vue'),
      },
      {
        path: '/SX',
        name: 'SX',
        component: () => import('@/views/ESGSX.vue'),
      },
      {
        path: '/tuijian',
        name: 'tuijian',
        component: () => import('@/views/tuijian.vue')
      },
      //带参路由
      {
        path: '/enterprise/:targetname',
        name: 'enterpriseindex',
        component: () => import('@/views/EnterpriseIndex.vue'),
      },
      {
        path: '/news/:title',
        name: 'newsdetail',
        component: () => import('@/views/New.vue'),
      },
      {
        path: '/mainnews/:title',
        name: 'mainnews',
        component: () => import('@/views/MainNew.vue'),
      },
      {
        path: '/404',
        name: '404',
        component: () => import('@/views/404.vue'),
      },
      {
        path: '/500',
        name: '500',
        component: () => import('@/views/500.vue'),
      },
      {
        path: '/news',
        name: 'news',
        component: () => import('@/views/ESGnews.vue'),
      },
]
