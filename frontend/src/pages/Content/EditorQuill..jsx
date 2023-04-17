import { useEffect } from "react";
import { useQuill } from "react-quilljs";
import BlotFormatter from "quill-blot-formatter";
import "quill/dist/quill.snow.css";

import "./styles.css";

const Editor = () => {
  const { quill, quillRef, Quill } = useQuill({
    modules: { blotFormatter: {} },
  });

  if (Quill && !quill) {
    // const BlotFormatter = require('quill-blot-formatter');
    Quill.register("modules/blotFormatter", BlotFormatter);
  };

  const handlesubmit = (e) => {
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
      <div ref={quillRef} />
      <button
        type="button"
        class="btn btn-primary"
        data-bs-toggle="modal"
        data-bs-target="#exampleModal"
        className="mt-3"
      >
        Publish
      </button>

      <div
        class="modal fade"
        id="exampleModal"
        tabindex="-1"
        aria-labelledby="exampleModalLabel"
        aria-hidden="true"
      >
        <div class="modal-dialog">
          <div class="modal-content">
            <div class="modal-header">
              <h1 class="modal-title fs-5" id="exampleModalLabel">
                Description
              </h1>
              <button
                type="button"
                class="btn-close"
                data-bs-dismiss="modal"
                aria-label="Close"
              ></button>
            </div>
            <div class="modal-body">...</div>
            <div class="modal-footer">
              <button
                type="button"
                class="btn btn-secondary"
                data-bs-dismiss="modal"
              >
                Close
              </button>
              <button type="button" class="btn btn-primary">
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
