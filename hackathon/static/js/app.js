$(document).on('change', ':file', function() {
  var input = $(this),
    numFiles = input.get(0).files ? input.get(0).files.length : 1,
    label = input.val().replace(/\\/g, '/').replace(/.*\//, '');
  input.trigger('fileselect', [numFiles, label]);

  document.getElementById('add-t-image').innerText = 'Change image';
  var img = document.getElementsByClassName('imagepreview');
  img[0].style.display = 'block';
});

function readURL(input) {
  if (input.files && input.files[0]) {
    var reader = new FileReader();
    reader.onload = function(e) {
      $('#preview').attr('src', e.target.result);
    }
    reader.readAsDataURL(input.files[0]);
  }
}

$('input[type="file"]').change(function() {
  readURL(this);
});

$(document).ready(function(){
  $("#hide").click(function(){
    $("#textshit").html("Add Classroom");
    $("#addclassroom").show();
    $("#hide").hide();
  });
});