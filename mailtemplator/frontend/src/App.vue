<template>
  <v-app>
    <v-app-bar color="grey lighten-5" elevation="1">
      <v-toolbar-title>Mailtemplater</v-toolbar-title>
    </v-app-bar>
    <v-navigation-drawer
      permanent
      color="grey lighten-5"
      elevation="3"
    >
      <v-list>
        <v-list-item
          v-for="(item, i) in this.navitems"
          :key="i"
          :to="item.path"
        >
          <v-list-item-content>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-footer color="grey lighten-5" class="text-right">
      © MUES File - Taketora Uzuahra, Hiroki Hisashige
    </v-footer>

    <router-view />
  </v-app>
</template>

<script>

export default {
  name: 'App',

  components: {
  },

  data: () => ({
    navitems : [
      {
        title: "始めの方へ",
        path: "/beginner"
      },
      {
        title: "お問い合わせ",
        path: "/contact"
      }
    ]
  }),
};
</script>
