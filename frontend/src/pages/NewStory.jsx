import React, { useEffect, useRef, useState } from "react";
import Button from "../components/Button";
import ReactQuill from "react-quill";
import "react-quill/dist/quill.snow.css";
import axios from "axios";
import { useNavigate } from "react-router-dom";

function NewStory() {
  const [content, setContent] = useState("");

  const navigate = useNavigate();

  function handleContentChange(value) {
    setContent(value);
  }

  const handlePublish = () => {console.log(content); console.log(typeof(content));}

  const inputRef = useRef(null);

  useEffect(() => {
    inputRef.current.focus();
    document.title = "New Story";
  }, []);

  const handleSubmit = (e) => {
    e.preventDefault();
    // axios
    //   .post(`url`, content)
    //   .then((res) => {
    //     console.log(res);

    //     navigate(`endpoint`);
    //   })
    //   .catch((err) => {
    //     console.log(err);
    //   });
    console.log(content);
  };

  const modules = {
    toolbar: [
      [{ font: [] }],
      [{ header: [1, 2, 3, 4, 5, 6, false] }],
      ["bold", "italic", "underline", "strike"],
      [{ color: [] }, { background: [] }],
      [{ script: "sub" }, { script: "super" }],
      ["blockquote", "code-block"],
      [{ list: "ordered" }, { list: "bullet" }],
      [{ indent: "-1" }, { indent: "+1" }, { align: [] }],
      ["link", "image"],
      ["clean"],
    ],
  };

  // const formats = [
  //   "header",
  //   "bold",
  //   "italic",
  //   "underline",
  //   "strike",
  //   "blockquote",
  //   "list",
  //   "bullet",
  //   "align",
  //   "color",
  //   "background",
  //   "link",
  //   "image",
  // ];

  return (
    <div className="container m-5 mx-auto">
      <div className="row">
        <div className="col">
<<<<<<< Updated upstream
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
=======
          <form onSubmit={handleSubmit}>
            <Button label="Publish" variant="success" type="submit" />
            <ReactQuill
              placeholder="Type your content here ..."
              ref={inputRef}
              className="mt-3"
              theme="snow"
              value={content}
              onChange={handleContentChange}
              modules={modules}
              // formats={formats}
            />
          </form>
          <div dangerouslySetInnerHTML={{ __html: content }}></div>
>>>>>>> Stashed changes
        </div>
      </div>
      <div dangerouslySetInnerHTML={{ __html: content }} />
    </div>
  );
}

export default NewStory;
