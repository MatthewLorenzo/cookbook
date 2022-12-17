function deleteRecipe(recipeId) {
  fetch("/delete-recipe", {
    method: "POST",
    body: JSON.stringify({ recipeId: recipeId }),
  }).then((_res) => {
    window.location.href = "/";
  });
}
function showForm() {
  document.getElementById('add_ingredients').style.display = 'block'
  document.getElementById('add_ingredients').style.marginTop = '50px';
}