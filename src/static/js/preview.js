    
$(document).ready(function() {


    // $('.testmarked').html(marked('# Marked in browser\n\nRendered by **marked**.'));

    // $('.content').each(function(){
    //   var content = $(this).text();
    //   var markedContent = marked(content);
    //   // console.log(markedContent);
    //   $(this).html(markedContent);
    // });

    

  var inputTiltle =  $('#id_title')

  function setTitle(value){
    $('#preview-title').text(value)
  }

  setTitle(inputTiltle.val())
  inputTiltle.keyup(function(){
    setTitle($(this).val())
  })


  var inputText = $('#id_text')

  function setText(value){
    markedContent = marked(value)
    $('#preview-content').html(markedContent)
    $('#preview-content img').each(function(){
      $(this).addClass('img-responsive');
    })
  }
  setText(inputText.val());

  inputText.keyup(function(){
    setText($(this).val())
  })

})
