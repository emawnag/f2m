document.addEventListener('DOMContentLoaded', function() {
    fetch('./append.html')
        .then(response => response.text())
        .then(data => {
            document.getElementById('main').innerHTML = data;
            mainReload();
        })
        .catch(error => console.error('Error fetching the HTML:', error));
});
/**注意utf8/16 */
function mainReload() {
    $("#s").css("background-color", "yellow");
    const mainTable = document.getElementById('mainT');
    const rows = mainTable.querySelectorAll('tbody tr');
    const randomRow = rows[Math.floor(Math.random() * rows.length)];
    const cells = randomRow.querySelectorAll('td');
    
    cells.forEach((cell, index) => {
        const targetId = String.fromCharCode(97 + index); // 'a' is 97 in ASCII
        const targetElement = document.getElementById(targetId);
        if (targetElement) {
            targetElement.innerText = cell.innerText;
        }

    });
    const randomBool = Math.random() >= 0.5;
    //console.log(`Random boolean for cell ${index}:`, randomBool);
    $(".css-mobile .left-time").html(randomBool?
        ($("#c").text())+'ft'
        :
        ($("#d").text())+'m'
    )
}
document.getElementById('reloadRandom').addEventListener('click', mainReload);