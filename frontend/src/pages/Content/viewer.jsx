import ReactMarkdown from "react-markdown";


export default function Viewer() {
  return <ReactMarkdown>{props.value}</ReactMarkdown>;
}
