var allSearchElement = document.getElementsByClassName("individualSearch");

var keyUpFunction = function () {
  const CURRENTVALUE = this.value.toUpperCase();
  const CURRENTTABLE = document.querySelector(`.${this.dataset.target} tbody`);
  const ALLROWS = CURRENTTABLE.getElementsByTagName("tr");
  let isFound = false;

  for (const currentRow of ALLROWS) {
    let cells = currentRow.getElementsByTagName("td");
    for (const currentCell of cells) {
      if (currentCell.textContent.toUpperCase().indexOf(CURRENTVALUE) > -1) {
        isFound = true;
        break;
      }
    }

    currentRow.style.display = isFound ? "" : "none";
    isFound = false;
  }
};

for (var i = 0; i < allSearchElement.length; i++) {
  allSearchElement[i].addEventListener("keyup", keyUpFunction, false);
}

let allForm = document.getElementsByTagName("form");

var submitFunction = function (e) {
  document.getElementById("form-button").disabled = true;
  // this.submit();
};

for (var i = 1; i < allForm.length; i++) {
  allForm[i].addEventListener("submit", submitFunction);
}

let filterIndus = document.getElementById("filterByIndustry");
if (filterIndus != null)
  filterIndus.addEventListener("change", function (e) {
    // console.log(this.value, this.options[this.selectedIndex].text);
    document.getElementById("smallQueryFilter").submit();
  });
