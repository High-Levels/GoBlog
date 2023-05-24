import React from "react";
import Input from "../../components/Input";
import Button from "../../components/Button";
import { Draft } from "./Draft";

const Profile = () => {
  return (
    <div className="container-fluid">
      <hr />
      <header className="d-flex align-items-center justify-content-md-between p-3 mb-4 border-bottom">
        <h3 className="mt-2">Your Stories</h3>
        <div className="ms-auto d-flex gap-2">
          <Button label="Write a story" variant="secondary" />
          <Button label="Edit" style={{
            color:"red",
            }}/>
        </div>
      </header>
      <div className="d-flex p-3 gap-2">
        <Button label="Draft" variant="primary" />
        <Button label="Published" variant="primary" />
        <Button label="Response" variant="primary" />
        <button className="btn btn-primary" onClick={useEffect(() => {
          effect
          return () => {
            cleanup
          };
        }, [input])}>djckajk</button>
      </div>
    </div>
  );
};

export default Profile;
