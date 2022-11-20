import React, { useState } from "react";
import "./App.css";
import InfiniteCarousel from "react-leaf-carousel";

function App() {
  const [file, setFile] = useState();

  function handleChange(e) {
    console.log(e.target.files);
    setFile(URL.createObjectURL(e.target.files[0]));
  }

  async function uploadFile(e) {
    const file = e.target.files[0];
    if (file != null) {
      const data = new FormData();
      data.append("file_from_react", file);

      let response = await fetch("/url_route", {
        method: "post",
        body: data,
      });
      let res = await response.json();
    }
  }

  async function cropimage() {
    await fetch("/classify", {
      method: "get",
    });
  }

  async function deleteImage(e){
    await fetch("/delete?PATH="+e.target.name.replaceAll("/","."), {
        method: "get",
      });
  }

  function importAll(r) {
    return r.keys().map(r);
  }

  const images = importAll(
    require.context("../../crop_image", false, /\.(png|jpe?g|svg)$/)
  );

  return (
    <div className="App">
      <h2 className="instruction-title">Welcome to FaceLift</h2>
      <h3 className="instruction-subtitle">
        A targeted face blur technology meant to protect your privacy in an ever
        evolving technological world
      </h3>
      <h4 className="instruction-description">
        Upload images of those you don't want blurred
      </h4>
      <input className="input-button" type="file" onChange={uploadFile} />
      <button onClick={cropimage} className="upload-button">
        {" "}
        Add Faces!
      </button>
      {/* <div style="text-align: center;"> */}
      <InfiniteCarousel
        breakpoints={[
          {
            breakpoint: 500,
            settings: {
              slidesToShow: 2,
              slidesToScroll: 2,
            },
          },
          {
            breakpoint: 768,
            settings: {
              slidesToShow: 3,
              slidesToScroll: 3,
            },
          },
        ]}
        dots={true}
        showSides={true}
        sidesOpacity={0.5}
        sideSize={0.1}
        slidesToScroll={4}
        slidesToShow={4}
        scrollOnDevice={true}
        autoCycle={true}
      >
        {images.map((img, index) => (
          <div className="cropImage">
            <img key={index} src={img} alt={img} />
            <input onClick={deleteImage} class="delete" type="button" name={img} value="Delete" />
          </div>
        ))}
      </InfiniteCarousel>
      {/* </div> */}
    </div>
  );
}

export default App;
