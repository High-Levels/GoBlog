import React from "react";
import Avatar from "../components/Avatar";
import Image1 from "../assets/images/avatar.png";
import CardProfile from "../components/CardProfile";
import Card from "../components/Card";
import Gap from "../components/Gap";
import "./home.css";
import Modal from "../components/Modal";
import gif from "../assets/images/giphy.gif";

const Home = () => {
  var i = 0;
  var txt = "Lorem ipsum dummy text blabla.";
  var speed = 50;

  const typeWriter = () => {
    if (i < txt.length) {
      document.getElementById("demo").innerHTML += txt.charAt(i);
      i++;
      setTimeout(typeWriter, speed);
    }
  };

  return (
    <>
      <div className="container-fluid">
        <div className="header">
          <div className="inside">
            <div>
              <div className="row">
                <div className="col">
                  <div className="p-3">
                    <img src={gif} className="gif" />
                  </div>
                </div>
                <div className="col">
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
                <div className="col-6">
                  <div className="p-4">
                    <div className="a">aaa</div>
                  </div>
                </div>
              </div>
            </div>
            <Gap height={40} />
            <hr />
            <Gap height={18} />
            <div class="row">
              <div class="col-sm-8">
              <div class="overflow-y-scroll">
                <Card />
                <Gap height={18} />
                <Card />
                <Gap height={18} />
                <Card />
                <Card />
                <Gap height={18} />
                <Card />
                <Gap height={18} />
                <Card />
                <Card />
                <Gap height={18} />
                <Card />
                <Gap height={18} />
                <Card />
                </div>
              </div>
              <div class="col-sm-4">
                <div>
                  Stick to the top on viewports sized MD (medium) or wider
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
