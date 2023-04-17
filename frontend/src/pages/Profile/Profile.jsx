import React from "react";
import Input from "../../components/Input";
import Button from "../../components/Button";
import Modal from "../../components/Modal";
import CardProfile from "../../components/CardProfile";
import { Account } from "./Account";
import { Link, useNavigate } from "react-router-dom";
import "./profile.css";

const Profile = () => {
  const navigate = useNavigate();
  const handleWriteStory = () => {
    navigate("/new-story");
  };
  return (
    <div className="container-fluid">
      <div className="prof">
        <CardProfile />
      </div>
      <header className="d-flex align-items-center justify-content-md-between p-3 mt-4 mb-4 border-bottom">
        <h3 className="mt-2">Your Stories</h3>
        <div className="ms-auto d-flex gap-2 p-3">
          <Button
            label="Write a story"
            variant="secondary"
            onClick={handleWriteStory}
          />
          <Button label="Edit" variant="light" />
        </div>
      </header>
      <div className="d-flex p-3 gap-2">
        <Link to="/profile/draft">Draft</Link>
        <Link to="/profile/published">Published</Link>
        <Link to="/profile/respond">Response</Link>
      </div>
      <hr />
    </div>
  );
};

export default Profile;
