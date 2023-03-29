import React, { useEffect, useRef, useState } from "react";
import Button from "../components/Button";

function NewStory() {
  const [title, setTitle] = useState("Title");
  const [content, setContent] = useState("Type your content here ...");

  const inputRef = useRef(null);
  useEffect(() => {
    inputRef.current.focus();
  }, []);

  return (
    <div className="container m-5">
      <div className="row">
        <div className="col">
          <Button label={"Publish"} variant={"success"} />
          <div className="d-flex mt-3">
            <h1
              contentEditable="true"
              style={{ outline: "0px solid transparent" }}
              className="text-secondary w-100"
              onChange={(e) => setTitle(e.target.innerText)}
            >
              {title}
            </h1>
          </div>
          <div className="d-flex">
            <p
              contentEditable="true"
              style={{ outline: "0px solid transparent" }}
              id="text-paragraph"
              className="text-secondary w-100"
              onChange={(e) => setContent(e.target.innerText)}
              ref={inputRef}
            >
              {content}
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}

export default NewStory;
