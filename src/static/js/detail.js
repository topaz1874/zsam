$(document).ready(function() {
    $('.testmarked').html(marked('# Marked in browser\n\nRendered by **marked**.'));
    $('.content').each(function(){
      var content = $(this).text();
      var markedContent = marked(content);
      // console.log(markedContent);
      $(this).html(markedContent);
    });
});