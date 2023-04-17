import { useEffect, useState } from "react";
import { useQuill } from "react-quilljs";
import BlotFormatter from "quill-blot-formatter";
import "quill/dist/quill.snow.css";
// import axios from "axios";
import "./styles.css";

const Editor = () => {
  const { quill, quillRef, Quill } = useQuill({
    modules: { blotFormatter: {} },
  });

  if (Quill && !quill) {
    // const BlotFormatter = require('quill-blot-formatter');
    Quill.register("modules/blotFormatter", BlotFormatter);
  }

  const [artikel, setArtikel] = useState({
    title: "",
    content: "",
  });

  const handlesubmit = (e) => {
    const handleinput = (e) => {
      const { name, value } = e.target;
      setArtikel({ ...artikel, [name]: value });
    };

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
    // console.log(title);
    // console.log(content);
  };

  useEffect(() => {
    if (quill) {
      quill.on("text-change", (delta, oldContents) => {
        console.log("Text change!");
        console.log(delta);

        let currrentContents = quill.getContents();
        console.log(currrentContents.diff(oldContents));
      });
    }
  }, [quill, Quill]);

  return (
    <div>
      <form onSubmit={handlesubmit}>
        <div ref={quillRef} value={artikel.content} />
        <button
          type="button"
          className="btn btn-primary mt-3"
          data-bs-toggle="modal"
          data-bs-target="#exampleModal"
        >
          Publish
        </button>

        <div
          className="modal fade"
          id="exampleModal"
          tabindex="-1"
          aria-labelledby="exampleModalLabel"
          aria-hidden="true"
        >
          <div className="modal-dialog">
            <div className="modal-content">
              <div className="modal-header">
                <h1 className="modal-title fs-5" id="exampleModalLabel">
                  Description
                </h1>
                <button
                  type="button"
                  className="btn-close"
                  data-bs-dismiss="modal"
                  aria-label="Close"
                ></button>
              </div>
              <div className="modal-body">
                <textarea
                  className=""
                  // {onChange={handleinput}}
                  value={artikel.title}
                >
                  input your description
                </textarea>
              </div>
              <div className="modal-footer">
                <button
                  type="button"
                  className="btn btn-secondary"
                  data-bs-dismiss="modal"
                >
                  Close
                </button>
                <button type="button" className="btn btn-primary">
                  Save
                </button>
              </div>
            </div>
          </div>
        </div>
      </form>
    </div>
  );
};

export default Editor;
