import React, { useEffect, useRef, useState } from "react";
import Button from "../components/Button";
import ReactQuill from "react-quill";
import "react-quill/dist/quill.snow.css";

function NewStory() {
  const [content, setContent] = useState("");

  function handleContentChange(value) {
    setContent(value);
  }

  const handlePublish = () => {console.log(content); console.log(typeof(content));}

  const inputRef = useRef(null);
  useEffect(() => {
    inputRef.current.focus();
  }, []);

  return (
    <div className="container m-5">
      <div className="row">
        <div className="col">
          <Button label={"Publish"} variant={"success"} onClick={handlePublish} />
          <ReactQuill
            placeholder="Type your content here ..."
            ref={inputRef}
            className="mt-3"
            theme="snow"
            value={content}
            onChange={handleContentChange}
            modules={{
              toolbar: [
                [{ header: "1" }, { header: "2" }, { font: [] }],
                [{ size: [] }],
                ["bold", "italic", "underline", "strike", "blockquote"],
                [
                  { list: "ordered" },
                  { list: "bullet" },
                  { indent: "-1" },
                  { indent: "+1" },
                ],
                ["link", "image", "video"],
                ["clean"],
              ],
            }}
          />
        </div>
      </div>
      <div dangerouslySetInnerHTML={{ __html: content }} />
    </div>
  );
}

export default NewStory;
