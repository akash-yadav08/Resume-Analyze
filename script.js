async function upload() {
    const file = document.getElementById("fileInput").files[0];

    if (!file) {
        alert("Please upload a resume!");
        return;
    }

    let formData = new FormData();
    formData.append("file", file);

    try {
        let res = await fetch("https://resume-analyze-6qax.onrender.com/analyze", {
            method: "POST",
            body: formData
        });

        let data = await res.json();

        document.getElementById("result").classList.remove("hidden");

        document.getElementById("scoreBar").style.width = data.score + "%";
        document.getElementById("scoreText").innerText = data.score + "%";

        let skillsDiv = document.getElementById("skills");
        skillsDiv.innerHTML = "";

        data.skills_found.forEach(skill => {
            let span = document.createElement("span");
            span.innerText = skill;
            skillsDiv.appendChild(span);
        });

        document.getElementById("suggestions").innerText = data.suggestions;

    } catch (error) {
        alert("Error connecting to server!");
        console.error(error);
    }
}