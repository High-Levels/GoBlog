// import React, { useState, useRef, useEffect } from "react";
// import Button from "../../components/Button";
// import ReactQuill from "react-quill";
// import "react-quill/dist/quill.bubble.css";
// import Gap from "../../components/Gap";
// import axios, { AxiosHeaders } from "axios";
// import { useNavigate } from "react-router-dom";

// function NewStory() {
//   const [content, setContent] = useState("");
//   const [title, setTitle] = useState("");

//   const navigate = useNavigate();
//   const inputRef = useRef(null);

//   function handleContentChange(value) {
//     setContent(value);
//   }

//   const handleFocus = () => {
//     inputRef.current.style.outline = "none";
//   };

//   // // Store accumulated changes
//   // let change = new Delta();
//   // quill.on("text-change", function (delta) {
//   //   change = change.compose(delta);
//   // });

//   // // Save periodically
//   // setInterval(function () {
//   //   if (change.length() > 0) {
//   //     console.log("Saving changes", change);
//   //     change = new Delta();
//   //   }
//   // }, 5 * 1000);

//   // // Check for unsaved data
//   // window.onbeforeunload = function () {
//   //   if (change.length() > 0) {
//   //     return "There are unsaved changes. Are you sure you want to leave?";
//   //   }
//   // };

//   // const handlePublish = () => {
//   //   console.log(content);
//   //   console.log(typeof content);
//   // };

//   // const inputRef = useRef(null);

//   const handleSubmit = (e) => {
//     e.preventDefault();
//     //     axios
//     //       .post(`url`, content)
//     //       .then((res) => {
//     //         console.log(res);
//     //         alert("Artikel berhasil dipublish");
//     //         // setContent("");
//     //         navigate(`endpoint`);
//     //       })
//     // .catch((err) => {await
//     //         console.log(err);
//     //       });
//     //     console.log(content);
//     // console.log(title);
//     // console.log(content);
//   };

//   const modules = {
//     toolbar: [
//       ["bold", "italic", "underline", "strike"],
//       [{ color: [] }, { background: [] }],
//       [{ header: [1, 2, 3, 4, 5, 6, false] }],
//       [{ script: "sub" }, { script: "super" }],
//       ["blockquote"],
//       [{ list: "ordered" }, { list: "bullet" }],
//       [{ indent: "-1" }, { indent: "+1" }],
//       ["link", "image"],
//       ["clean"],
//     ],
//   };

//   useEffect(() => {
//     document.title = "New Story";
//   }, []);

//   return (
//     <div className="container  m-5 mx-auto">
//       <div className="row">
//         <div className="col">
//           <div>
//             <input
//               type="text"
//               placeholder="Judul artikel"
//               className="border-0 w-100 mx-3"
//               ref={inputRef}
//               onFocus={handleFocus}
//               onChange={(e) => setTitle(e.target.value)}
//               style={{ fontSize: "32px", fontWeight: "bold" }}
//             />
//           </div>
//           <form onSubmit={handleSubmit}>
//             <ReactQuill
//               placeholder="Tell your story ..."
//               className="mt-3"
//               theme="bubble"
//               value={content}
//               onFocus={() => setContent("")}
//               onChange={handleContentChange}
//               modules={modules}
//             />
//             <Gap height={18} />
//             <div className="mx-3">
//               <Button label="Publish" variant="success" type="submit" />
//             </div>
//           </form>
//         </div>
//       </div>
//     </div>
//   );
// }

// export default NewStory;

// // <div dangerouslySetInnerHTML={{ __html: content }}></div>
