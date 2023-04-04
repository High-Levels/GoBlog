import React from "react";
import Avatar from "./Avatar";
import Image1 from "../assets/images/avatar.png";

function Card() {
  const truncanteText = (title, text, limitTitle, limitText) => {
    let titleWords = title.split(" ");
    let textWords = text.split(" ");

    if (titleWords.length > limitTitle) {
      title = titleWords.slice(0, limitTitle).join(" ") + "...";
    }

    if (textWords.length > limitText) {
      text = textWords.slice(0, limitText).join(" ") + "...";
    }
    return { title, text };
  };

  const oriTitle =
    "Judul Artikel Ini Masih Belum Ditentukan Nanti Akan Diganti Bila Sudah Jadi";
  const oriText =
    "Lorem ipsum dolor sit amet consectetur adipisicing elit. Aliquid dolore esse magni a odio, reprehenderit voluptas eaque assumenda soluta hic odit obcaecati nemo minima quo. Commodi incidunt pariatur vitae. Numquam.";

  const limitTitle = 10;
  const limitText = 24;

  const { title, text } = truncanteText(
    oriTitle,
    oriText,
    limitTitle,
    limitText
  );

  return (
    <div className="container mb-3">
      <div className="card p-3 shadow" style={{ maxWidth: "700px" }}>
        <div className="row">
          <div className="col d-flex align-items-center mb-2">
            <Avatar src={Image1} height={30} />
            <div className="ms-2">
              <small className="fw-bold">Nama User</small>
            </div>
          </div>
        </div>
        <div className="row">
          <div className="col-md-8">
            <h4 className="fw-bold text-start">{title}</h4>
            <p className="text-start">{text}</p>
          </div>
          <div className="col-md-4">
            <img
              src="/src/assets/images/example.jpg"
              alt=""
              className="img-fluid"
            />
          </div>
        </div>
        <div className="row d-flex align-items-center">
          <small className="text-secondary">27 Maret 2023</small>
        </div>
      </div>
    </div>
  );
}

export default Card;
