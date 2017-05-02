$(document).ready(function() {
    console.log("I am ok!");
    console.log("I am ok again.")
    var marked = require('marked');
    console.log(marked('I am using __markdown__.'));
});