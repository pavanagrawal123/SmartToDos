<template>
  <v-layout column justify-center align-center>
    <v-container grid-list-md align-center text-xs-center>
      <h1> Your todo list will take {{ Math.round(this.time) }} minutes to complete </h1>
      <v-layout align-content-center row wrap>
        <v-flex xs3>
          <v-text-field v-model="todo" label="New Todo"></v-text-field>
        </v-flex>
        <v-flex xs2>
          <v-btn @click="addTodo">Add</v-btn>
        </v-flex>
        <v-flex xs2>
          <v-btn @click="Prioritize">Prioritize Tasks</v-btn>
        </v-flex>
        <v-flex xs3>
          <v-btn @click="Time">Predict Time Needed</v-btn>
        </v-flex>
        <v-flex xs2>
          <v-btn @click="Dummy">Load Dummy Data</v-btn>
        </v-flex>
      </v-layout>
    </v-container>
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
          <td>{{ props.item.time }}</td>
          <td>
            <v-btn  @click="removeTodo(props.item.id)">Completed</v-btn>
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
          <td>{{ props.item.time }}</td>
          <td>
            <v-btn  @click="removeTodo(props.item.id)">Completed</v-btn>
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
          <td>{{ props.item.time }}</td>
          <td>
            <v-btn @click="removeTodo(props.item.id)">Completed</v-btn>
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
          <td>{{ props.item.time }}</td>
          <td>
            <v-btn @click="removeTodo(props.item.id)">Completed</v-btn>
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
      todoList: [],
      count: -1,
      time: 0,
    }
  },
  methods: {
    addTodo: function() {
      this.todoList.push({
        id: ++this.count,
        text: this.todo,
        priority: null,
        time: null
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
        if (this.todoList[i].priority == null) {
          axios
            .get(
              'http://ec2-54-172-93-154.compute-1.amazonaws.com:5000/priority?task=' + this.todoList[i].text
            )
            .then(response => {
              this.todoList[i].priority = response.data
            })
        }
      }
    },
    Time: function() {
      for (let i = 0; i < this.todoList.length; i++) {
        if (this.todoList[i].time == null) {
          axios
            .get(
              'http://ec2-54-172-93-154.compute-1.amazonaws.com:5000/time?task=' + this.todoList[i].text
            )
            .then(response => {
              this.todoList[i].time = response.data;
              this.time+= response.data;
            })
        }
      }
    },
    Dummy: function() {
      this.todoList =[
        { id: 0, text: "Calculus Homework", priority: null, time: null},
        { id: 1, text: "Physics Homework", priority: null, time: null},
        { id: 2, text: "English Paper", priority: null, time: null},
        { id: 3, text: "Eat Lunch", priority: null, time: null},
        { id: 4, text: "Do Laundry", priority: null, time: null},
        { id: 5, text: "Call insurance company to renew", priority: null, time: null},
        { id: 6, text: "pay elctricity bill", priority: null, time: null},
        { id: 7, text: "drive to school and pickup kid from school", priority: null, time: null},
        { id: 8, text: "mow the lawn", priority: null, time: null},
        { id: 9, text: "reserve table at restaurant", priority: null, time: null},
        { id: 10, text: "purchase tickets", priority: null, time: null},
        { id: 11, text: "work on the book report.", priority: null, time: null},
        { id: 12, text: "Call the doctor's office to make an appointment", priority: null, time: null},
        { id: 13, text: "go to store and buy present for birthday party", priority: null, time: null},

      ]
      this.size = 14;
      this.time = 0;
    }
  }
}
</script>
