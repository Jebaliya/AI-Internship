import React from "react";
import { createRoot } from "react-dom/client";
import App from "./App";
import Footer from "./component/footer";
import Header from "./component/header";
import "./styles.css";

createRoot(document.getElementById("root")).render(
  <div>
    <Header />
    <App />
    <Footer />
  </div>
);
