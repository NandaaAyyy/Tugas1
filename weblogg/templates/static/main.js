const cards = document.getElementsByClassName("card")

for (let element of cards) {

    element.onclick = (event) => {
        event.currentTarget.classList.toggle("expanded")
    }
}