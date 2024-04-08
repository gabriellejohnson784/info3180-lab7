<template>
  <div>
    <h1>Movies</h1>
    <div class="card-container">
      <div v-for="movie in movies" :key="movie.id" class="card">
        <img :src="movie.image" alt="Movie Poster" class="card-image" />
        <div class="card-body">
          <h2 class="card-title">{{ movie.title }}</h2>
          <p class="card-description">{{ movie.description }}</p>
        </div>
      </div>
    </div>
  </div>
</template>


<script setup>
import { ref, onMounted } from "vue";
let movies = ref([]);

const fetchMovies = async () => {
  try {
    const response = await fetch("/api/v1/movies");
    if (!response.ok) {
      throw new Error("Failed !");
    }
    movies.value = await response.json();
  } catch (error) {
    console.error(error);
  }
};

onMounted(fetchMovies);
</script>

