import React from "react";
import Input from "../../components/Input";
import Button from "../../components/Button";
import { Link, useNavigate } from "react-router-dom";

const Profile = () => {
  Navigate = useNavigate()
  return (
    <div className="container-fluid">
      <hr />
      <header className="d-flex align-items-center justify-content-md-between p-3 mb-4 border-bottom">
        <h3 className="mt-2">Your Stories</h3>
        <div className="ms-auto d-flex gap-2">
          <Button label="Write a story" variant="secondary" />
          <Button label="Edit" variant="light" />
        </div>
      </header>
      <div className="d-flex p-3 gap-2">
        <Link to="/profile/draft">
          Draft
        </Link>
        <Link to="/profile/published">
          Published
        </Link>
        <Link to="/profile/respond">
          Response
        </Link>
      </div>
      <hr />
    </div>
  );
};

export default Profile;
