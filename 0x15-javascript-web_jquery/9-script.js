$(() => {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', (data, status) => {
    if (status === 'success') {
      $('div#hello').text(data.hello);
    }
  });
});
