$(() => {
  $.get('https://swapi-api.hbtn.io/api/films/?format=json', (data, status) => {
    if (status === 'success') {
      const movies = data.results;
      movies.forEach(movie => {
        $('#list_movies').append('<li>' + movie.title + '</li>');
      });
    }
  });
});
