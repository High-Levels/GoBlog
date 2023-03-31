import React, { useState, useRef, useEffect } from "react";
import Button from "../components/Button";
import ReactQuill from "react-quill";
import "react-quill/dist/quill.snow.css";
import Gap from "../components/Gap";
import axios from "axios";
import { useNavigate } from "react-router-dom";

function NewStory() {
  const [content, setContent] = useState("input type here");
  const {Header, Article} = content;
  
  const navigate = useNavigate();
  
  function handleContentChange(value) {
    
    setContent(value);
    console.log(content)
  }

  // const handlePublish = () => {
  //   console.log(content);
  //   console.log(typeof content);
  // };

  // const inputRef = useRef(null);

  // useEffect(() => {
  //   document.title = "New Story";
  //   inputRef.current.focus();
  //   if (inputRef.current) {
  //     const input = inputRef.current.getEditor();

  //     const headingPlaceholder = "<h2><b>Judul Artikel</b></h2>";
  //     const paragraphPlaceholder = "<p>Ketikkan konten Anda di sini ...</p>";

  //     input.root.innerHTML = headingPlaceholder + paragraphPlaceholder;

  //     input.formatLine(0, 1, { header: 2 });

  //     input.on("text-change", () => {
  //       const isEmpty = input.getText().trim().length === 0;
  //       if (isEmpty) {
  //         input.root.innerHTML = headingPlaceholder + paragraphPlaceholder;
  //         input.formatLine(0, 1, { header: 2 });
  //       }
  //     });

  //     input.root.addEventListener("click", () => {
  //       const isEmpty = input.getText().trim().length === 0;
  //       if (isEmpty) {
  //         input.root.innerHTML = "";
  //       }
  //     });
  //   }
  // }, []);

  const handleSubmit = (e) => {
    e.preventDefault();
    //     axios
    //       .post(`url`, content)
    //       .then((res) => {
    //         console.log(res);
    //         alert("Artikel berhasil dipublish");
    //         // setContent("");
    //         navigate(`endpoint`);
    //       })
    // .catch((err) => {await
    //         console.log(err);
    //       });
    //     console.log(content);
  };

  const modules = {
    toolbar: [  
      ["bold", "italic", "underline", "strike"],
      [{ color: [] }, { background: [] }],
      [{ 'header': [1, 2, 3, 4, 5, 6, false]}, Header], 
      [{ script: "sub" }, { script: "super" }],
      ["blockquote"],
      [{ list: "ordered" }, { list: "bullet" }],
      [{ indent: "-1" }, { indent: "+1" }],
      ["link", "image"],
      ["clean"],
    ],
  };

  // const placeholder1 = "Title";
  // const placeholder2 = "Type your content here...";

  return (
    <div className="container m-5 mx-auto">
      <div className="row">
        <div className="col">
          <form onSubmit={handleSubmit}>
            <ReactQuill
              // placeholder1={placeholder1}
              // placeholder2={placeholder2}
              // ref={inputRef}
              className="mt-3"
              theme="snow"
              value={content}
              onFocus={() => setContent("")}
              onChange={handleContentChange}
              modules={modules}
            />
            <Gap height={18}/>
            <Button label="Publish" variant="success" type="submit" />
          </form>
     
        </div>
      </div>
    </div>
  );
}

export default NewStory;

// <div dangerouslySetInnerHTML={{ __html: content }}></div>