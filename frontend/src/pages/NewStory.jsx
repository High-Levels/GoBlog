import React from "react";

function NewStory() {
  return (
    <div className="container m-5">
      <div className="row">
        <div className="col-8">
          <button className="btn btn-success mb-3">Publish</button>
          <div className="d-flex">
            <button className="btn btn-outline-dark btn-rounded m-2">+</button>
            <h1
              contentEditable="true"
              style={{ outline: "0px solid transparent" }}
              className="text-secondary"
            >
              Title
            </h1>
          </div>
          <div className="d-flex">
            <button className="btn btn-outline-dark btn-rounded ms-2">+</button>
            <p
              contentEditable="true"
              style={{ outline: "0px solid transparent" }}
              id="text-paragraph"
              className="text-secondary"
            >
              Tell your story ...
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}

export default NewStory;
