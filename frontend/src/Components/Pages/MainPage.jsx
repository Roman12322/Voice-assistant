import React, { useState } from "react";
import "./MainPage.css";
import { api, fileSharing } from "../../api";
import Alert from "@mui/material/Alert";
import AlertTitle from "@mui/material/AlertTitle";

export const MainPage = () => {
  const [drag, setDrag] = useState(false);
  const [text, setText] = useState("");
  const [alertTitle, setAlertTitle] = useState("");
  const [alertTitleInfo, setAlertTitleInfo] = useState("");
  const [alertTitleError, setAlertTitleError] = useState("");
  const [alertContent, setAlertContent] = useState("");
  const [alertContentInfo, setAlertContentInfo] = useState("");
  const [alertContentError, setAlertContentError] = useState("");
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
    if (files[0].type === "audio/wav") {
      const formData = new FormData();
      formData.append("file", files[0]);
      formData.append("userId", 1);
      api.post("/upload", formData);
      setAlertTitle("success");
      setAlertContent("Ваш файл успешно отправлен!");
      setAlertTitleInfo("Info");
      setAlertContentInfo(
        "Идет обработка запроса. Данный процесс может занять некоторое время. Не закрывайте и не перезагружайте страницу"
      );
      setAlertTitleError("");
      setAlertContentError("");
      // setText(fileSharing()); <- return after ML available 
    } else {
      setAlertTitleError("Error");
      setAlertContentError(
        "Выбранный вами файл не имеет аудио формат (.wav). Попробуйте выбрать другой файл"
      );
      setAlertTitle("");
      setAlertContent("");
      setAlertTitleInfo("");
      setAlertContentInfo("");
    }
    setDrag(false);
  }

  return (
    <>
      <h2 className="header__name">
        GeekSupport
      </h2>
      <div className="main">
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
              className="drop-area__inactive"
              onDragStart={(e) => drugStartHundler(e)}
              onDragLeave={(e) => drugLeavetHundler(e)}
              onDragOver={(e) => drugStartHundler(e)}
            >
              Выберите файл(-ы)
            </div>
          )}
        </div>
        <div className="StatusBlock">
          <div className="contentFooter">
            <Alert severity="success" variant="outlined" className="Alert">
              <AlertTitle>{alertTitle}</AlertTitle>
              {alertContent}
            </Alert>
            <Alert severity="info" variant="outlined" className="Alert">
              <AlertTitle>{alertTitleInfo}</AlertTitle>
              {alertContentInfo}
            </Alert>
            <Alert severity="error" variant="outlined" className="Alert">
              <AlertTitle>{alertTitleError}</AlertTitle>
              {alertContentError}
            </Alert>
          </div>
        </div>
      </div>
      <div className="contentBlock">
        <h2 className="contentTitle">Конспект</h2>
        {text}
      </div>
    </>
  );
};
