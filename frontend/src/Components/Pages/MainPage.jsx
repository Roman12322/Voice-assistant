import { useState } from "react";
import "./MainPage.css";
import { api } from "../../api";

export const MainPage = () => {
  const [drag, setDrag] = useState(false);

  function drugStartHundler(e) {
    e.preventDefault();
    setDrag(true);
  }
  function drugLeavetHundler(e) {
    e.preventDefault();
    setDrag(false);
  }
  function onDropHandler(e) {
    e.preventDefault();
    let files = [...e.dataTransfer.files];
    const formData = new FormData();
    formData.append("file", files[0]);
    formData.append("userId", 1);
    console.log(files);
    api.post('/upload', formData)
    setDrag(false);
  }

  return (
    <div className="mainBlock">
      {drag ? (
        <div
          className="drop-area"
          onDragStart={(e) => drugStartHundler(e)}
          onDragLeave={(e) => drugLeavetHundler(e)}
          onDragOver={(e) => drugStartHundler(e)}
          onDrop={(e) => onDropHandler(e)}
        >
          Перетащите файлы сюда
        </div>
      ) : (
        <div
          onDragStart={(e) => drugStartHundler(e)}
          onDragLeave={(e) => drugLeavetHundler(e)}
          onDragOver={(e) => drugStartHundler(e)}
        >
          Выберите файл(-ы)
        </div>
      )}
    </div>
  );
};
