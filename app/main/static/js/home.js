adaptLastPosts();
window.onresize = adaptLastPosts;

function adaptLastPosts() {
    if (window.innerWidth < 1200) {
        ultimosPosts = document.getElementById("ultimosPosts")
        ultimosPosts.children[3].style.setProperty("display", "none", "important");
        if (window.innerWidth < 1000) {
            ultimosPosts.children[2].style.setProperty("display", "none", "important");
            if (window.innerWidth < 764) {
                ultimosPosts.children[1].style.setProperty("display", "none", "important");
            } else {
                ultimosPosts.children[1].style.setProperty("display", "flex");
            }
        } else {
            ultimosPosts.children[2].style.setProperty("display", "flex");
            ultimosPosts.children[1].style.setProperty("display", "flex");
        }
    } else {
        ultimosPosts.children[3].style.setProperty("display", "flex");
        ultimosPosts.children[2].style.setProperty("display", "flex");
        ultimosPosts.children[1].style.setProperty("display", "flex");
    }
}
