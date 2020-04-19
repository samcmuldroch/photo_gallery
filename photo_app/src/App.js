import React, { useState, useEffect } from 'react';
import Masonry from "react-masonry-component";
import { masonryOptions } from "./exports";
import './App.css';

function renderPhoto(photoUrl) {
  return (
      <div>
        <img src={require("." + photoUrl)} />
      </div>
    );
}

function App() {
  const [photoUrls, setPhotoUrls] = useState([]);
  const [greyscale, setGreyscale] = useState(0)
  const [width, setWidth] = useState(0);

  useEffect(() => {
    fetch('/photo/grey/' + greyscale).then(res => res.json()).then(data => {
      let photoLocations = [];
      for (var i = 0; i < data.photos.length; i++) {
        let currPhoto = data.photos[i]
        photoLocations.push(currPhoto.photo);
      }
      setPhotoUrls(photoLocations);
    });
  }, [greyscale, width]);

  return (
    <div className="App">
      <header className="App-header">
        <p>Photo Gallery</p>
      </header>
      <>
        <button onClick={() => {
            if (greyscale == 0) {
              setGreyscale(1);
            } else {
              setGreyscale(0);
            }
          }}>
          Toggle Greyscale
        </button>
      </>
      <Masonry
        className={"grid"}
        elementType={"div"}
        options={masonryOptions}
        disableImagesLoaded={false}
        updateOnEachImageLoad={false}
      >
        {photoUrls.map(photoUrl => renderPhoto(photoUrl))}
      </Masonry>
    </div>
  );
}

export default App;
