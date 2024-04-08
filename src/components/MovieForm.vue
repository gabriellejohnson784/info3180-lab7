<script setup>
import { ref, onMounted } from "vue";

const movieTitle = ref('');
const movieGenre = ref('');
const movieRating = ref('');
let csrf_token = ref('');

function getCsrfToken() {
  fetch('/api/v1/csrf-token')
    .then((response) => response.json())
    .then((data) => {
      csrf_token.value = data.csrf_token;
    });
}

onMounted(() => {
  getCsrfToken();
});

let movieForm = document.getElementById('movieForm');
let form_data = new FormData(movieForm);

const saveMovie = () => {
  fetch("/api/v1/movies", {
 method: 'POST',
 body: form_data,
 headers: {
 'X-CSRFToken': csrf_token.value
 } 
})
 .then(function (response) {
      if (response.ok) {
        console.log('File Upload Successful.');
        
        movieTitle.value = '';
      } else {
        
        console.log('Error.');
      }
    })
    .catch(function (error) {
      console.log(error);
    });
};
</script>

<template>
  <div class="container">
    <form id="movieForm" @submit.prevent="saveMovie" class="movie-form">
      <div class="form-group">
        <label for="title">Title</label>
        <input type="text" id="title" v-model="title" class="form-control">
      </div>
      <div class="form-group">
        <label for="description">Description</label>
        <textarea id="description" v-model="description" class="form-control" rows="5"></textarea>
      </div>
      <button type="submit" class="btn btn-primary">Submit</button>
    </form>
    <div v-if="successMessage" class="success-message">{{ successMessage }}</div>
    <div v-if="errorMessage" class="error-message">{{ errorMessage }}</div>
  </div>
</template>


<style>
.container {
  width: 80vw;
  margin: 0 auto;
}

.movie-form {
  border: 1px solid #ccc;
  padding: 20px;
  border-radius: 5px;
}

.form-group {
  margin-bottom: 15px;
}

label {
  display: block;
  margin-bottom: 5px;
}

input[type="text"],
textarea {
  width: 100%;
  padding: 8px;
  box-sizing: border-box;
  border: 1px solid #ccc;
  border-radius: 3px;
}

button {
  padding: 8px 20px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 3px;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}

.btn-primary {
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 3px;
  cursor: pointer;
}

.btn-primary:hover {
  background-color: #0056b3;
}
</style>


