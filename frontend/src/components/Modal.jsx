import React from "react";
import Button from "./Button";

const Modal = () => {
  return (
    <div>
      {/* <Button
        label="test modal"
        variant="success"
        data-bs-toggle="modal"
        data-bs-target="#exampleModal"
      /> */}

      <div
        className="modal fade"
        id="exampleModal"
        aria-labelledby="exampleModalLabel"
        aria-hidden="true"
      >
        <div className="modal-dialog">
          <div className="modal-content">
            <div className="modal-header">
              <h1 className="modal-title fs-5" id="exampleModalLabel">
                Modal title
              </h1>
              <button
                type="button"
                className="btn-close"
                data-bs-dismiss="modal"
                aria-label="Close"
              ></button>
            </div>
            <div className="modal-body">...</div>
            <div className="modal-footer">
              <Button
                variant="secondary"
                label="Close"
                type="button"
                data-bs-dismiss="modal"
              />
              <Button variant="success" label="Save Change" type="button" />
            </div>
          </div>
        </div>
      </div>
    </div>
  );                                                                            
};

export default Modal;
