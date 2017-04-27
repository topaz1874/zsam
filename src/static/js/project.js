// <script type="text/javascript">
$(document).ready(function(){
    $('.content').each(function(){
      var content = $(this).text();
      var markedContent = marked(content);
      $(this).html(markedContent);
    })
  })
// </script>