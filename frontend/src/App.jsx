import React, { useState } from "react";
import api from "./api";

export default function App() {
  const [query, setQuery] = useState("");
  const [response, setResponse] = useState("");
  const [file, setFile] = useState(null);
  const [summary, setSummary] = useState("");
  const [keywords, setKeywords] = useState([]);

  const sendQuery = async () => {
    const res = await api.post("/chat", { query });
    setResponse(res.data.response);
  };

  const uploadFile = async () => {
    const form = new FormData();
    form.append("file", file);
    const res = await api.post("/upload", form);
    setSummary(res.data.summary || "");
    setKeywords(res.data.keywords || []);
  };

  return (
    <div style={{ padding: 30, fontFamily: "Arial" }}>
      <h1>Smart Enterprise Assistant</h1>
      <input value={query} onChange={e => setQuery(e.target.value)} placeholder="Ask a question" />
      <button onClick={sendQuery}>Send</button>
      <p><strong>Response:</strong> {response}</p>
      <hr />
      <input type="file" onChange={e => setFile(e.target.files[0])} />
      <button onClick={uploadFile} disabled={!file}>Upload</button>
      <p><strong>Summary:</strong> {summary}</p>
      <p><strong>Keywords:</strong> {keywords.join(", ")}</p>
    </div>
  );
}
