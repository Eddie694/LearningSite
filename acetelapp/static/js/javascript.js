
function hiddenNav(){
    const hiddenNav = document.getElementById("hidden-nav");
    const header =document.getElementById("header");
    hiddenNav.style.display = "flex";
    header.style.display = "none";
    document.getElementById("html").classList.add("html");

}
function closeNav(){
    const hiddenNav = document.getElementById("hidden-nav");
    const header =document.getElementById("header");
    header.style.display = "flex";
    hiddenNav.style.display = "none";
    document.getElementById("html").classList.remove("html");
}


let count = 0;
function displaySettings(){
        const home = document.getElementById("settings");
        const dis = document.getElementById("display");
        
        number = count++;

        if (number%2 == 0){
            console.log(1);
            home.style.display ="block";
        }
        else{
            home.style.display = "none";
            console.log(2);
        }
}

// Get the header element
const header = document.getElementById('header');

// Initialize variables to keep track of scroll position
let prevScrollPos = window.pageYOffset;
let currentScrollPos;

// Function to handle the scroll event
function handleScroll() {
    currentScrollPos = window.pageYOffset;

    // Check if scrolling direction is up or down
    if (prevScrollPos > currentScrollPos) {
        // Scrolling up, show the sticky nav
        header.classList.add('show');
    } else {
        // Scrolling down, hide the sticky nav
        header.classList.remove('show');
    }

    prevScrollPos = currentScrollPos;
}

// Attach the handleScroll function to the scroll event
window.addEventListener('scroll', handleScroll);
