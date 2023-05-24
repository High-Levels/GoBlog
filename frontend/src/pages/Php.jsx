import React from "react";
import Hola from "../assets/images/200w.webp";
import Avatar from "../components/Avatar";
import { Link } from "react-router-dom";

const PageNotFound = () => {
  return (
    <div className="px-4 py-5 my-5 text-center">
      <Avatar src={Hola} height={100} className="mb-5" />
      <h1>404 Error</h1>
      <h1>Page Not Found</h1>
      <Link to="/">Home</Link>
    </div>
  );
};

export default PageNotFound;
