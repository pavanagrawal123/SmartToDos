<template>
  <v-layout column justify-center align-center>
    <v-container grid-list-md align-center text-xs-center>
      <v-layout align-content-center row wrap>
        <v-flex xs3>
          <v-text-field v-model="todo" label="New Todo"></v-text-field>
        </v-flex>
        <v-flex xs3>
          <v-btn @click="addTodo">Add</v-btn>
        </v-flex>
        <v-flex xs3>
          <v-btn @click="Prioritize">Prioritize Tasks</v-btn>
        </v-flex>
        <v-flex xs3>
          <v-btn @click="addTodo">Add</v-btn>
        </v-flex>
      </v-layout>
    </v-container>
    <template>
      <v-form v-model="valid" v-on:submit.prevent="addTodo">
        <v-btn :disabled="!valid" @click="addTodo">Add</v-btn>
      </v-form>
    </template>
    <template>
      <h1>No Priority Tasks</h1>
      <v-data-table
        hide-actions
        hide-headers
        :headers="headers"
        :items="todoList.filter(item => item.priority == null)"
        class="elevation-1"
      >
        <template slot="items" slot-scope="props">
          <td>{{ props.item.text }}</td>
          <td>
            <v-btn :disabled="!valid" @click="removeTodo(props.item.id)">Completed</v-btn>
          </td>
        </template>
      </v-data-table>
      <h1>High Priority Tasks</h1>
      <v-data-table
        hide-actions
        hide-headers
        :headers="headers"
        :items="todoList.filter(item => item.priority >= 4)"
        class="elevation-1"
      >
        <template slot="items" slot-scope="props">
          <td>{{ props.item.text }}</td>
          <td>
            <v-btn :disabled="!valid" @click="removeTodo(props.item.id)">Completed</v-btn>
          </td>
        </template>
      </v-data-table>
      <h1>Medium Priority Tasks</h1>
      <v-data-table
        hide-actions
        hide-headers
        :headers="headers"
        :items="todoList.filter(item => item.priority == 3)"
        class="elevation-1"
      >
        <template slot="items" slot-scope="props">
          <td>{{ props.item.text }}</td>
          <td>
            <v-btn :disabled="!valid" @click="removeTodo(props.item.id)">Completed</v-btn>
          </td>
        </template>
      </v-data-table>
      <h1>Low Priority Tasks</h1>
      <v-data-table
        hide-actions
        hide-headers
        :headers="headers"
        :items="todoList.filter(item => item.priority < 3 && item.priority >= 1)"
        class="elevation-1"
      >
        <template slot="items" slot-scope="props">
          <td>{{ props.item.text }}</td>
          <td>
            <v-btn :disabled="!valid" @click="removeTodo(props.item.id)">Completed</v-btn>
          </td>
        </template>
      </v-data-table>
    </template>
  </v-layout>
</template>

<script>
import Logo from '~/components/Logo.vue'
import VuetifyLogo from '~/components/VuetifyLogo.vue'
import axios from 'axios'
export default {
  components: {
    Logo,
    VuetifyLogo
  },
  data() {
    return {
      todo: '',
      headers: [],
      todoList: [
        { id: 0, text: 'Item 1', priority: null },
        { id: 1, text: 'Item 2', priority: null },
        { id: 2, text: 'Item 3', priority: null }
      ],
      count: 2
    }
  },
  methods: {
    addTodo: function() {
      this.todoList.push({
        id: ++this.count,
        text: this.todo,
        priority: null
      })
    },
    removeTodo: function(id) {
      this.size--
      this.todoList.splice(id, 1)
      for (let i = 0; i < this.todoList.length; i++) {
        if (this.todoList[i].id >= id) {
          this.todoList[i].id--
        }
      }
    },
    Prioritize: function() {
      for (let i = 0; i < this.todoList.length; i++) {
        axios
          .get(
            'http://ec2-54-172-93-154.compute-1.amazonaws.com:5000/time?task=Calculus%20Homework'
          )
          .then(response => {
            alert(response)
          })
      }
    }
  }
}
</script>
