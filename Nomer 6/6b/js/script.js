$('#deleteRow').click(function () {
    var tableID = "rowTable";
    var table = document.getElementById(tableID);
    var rowCount = table.rows.length;
    console.log(rowCount);
    if (rowCount != 1) {
        rowCount = rowCount - 1;
        table.deleteRow(rowCount);
    }
});