
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