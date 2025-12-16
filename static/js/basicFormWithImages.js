iframe = document.getElementById("iframe");
iframe.onload = hideAndRemoveNavAndFooter;

function hideAndRemoveNavAndFooter() {
    let iframe = document.getElementById("iframe");
    let nav = iframe.contentWindow.document.getElementsByTagName("header")[0];
    nav.style.display = "none";
    let footer = iframe.contentWindow.document.getElementsByTagName("footer")[0];
    footer.style.display = "none";
    iframe.style.height = (80 + iframe.contentWindow.document.body.scrollHeight) + "px";

    if (iframe.contentWindow.document.getElementById("cancelAnchor")) {
        iframe.contentWindow.document.getElementById("cancelAnchor").href = iframe.getAttribute("data-url")
    }

    if (iframe.style.display == "") {
        iframe.style.display = "none";
    }
}

function toggleIframe() {
    if (iframe.style.display == "none") {
        iframe.style.display = "block";
    } else {
        iframe.style.display = "none";
    }
}
