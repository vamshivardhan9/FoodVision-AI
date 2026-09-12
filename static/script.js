let selectedModel = null;


// ================= 34 CLASSES =================

const classes = [
    "Baked Potato",
    "Pakode",
    "Chapati",
    "Chicken Curry",
    "Kulfi",
    "Taco",
    "Burger",
    "Momos",
    "Donut",
    "Butter Naan",
    "Masala Dosa",
    "Fries",
    "Dal Makhani",
    "Jalebi",
    "Chole Bhature",
    "Pav Bhaji",
    "Pizza",
    "Samosa",
    "Idli",
    "Dhokla",
    "Poha",
    "Pani Puri",
    "Fried Rice",
    "Biryani",
    "Gulab Jamun",
    "Rasgulla",
    "Paratha",
    "Kheer",
    "Rajma",
    "Palak Paneer",
    "Paneer Tikka",
    "Aloo Gobi",
    "Fish Curry",
    "Vegetable Curry"
];


// Display classes

const classesList =
    document.getElementById("classesList");


classes.forEach(function(food) {

    const div =
        document.createElement("div");

    div.className = "class-item";

    div.textContent = food;

    classesList.appendChild(div);

});


// ================= IMAGE UPLOAD =================

const imageInput =
    document.getElementById("imageInput");


imageInput.addEventListener("change", function() {

    const file = this.files[0];

    if (!file) {
        return;
    }

    const imageURL =
        URL.createObjectURL(file);


    document.getElementById(
        "uploadedImage"
    ).src = imageURL;


    document.getElementById(
        "mainImage"
    ).src = imageURL;


    document.getElementById(
        "predictionImage"
    ).src = imageURL;

});


// ================= MODEL SELECTION =================

const modelButtons =
    document.querySelectorAll(".model-btn");


modelButtons.forEach(function(button) {

    button.addEventListener("click", function() {

        modelButtons.forEach(function(btn) {

            btn.classList.remove("active");

        });


        this.classList.add("active");

        selectedModel =
            this.dataset.model;


        document.getElementById(
            "selectedModel"
        ).textContent = selectedModel;

    });

});


// ================= PREDICTION =================

document.getElementById(
    "predictBtn"
).addEventListener("click", async function() {

    if (!imageInput.files[0]) {

        alert("Please upload an image.");

        return;

    }


    if (!selectedModel) {

        alert("Please select CNN, VGG16 or ResNet50.");

        return;

    }


    const formData =
        new FormData();


    formData.append(
        "image",
        imageInput.files[0]
    );


    formData.append(
        "model",
        selectedModel
    );


    try {

        const response =
            await fetch("/predict", {

                method: "POST",

                body: formData

            });


        const data =
            await response.json();


        if (!data.success) {

            alert(data.message);

            return;

        }


        // Prediction

        document.getElementById(
            "predictionResult"
        ).textContent =
            data.prediction;


        // Hide classes

        document.getElementById(
            "classesSection"
        ).classList.add("hidden");


        // Show reports

        document.getElementById(
            "reportsSection"
        ).classList.remove("hidden");


        // Update image

        document.getElementById(
            "predictionImage"
        ).src = data.image;


    }

    catch (error) {

        console.error(error);

        alert("Prediction failed.");

    }

});