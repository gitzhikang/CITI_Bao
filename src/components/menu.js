export const menuItems = [
    {
        id: 1,
        label: "menuitems.menu.text",
        isTitle: true
    },
    {
        id: 5,
        label: 'Follower',
        icon: 'ri-store-2-line',
        subItems: [
            {
                id: 8,
                label: 'menuitems.ecommerce.list.orders',
                link: '/ecommerce/orders'
            },
        ]
    },
    {
        id: 14,
        label: 'menuitems.email.text',
        icon: 'ri-mail-send-line',
        subItems: [
            {
                id: 15,
                label: 'menuitems.email.list.inbox',
                link: '/email'
            },
            {
                id: 16,
                label: 'menuitems.email.list.reademail',
                link: '/email/read'
            }
        ]
    },
    {
        id: 18,
        isLayout: true
    },
    {
        id: 19,
        label: 'menuitems.pages.text',
        isTitle: true
    },
    {
        id: 20,
        label: 'menuitems.authentication.text',
        icon: 'ri-account-circle-line',
        subItems: [
            {
                id: 21,
                label: 'menuitems.authentication.list.login',
                link: '/auth/login-1'
            },
            {
                id: 22,
                label: 'menuitems.authentication.list.register',
                link: '/auth/register-1'
            },
            {
                id: 23,
                label: 'menuitems.authentication.list.recoverpwd',
                link: '/auth/recoverpwd-1'
            },
            {
                id: 24,
                label: 'menuitems.authentication.list.lockscreen',
                link: '/auth/lock-screen-1'
            }
        ]
    },
    {
        id: 25,
        label: 'menuitems.utility.text',
        icon: 'ri-profile-line',
        subItems: [
            {
                id: 29,
                label: 'menuitems.utility.list.timeline',
                link: '/pages/timeline'
            },
            {
                id: 30,
                label: 'menuitems.utility.list.faqs',
                link: '/pages/faqs'
            },
        ]
    },
    {
        id: 74,
        label: "menuitems.icons.text",
        icon: 'ri-brush-line',
        subItems: [
            {
                id: 75,
                label: 'menuitems.icons.list.remix',
                link: '/icons/remix'
            },
            {
                id: 76,
                label: "menuitems.icons.list.materialdesign",
                link: '/icons/material-design'
            },
            {
                id: 77,
                label: "menuitems.icons.list.dripicons",
                link: '/icons/dripicons'
            },
            {
                id: 78,
                label: "menuitems.icons.list.fontawesome",
                link: '/icons/font-awesome'
            }
        ]
    },
]