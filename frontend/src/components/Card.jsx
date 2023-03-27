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

  const oriTitle = "Judul Artikel Ini Masih Belum Ditentukan";
  const oriText =
    "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Laborum architecto autem nisi dolorem officiis est et harumeos corporis quia. Tenetur, aperiam. Dignissimos dolore undesunt ipsam. Aut, ea iure.";

  const limitTitle = 5;
  const limitText = 8;

  const { title, text } = truncanteText(
    oriTitle,
    oriText,
    limitTitle,
    limitText
  );

  return (
    <div className="container">
      <div className="row">
        <div className="col-md-7">
          <div className="card mx-auto">
            <div className="row">
              <div className="col">
                <div className="card-body">
                  <div className="d-flex align-items-center mb-2">
                    <Avatar src={Image1} height={30} />
                    <div className="ms-2">
                      <small className="fw-bold ">Nama User</small>
                    </div>
                  </div>
                  <h4 className="card-title fw-bold text-start">{title}</h4>
                  <p className="text-body-secondary text-start">{text}</p>
                  <p className="card-text text-start">
                    <small className="text-body-secondary">27 Maret 2023</small>
                  </p>
                </div>
              </div>
              <div className="col">
                <img
                  src="/src/assets/images/example.jpg"
                  alt=""
                  className="img-fluid"
                />
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Card;
