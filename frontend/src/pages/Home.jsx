import React from "react";
import Avatar from "../components/Avatar";
import Image1 from "../assets/images/avatar.png";
import CardProfile from "../components/CardProfile";
import Card from "../components/Card";
import Gap from "../components/Gap";
import Modal from "../components/Modal";
import gif from "../assets/images/giphy.gif";
import Comment from "../components/Comment";
import "./home.css";

const Home = () => {
  return (
    <>
      <div className="container-fluid">
        <div className="header">
          <div className="container overflow-hidden text-center">
            <div className="row gy-5">
              <div className="col-6">
                <div className="p-4">
                  <img src={gif} className="row" />
                </div>
              </div>
              <div className="col">
                <div className="p-3">
                  <div className="d-flex justify-center align-content-center">
                    <div>
                      <p class="first_line">Hello. My name is Onter</p>
                      <p class="second_line">
                        and I'm the onwer of GoBlog Group{" "}
                      </p>       
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <Comment /> 
          <div className="headline">
            <div className="container overflow-hidden text-center">
              <div className="row gy-5">
                <div className="col-6">
                  <div className="p-4">
                    <CardProfile />
                  </div>
                </div>
                <div className="col-6">
                  <div className="p-4">
                    <CardProfile />
                  </div>
                </div>
              </div>
              <div className="row gy-5">
                <div className="col-6">
                  <div className="p-4">
                    <CardProfile />
                  </div>
                </div>
              </div>
            </div>
            <Gap height={40} />
            <hr />
            <Gap height={18} />
            <div className="row">
              <div className="col-sm-8">
                <Card />
                <Gap height={18} />
                <Card />
                <Gap height={18} />
                <Card />
                <Gap height={18} />
                <Card />
                <Gap height={18} />
                <Card />
                <Gap height={18} />
                <Card />
                <Gap height={18} />
                <Card />
                <Gap height={18} />
                <Card />
                <Gap height={18} />
                <Card />
              </div>
              <div className="col-sm-4">
                <div className="sticky">
                  <Card />
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </>
  );
};

export default Home;
