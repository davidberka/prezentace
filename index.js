const container = document.querySelector("#container");

for (let i = 1; i <= 20; i++) {
  for (let j = 1; j <= 6; j++) {
    const img = new Image();
    const url = `./screenshots/${i}/slide_${j}.png`;
    img.src = url;
    img.loading = "lazy";
    img.onerror = () => {
      img.style.opacity = 0;
    };

    container.appendChild(img);
  }
}
